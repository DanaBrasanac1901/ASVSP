from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def quiet_logs(sc):
    logger = sc._jvm.org.apache.log4j
    logger.LogManager.getLogger("org").setLevel(logger.Level.ERROR)
    logger.LogManager.getLogger("akka").setLevel(logger.Level.ERROR)

spark = SparkSession \
    .builder \
    .appName("Ingest Bulk CSV to Hadoop") \
    .master("spark://spark-master:7077") \
    .getOrCreate()

quiet_logs(spark)

csv_arrests_path = "/home/sourceData/arrests/csv/*.csv"
csv_detentions_path = "/home/sourceData/detentions/csv/*.csv"
csv_removals_path = "/home/sourceData/removals/csv/*.csv"
csv_risk_path = "/home/sourceData/risk_classification/csv/*.csv"

hdfs_destination_arrests = "hdfs://namenode:9000/user/root/raw/arrests"
hdfs_destination_detentions = "hdfs://namenode:9000/user/root/raw/detentions"
hdfs_destination_removals = "hdfs://namenode:9000/user/root/raw/removals"
hdfs_destination_risk = "hdfs://namenode:9000/user/root/raw/risk_classification"

print(f"--- Loading all CSV files from: {csv_arrests_path} ---")

# Adjust options based on your CSV structure (e.g., delimiter=";")
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(csv_arrests_path)

print(f"Total rows loaded: {df.count()}")
df.printSchema()

print(f"--- Streaming data over network to Hadoop: {hdfs_destination_arrests} ---")

df.write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv(hdfs_destination_arrests)
    
print(f"--- Loading all CSV files from: {csv_detentions_path} ---")

# Adjust options based on your CSV structure (e.g., delimiter=";")
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(csv_detentions_path)

print(f"Total rows loaded: {df.count()}")
df.printSchema()

print(f"--- Streaming data over network to Hadoop: {hdfs_destination_detentions} ---")

df.write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv(hdfs_destination_detentions)
    
print(f"--- Loading all CSV files from: {csv_removals_path} ---")

# Adjust options based on your CSV structure (e.g., delimiter=";")
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(csv_removals_path)

print(f"Total rows loaded: {df.count()}")
df.printSchema()

print(f"--- Streaming data over network to Hadoop: {hdfs_destination_removals} ---")

df.write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv(hdfs_destination_removals)

print(f"--- Loading all CSV files from: {csv_risk_path} ---")

# Adjust options based on your CSV structure (e.g., delimiter=";")
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(csv_risk_path)

print(f"Total rows loaded: {df.count()}")
df.printSchema()

print(f"--- Streaming data over network to Hadoop: {hdfs_destination_risk} ---")

df.write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv(hdfs_destination_risk)
    
print("--- Pipeline Complete! Data successfully landed in Hadoop. ---")
