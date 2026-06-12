from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, trim, upper, to_date, year, when


# ── Suppress noisy logs (same helper as ingest.py) ────────────────────────────
def quiet_logs(sc):
    logger = sc._jvm.org.apache.log4j
    logger.LogManager.getLogger("org").setLevel(logger.Level.ERROR)
    logger.LogManager.getLogger("akka").setLevel(logger.Level.ERROR)


# ── Generic helpers ───────────────────────────────────────────────────────────

def drop_redacted_columns(df: DataFrame) -> DataFrame:
    """
    Drop columns where every value is a FOIA privacy redaction marker.
    These columns contain only '(b)(6)(b)(7)(c)' or variants and carry
    no analytical value.
    """
    redacted_markers = {"(b)(6)(b)(7)(c)", "(b)(6),(b)(7)(c)", "b(6), b(7)c"}
    cols_to_drop = []
    for c in df.columns:
        distinct_vals = {
            row[0]
            for row in df.select(col(c).cast("string")).distinct().limit(5).collect()
            if row[0] is not None
        }
        if distinct_vals and distinct_vals.issubset(redacted_markers):
            cols_to_drop.append(c)
    if cols_to_drop:
        print(f"  Dropping fully-redacted columns: {cols_to_drop}")
    return df.drop(*cols_to_drop)


def trim_strings(df: DataFrame) -> DataFrame:
    """Trim leading/trailing whitespace from all string columns."""
    string_cols = [c for c, t in df.dtypes if t == "string"]
    for c in string_cols:
        df = df.withColumn(c, trim(col(c)))
    return df


def replace_empty_with_null(df: DataFrame) -> DataFrame:
    """Replace empty strings with NULL so null handling is consistent."""
    string_cols = [c for c, t in df.dtypes if t == "string"]
    for c in string_cols:
        df = df.withColumn(c, when(col(c) == "", None).otherwise(col(c)))
    return df


def write_clean(df: DataFrame, hdfs_path: str, name: str):
    print(f"\n--- Writing clean {name} to {hdfs_path} ---")
    print(f"  Row count: {df.count()}")
    df.write.mode("overwrite").parquet(hdfs_path)
    print(f"  Done.")


# ── Spark session ─────────────────────────────────────────────────────────────
spark = (
    SparkSession.builder
    .appName("Transform - Cleaning Zone")
    .master("spark://spark-master:7077")
    .getOrCreate()
)
quiet_logs(spark)

HDFS = "hdfs://namenode:9000"
RAW  = f"{HDFS}/user/root/raw"
CLEAN = f"{HDFS}/user/root/clean"


# ─────────────────────────────────────────────────────────────────────────────
# 1. ARRESTS
# ─────────────────────────────────────────────────────────────────────────────
print("\n========== ARRESTS ==========")
arrests = spark.read.parquet(f"{RAW}/arrests")

# Drop redacted columns (Case ID, Subject ID, Alien File Number, Arrest Created By)
arrests = drop_redacted_columns(arrests)

# Fix date type
arrests = arrests.withColumn(
    "Apprehension Date", to_date(col("Apprehension Date"), "yyyy-MM-dd")
)

# Standardize categoricals
arrests = arrests.withColumn("Apprehension Method", trim(col("Apprehension Method")))

# Drop duplicates on the only real unique key available
arrests = arrests.dropDuplicates(["Anonymized Identifier"])

# Trim + empty → null
arrests = trim_strings(arrests)
arrests = replace_empty_with_null(arrests)

print("  Schema after cleaning:")
arrests.printSchema()
write_clean(arrests, f"{CLEAN}/arrests", "arrests")


# ─────────────────────────────────────────────────────────────────────────────
# 2. DETENTIONS
# ─────────────────────────────────────────────────────────────────────────────
print("\n========== DETENTIONS ==========")
detentions = spark.read.parquet(f"{RAW}/detentions")

# Drop redacted columns (Detention ID, Case ID, Subject ID, Alien File Number, Birth Date)
detentions = drop_redacted_columns(detentions)

# Fix date types (already DATE in schema but inferSchema sometimes reads as string)
for date_col in ["Stay Book In Date", "Detention Book In Date",
                  "Detention Book Out Date", "Stay Book Out Date",
                  "Final Order Date", "Departed Date"]:
    detentions = detentions.withColumn(date_col, to_date(col(date_col)))

# Drop corrupt birth years — valid range 1900 is suspiciously low, cap at 1920-2010
detentions = detentions.filter(
    col("Birth Year").isNull() |
    (col("Birth Year").between(1920, 2010))
)

# Drop corrupt final order dates (future dates beyond 2025 are data errors)
detentions = detentions.filter(
    col("Final Order Date").isNull() |
    (year(col("Final Order Date")) <= 2025)
)

# Drop corrupt departed dates (same reason)
detentions = detentions.filter(
    col("Departed Date").isNull() |
    (year(col("Departed Date")) <= 2025)
)

# Case threat level should only be 1, 2, or 3
detentions = detentions.filter(
    col("Case Threat Level").isNull() |
    col("Case Threat Level").between(1, 3)
)

# Standardize gender casing
detentions = detentions.withColumn("Gender", upper(trim(col("Gender"))))

# Drop full duplicates
detentions = detentions.dropDuplicates()

# Trim + empty → null
detentions = trim_strings(detentions)
detentions = replace_empty_with_null(detentions)

print("  Schema after cleaning:")
detentions.printSchema()
write_clean(detentions, f"{CLEAN}/detentions", "detentions")


# ─────────────────────────────────────────────────────────────────────────────
# 3. REMOVALS
# ─────────────────────────────────────────────────────────────────────────────
print("\n========== REMOVALS ==========")
removals = spark.read.parquet(f"{RAW}/removals")

# Drop fully redacted columns (Case ID, Alien File Number, Birth Date — 100% null)
removals = drop_redacted_columns(removals)

# Birth Date is 100% null — drop it explicitly
if "Birth Date" in removals.columns:
    removals = removals.drop("Birth Date")
    print("  Dropped 'Birth Date' column (100% null)")

# Fix date types
for date_col in ["Departure Date", "Final Order Date",
                  "MSC Charge Date", "MSC Conviction Date"]:
    removals = removals.withColumn(date_col, to_date(col(date_col)))

# Apprehension Date is a TIMESTAMP — cast to date only
removals = removals.withColumn(
    "Apprehension Date", to_date(col("Apprehension Date"))
)

# Entry Date has corrupt far-future values (e.g. 2110) — drop them
removals = removals.filter(
    col("Entry Date").isNull() |
    (year(col("Entry Date")) <= 2024)
)

# Drop corrupt final order dates
removals = removals.filter(
    col("Final Order Date").isNull() |
    (year(col("Final Order Date")) <= 2025)
)

# Standardize gender casing
removals = removals.withColumn("Gender", upper(trim(col("Gender"))))

# Standardize country name casing (already uppercase per schema, ensure consistent)
for country_col in ["Departure Country", "Birth Country", "Citizenship Country"]:
    removals = removals.withColumn(country_col, upper(trim(col(country_col))))

# Drop full duplicates
removals = removals.dropDuplicates()

# Trim + empty → null
removals = trim_strings(removals)
removals = replace_empty_with_null(removals)

print("  Schema after cleaning:")
removals.printSchema()
write_clean(removals, f"{CLEAN}/removals", "removals")


# ─────────────────────────────────────────────────────────────────────────────
# 4. RISK CLASSIFICATION
# ─────────────────────────────────────────────────────────────────────────────
print("\n========== RISK CLASSIFICATION ==========")
risk = spark.read.parquet(f"{RAW}/risk_classification")

# Drop redacted columns (A_NUMBER, SUBJ_ID, LAST_NAME, FIRST_NAME, OFFICER_ID etc.)
risk = drop_redacted_columns(risk)

# Drop columns with extreme null rates that carry no analytical value
#   FO_DATE_AT_RCA_DECISION     96.75% null
#   RCA_DECISION_DATE           90.96% null
#   fiscal_year_code            90.96% null  (also only value is 2013)
#   fiscal_quarter_name         90.96% null
#   DISC_INFR_VER               99.99% null
#   ANONYMIZED_IDENTIFIER       90.98% null
high_null_cols = [
    "FO_DATE_AT_RCA_DECISION",
    "RCA_DECISION_DATE",
    "fiscal_year_code",
    "fiscal_quarter_name",
    "DISC_INFR_VER",
    "ANONYMIZED_IDENTIFIER",
    "SPECIAL_VULNERABILITY_COMMENTS",  # 71.7% null, free text, not useful
    "OFFICER_COMMENTS",                # 6.31% null but free text
    "SUPERVISOR_COMMENTS",             # free text
]
existing_high_null = [c for c in high_null_cols if c in risk.columns]
print(f"  Dropping high-null / free-text columns: {existing_high_null}")
risk = risk.drop(*existing_high_null)

# Fix date types
risk = risk.withColumn("SUBMISSION_DATE", to_date(col("SUBMISSION_DATE")))

# Standardize categoricals to uppercase
for cat_col in ["ACTIVE_INACTIVE", "STATUS_CODE", "RISK_TO_PUBLIC_SAFETY",
                 "RISK_OF_FLIGHT", "OFFICER_AGREE_DISAGREE",
                 "SUPERVISOR_AGREE_DISAGREE", "RCA_FINAL_DECISION"]:
    if cat_col in risk.columns:
        risk = risk.withColumn(cat_col, upper(trim(col(cat_col))))

# FINAL_BOND_AMOUNT: -1 appears to be a sentinel for "no bond" — replace with null
risk = risk.withColumn(
    "FINAL_BOND_AMOUNT",
    when(col("FINAL_BOND_AMOUNT") == -1, None).otherwise(col("FINAL_BOND_AMOUNT"))
)

# Drop full duplicates
risk = risk.dropDuplicates()

# Trim + empty → null
risk = trim_strings(risk)
risk = replace_empty_with_null(risk)

print("  Schema after cleaning:")
risk.printSchema()
write_clean(risk, f"{CLEAN}/risk_classification", "risk_classification")


# ─────────────────────────────────────────────────────────────────────────────
print("\n========== TRANSFORMATION COMPLETE ==========")
print(f"All cleaned datasets written to {CLEAN}/")
print("Next step: run curate.py to build the star schema in /user/root/curated/")

spark.stop()
