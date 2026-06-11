# ASVSP projekat - Dana Brašanac E2 19/2025 - Analiza podataka ICE hapšenja, pritvora, i deportacija u odnosu na podatke o susretanju migranata pri pokušaju ulaska u SAD

## Istorijski skup - source i format

Primarni (istorijski skup) https://www.kaggle.com/datasets/bwandowando/ice-2012-2023-historical-data/data

#### **arrests_2011_2023.csv (273.13 MB)**

Sumarizovana tabela:

| column_name | column_type | min | max | approx_unique | count | null_percentage |
| --- | --- | --- | --- | --- | --- | --- |
| Apprehension Date | VARCHAR | 2011-10-01 | 2023-09-30 | 3,587 | 1,813,280 | 0 |
| Apprehension Method | VARCHAR | 287(g) Program | Worksite Enforcement | 29 | 1,813,280 | 0 |
| Arrest Created By | VARCHAR | (b)(6)(b)(7)(c) | (b)(6)(b)(7)(c) | 1 | 1,813,280 | 0 |
| Case ID | VARCHAR |  | (b)(6)(b)(7)(c) | 2 | 1,813,280 | 0 |
| Subject ID | VARCHAR | (b)(6)(b)(7)(c) | (b)(6)(b)(7)(c) | 1 | 1,813,280 | 0 |
| Alien File Number | VARCHAR |  | (b)(6)(b)(7)(c) | 2 | 1,813,280 | 0 |
| Anonymized Identifier | VARCHAR |  | fffffd02ff3b012bbca32c29ec95b106d89f33f0 | 1,370,263 | 1,813,280 | 0 |

#### **detentions_2011_2023.csv (4.13 GB)**

summarized:

| column_name | column_type | min | max | approx_unique | avg | count | null_percentage |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Detention ID | VARCHAR | (b)(6)(b)(7)(c) | nan | 855,610 |  | 8,458,563 | 0 |
| Case ID | VARCHAR | (b)(6)(b)(7)(c) | (b)(6),(b)(7)(c) | 3 |  | 8,458,563 | 1.03 |
| Subject ID | VARCHAR | (b)(6)(b)(7)(c) | (b)(6),(b)(7)(c) | 2 |  | 8,458,563 | 0 |
| Stay Book In Date | DATE | 1995-08-31 | 2023-11-14 | 5,353 | 2017-02-21 07:40:12.707265 | 8,458,563 | 0 |
| Detention Book In Date | DATE | 2012-01-01 | 2023-11-15 | 4,824 | 2017-03-11 03:09:12.692603 | 8,458,563 | 0 |
| Detention Facility | VARCHAR | (OLD) CENTRAL REGIONAL JAIL | YUMA HOLDROOM | 1,215 |  | 8,458,563 | 0 |
| Detention Facility Code | VARCHAR | AAORDMD | YUMHOLD | 1,199 |  | 8,458,563 | 0 |
| Detention Book Out Date | DATE | 2012-01-01 | 2023-11-15 | 4,824 | 2017-03-16 05:53:26.474097 | 8,458,563 | 0.47 |
| Detention Release Reason | VARCHAR | ATD - Alternatives to Detention | Withdrawal - lack of space | 48 |  | 8,458,563 | 0.47 |
| Stay Book Out Date | DATE | 2012-01-01 | 2023-11-14 | 4,824 | 2017-03-31 02:55:38.408429 | 8,458,563 | 0.87 |
| Stay Release Reason | VARCHAR | ATD - Alternatives to Detention | Withdrawal - lack of space | 48 |  | 8,458,563 | 0.87 |
| Religion | VARCHAR |  | veracruz | 536 |  | 8,458,563 | 0 |
| Marital | VARCHAR | Divorced | Widowed | 6 |  | 8,458,563 | 0.77 |
| Gender | VARCHAR | Female | Unknown | 3 |  | 8,458,563 | 0 |
| Birth Date | VARCHAR | (b)(6)(b)(7)(c) | (b)(6),(b)(7)(c) | 2 |  | 8,458,563 | 0 |
| Ethnicity | VARCHAR | Hispanic Origin | Unknown | 3 |  | 8,458,563 | 56.44 |
| Alien File Number | VARCHAR | (b)(6)(b)(7)(c) | (b)(6),(b)(7)(c) | 2 |  | 8,458,563 | 0.42 |
| Birth Year | BIGINT | 1900 | 2023 | 122 | 1985.2437922834247 | 8,458,563 | 0 |
| Entry Status | VARCHAR | Absconder | Visitor | 55 |  | 8,458,563 | 3.47 |
| Bond Posted Date | TIMESTAMP | 1976-08-25 00:00:00 | 2023-11-14 18:16:29 | 274,028 | 2016-03-17 08:39:09.519184 | 8,458,563 | 84.47 |
| Bond Posted Amount | BIGINT | 100 | 1250000 | 219 | 7672.749716756158 | 8,458,563 | 84.47 |
| Initial Bond Set Amount | BIGINT | 1 | 999999999 | 311 | 20528.49169371739 | 8,458,563 | 82.49 |
| Case Status | VARCHAR | 0-Withdrawal Permitted - I-275 Issued | Z-SAW - Permanent Residence Granted | 13 |  | 8,458,563 | 1.03 |
| Case Category | VARCHAR | [10] Visa Waiver Deportation / Removal | [9] VR Under Safeguards | 38 |  | 8,458,563 | 1.03 |
| Final Order Yes No | BOOLEAN | false | true | 2 |  | 8,458,563 | 1.03 |
| Final Order Date | DATE | 1911-05-19 | 2029-05-19 | 11,113 | 2015-07-14 15:04:32.796822 | 8,458,563 | 30.31 |
| Departed Date | DATE | 1923-09-14 | 2031-03-17 | 5,007 | 2016-11-09 12:18:31.643897 | 8,458,563 | 34.18 |
| Departure Country | VARCHAR | AFGHANISTAN | ZIMBABWE | 256 |  | 8,458,563 | 34.25 |
| Case Threat Level | BIGINT | 1 | 3 | 3 | 1.9209439605021914 | 8,458,563 | 51.08 |
| Charge | VARCHAR | ** AGGRAVATED FELONY | WAS INADMISSIBLE AT TIME OF ENTRY AS ALIEN PREVIOUSLY REMOVED AS INADMISSIBLE (EXCLUDED) SEEKING ENTRY WITHIN 5 YEARS (20 YEARS IF TWICE OR AG FELON) | 265 |  | 8,458,563 | 34.42 |
| Charge Code | VARCHAR | 21210 | WITIH | 205 |  | 8,458,563 | 0 |
| Charge Section Code | VARCHAR | 212A2C | 241a9 | 125 |  | 8,458,563 | 34.42 |
| Anonymized Identifier | VARCHAR | 0000006d23db86858bf081aa7482940341ac9983 | fffffd02ff3b012bbca32c29ec95b106d89f33f0 | 3,128,669 |  | 8,458,563 | 0.42 |

Notes:

Even though there are 855,610 values for "Detention ID",
the most common value '(b)(6)(b)(7)(c)' appears in 5,645,755 rows,
and the second most common '(b)(6),(b)(7)(c)' appears in 1,999,717 rows.

The third and following most common values appear no more than 5 times.

So this column is also annonimised like a lot of others, and probably isn't worth taking into account.

#### **removals_2011_2023.csv (1.22 GB)**

| column_name | column_type | min | max | approx_unique | count | null_percentage |
| --- | --- | --- | --- | --- | --- | --- |
| Departure Date | DATE | 2011-10-01 | 2023-09-30 | 4,824 | 2,771,204 | 0 |
| Port of Departure | VARCHAR | ABERDEEN, WA, POE | YSLETA, TX, POE | 458 | 2,771,204 | 0 |
| Departure Country | VARCHAR | AFGHANISTAN | ZIMBABWE | 256 | 2,771,204 | 0 |
| Case Status | VARCHAR | 0-Withdrawal Permitted - I-275 Issued | X-Section 250 Removal | 6 | 2,771,204 | 0 |
| Case Category | VARCHAR | [10] Visa Waiver Deportation / Removal | [9] VR Under Safeguards | 38 | 2,771,204 | 0 |
| Final Order Yes No | BOOLEAN | false | true | 2 | 2,771,204 | 0 |
| Final Order Date | DATE | 1911-05-19 | 2029-05-19 | 10,570 | 2,771,204 | 5.82 |
| Case ID | VARCHAR | (b)(6)(b)(7)(c) | (b)(6),(b)(7)(c) | 3 | 2,771,204 | 0 |
| Gender | VARCHAR | Female | Unknown | 3 | 2,771,204 | 0 |
| Birth Country | VARCHAR | AFGHANISTAN | ZIMBABWE | 228 | 2,771,204 | 0 |
| Citizenship Country | VARCHAR | AFGHANISTAN | ZIMBABWE | 224 | 2,771,204 | 0 |
| Birth Date | VARCHAR |  |  | 0 | 2,771,204 | 100 |
| Birth Year | BIGINT | 1900 | 2023 | 124 | 2,771,204 | 0 |
| Alien File Number | VARCHAR | (b)(6)(b)(7)(c) | (b)(6),(b)(7)(c) | 2 | 2,771,204 | 0.38 |
| Entry Status | VARCHAR | Absconder | Visitor | 53 | 2,771,204 | 0.87 |
| Entry Date | DATE | 1900-03-03 | 2110-09-14 | 15,252 | 2,771,204 | 26.25 |
| MSC Charge | VARCHAR | Abduct-No Ransom or Assault | Witness - Dissuading | 432 | 2,771,204 | 43.52 |
| MSC Charge Date | DATE | 1962-07-28 | 2023-09-25 | 13,537 | 2,771,204 | 46.14 |
| MSC Charge Code | VARCHAR | 0101 | 93AA | 639 | 2,771,204 | 43.52 |
| MSC Conviction Date | DATE | 1962-07-28 | 2031-07-18 | 12,476 | 2,771,204 | 43.52 |
| MSC Criminal Charge Status | VARCHAR | Convicted | Pending | 3 | 2,771,204 | 43.52 |
| Case Threat Level | BIGINT | 1 | 3 | 3 | 2,771,204 | 43.52 |
| Processing Disposition Code | VARCHAR | ABS | WD2 | 58 | 2,771,204 | 0.05 |
| Processing Disposition | VARCHAR | ADMINISTRATIVE DEPORTATION I-851/I-851A | Withdrawal in Lieu of NTA | 54 | 2,771,204 | 0.05 |
| Current Program | VARCHAR | 287G Program | Violent Criminal Alien Section | 33 | 2,771,204 | 1 |
| Apprehension Date | TIMESTAMP | 1966-07-26 00:00:00 | 2023-10-27 16:54:14 | 1,177,338 | 2,771,204 | 1.36 |
| Charge Section Code | VARCHAR | 212A2C | 241a9B | 130 | 2,771,204 | 0.44 |
| Charge Code | VARCHAR | 21210 | WITIH | 207 | 2,771,204 | 0 |
| Anonymized Identifer | VARCHAR | 000003db061128c2de334c008a1d4aaf49f9bbff | fffffee8b080fefc0270ddc0929952fc04beb3df | 1,757,325 | 2,771,204 | 0.38 |

#### **risk_classification_2011_2023.csv(1.53 GB)**

| column_name | column_type | min | max | approx_unique | count | null_percentage |
| --- | --- | --- | --- | --- | --- | --- |
| RCA_AOR | VARCHAR | ATL | WAS | 31 | 3,543,467 | 0 |
| RCA_DCO | VARCHAR | ABQ | YUM | 201 | 3,543,467 | 0 |
| A_NUMBER | VARCHAR | (b)(6)(b)(7)(c) | b(6), b(7)c | 5 | 3,543,467 | 0.3 |
| SUBJ_ID | VARCHAR | (b)(6)(b)(7)(c) | b(6), b(7)c | 5 | 3,543,467 | 0 |
| LAST_NAME | VARCHAR | (b)(6)(b)(7)(c) | b(6), b(7)c | 5 | 3,543,467 | 0 |
| FIRST_NAME | VARCHAR | (b)(6)(b)(7)(c) | b(6), b(7)c | 5 | 3,543,467 | 0 |
| ALERT_CODE | VARCHAR | 1 | Z | 4,774 | 3,543,467 | 0 |
| ACTIVE_INACTIVE | VARCHAR | Active | Inactive | 2 | 3,543,467 | 0 |
| SUBMISSION_DATE | DATE | 2012-07-21 | 2023-10-10 | 4,824 | 3,543,467 | 16.12 |
| STATUS_CODE | VARCHAR | A | I | 6 | 3,543,467 | 26.06 |
| RISK_TO_PUBLIC_SAFETY | VARCHAR | High | Medium | 3 | 3,543,467 | 16.12 |
| RISK_OF_FLIGHT | VARCHAR | High | Medium | 3 | 3,543,467 | 16.12 |
| SPECIAL_VULNERABILITY | VARCHAR | DIS | VSAVC, VSAVC | 203 | 3,543,467 | 17.85 |
| SPECIAL_VULNERABILITY_COMMENTS | VARCHAR |  | b(7)e | 10 | 3,543,467 | 71.7 |
| RCA_CASE_NUMBER | VARCHAR | 10 | b(6), b(7)(c) | 30 | 3,543,467 | 0 |
| CASE_CAT_AT_RCA_DECISION | VARCHAR | 10 | Y | 35 | 3,543,467 | 0 |
| FO_AT_RCA_DECISION | VARCHAR | 1962-06-25 00:00:00 | Y | 11,062 | 3,543,467 | 0 |
| FO_DATE_AT_RCA_DECISION | DATE | 1970-04-08 | 2013-09-30 | 5,098 | 3,543,467 | 96.75 |
| REMOVAL_LIKELY_AT_RCA_DECISION | VARCHAR | N | Y | 2 | 3,543,467 | 35.91 |
| REASON_REMOVAL_UNLIKELY_AT_RCA_DECISION | VARCHAR | Citizenship / Nationality Undetermined | Writ of Habeas Corpus | 567 | 3,543,467 | 8.39 |
| MAN_DET_PER_STAT_ALLEG | VARCHAR | Detain in the Custody of This Service | Y | 15 | 3,543,467 | 3.56 |
| RCA_DECISION_TYPE | VARCHAR | 10000 | Unknown | 49 | 3,543,467 | 0 |
| RCA_RECOMMENDATION | VARCHAR | (b)(6)(b)(7)(c) | b(6), b(7)c | 18 | 3,543,467 | 15.96 |
| RCA_BOND_RECOMMENDATION | VARCHAR | 10000 | Unknown | 42 | 3,543,467 | 0 |
| OFFICER_ID | VARCHAR | (b)(6)(b)(7)(c) | b(6), b(7)c | 6 | 3,543,467 | 1.93 |
| OFFICER_AGREE_DISAGREE | VARCHAR | Agree | Redetermine Detain / Release Decision | 5 | 3,543,467 | 0.15 |
| OFFICER_COMMENTS | VARCHAR |  | b(6), b(7)© | 16 | 3,543,467 | 6.31 |
| SUPERVISOR_ID | VARCHAR | 10000 | b(6), b(7)(c) | 102 | 3,543,467 | 0 |
| SUPERVISOR_AGREE_DISAGREE | VARCHAR | 2012-07-21 00:00:00 | Redetermine Detain / Release Decision | 3,792 | 3,543,467 | 0 |
| SUPERVISOR_COMMENTS | VARCHAR |  | b(6), b(7)© | 25 | 3,543,467 | 0 |
| RCA_FINAL_DECISION | VARCHAR | 1 | Unknown | 12 | 3,543,467 | 0 |
| FINAL_BOND_AMOUNT | BIGINT | -1 | 999999999 | 66 | 3,543,467 | 0 |
| RCA_DECISION_DATE | DATE | 2012-10-01 | 2013-09-30 | 276 | 3,543,467 | 90.96 |
| RCA_SCORING_VER | DOUBLE | 1.2 | 2023.0 | 18 | 3,543,467 | 0.16 |
| SPEC_VULN_VER | VARCHAR | 1 | Unknown | 6 | 3,543,467 | 0 |
| MAN_DET_VER | VARCHAR | 000003db061128c2de334c008a1d4aaf49f9bbff | fffff94807d6807b6ef619353a49d8229afde0d9 | 1,315,848 | 3,543,467 | 0 |
| DISC_INFR_VER | BIGINT | 1 | 1 | 1 | 3,543,467 | 99.99 |
| fiscal_year_code | BIGINT | 2013 | 2013 | 1 | 3,543,467 | 90.96 |
| fiscal_quarter_name | VARCHAR | Q1 | Q4 | 4 | 3,543,467 | 90.96 |
| ANONYMIZED_IDENTIFIER | VARCHAR | 00004afdedfdf6e987b124f6e258522bee6bda0e | ffffeae2afabe4f1749b7933200a76459ceb19ba | 154,138 | 3,543,467 | 90.98 |

## Streaming skup - source i format

Streaming skup - https://www.cbp.gov/document/stats/nationwide-encounters

Encounter data includes:

1.  U.S. Border Patrol (USBP) Title 8 Apprehensions
2. Office of Field Operations (OFO) Title 8 Inadmissibles 
3. Title 42 Expulsions

Data is available for the Northern Land Border, Southwest Land Border, and Nationwide (i.e., air, land, and sea modes of transportation) encounters.

Title 8 Enforcement Actions refers  to apprehensions or inadmissibles processed under CBP’s immigration authority. 

Inadmissibles refers to individuals encountered at ports of entry (POEs) by OFO who are seeking lawful admission into the United States (U.S.) but are determined to be inadmissible, individuals presenting themselves to seek humanitarian protection under our laws, and individuals who withdraw an application for admission and return to their countries of origin within a short timeframe. 

Apprehensions refers to the physical control or temporary detainment of a person by USBP between POEs who is not lawfully in the U.S. which may or may not result in an arrest.

Title 42 Expulsions refers to individuals encountered by USBP and OFO and expelled to the country of last transit or home country in the interest of public health under Title 42 U.S.C. 
265 from March 21, 2020 to May 11, 2023.

Demographics for USBP and OFO include:

- Accompanied Minors (AM)
- Individuals in a Family Unit (FMUA)
- Single Adults
- Unaccompanied Alien Children (UAC) / Single Minors

Skup je grupisan po mesecu i tipu susreta, ali je plan da se od ovoga napravi sinteticki streaming skup tako sto ce se vrednosti po mesecu razdeljivati na odvojene dogadjaje, u neko nasumicno vreme.

#### Nationwide Encounters by Area of Responsibility

| column_name | column_type | min | max | approx_unique | count | null_percentage |
| --- | --- | --- | --- | --- | --- | --- |
| Fiscal Year | BIGINT | 2020 | 2023 | 4 | 53,859 | 0 |
| Month Grouping | VARCHAR | FYTD | FYTD | 1 | 53,859 | 0 |
| Month (abbv) | VARCHAR | APR | SEP | 12 | 53,859 | 0 |
| Component | VARCHAR | Office of Field Operations | U.S. Border Patrol | 2 | 53,859 | 0 |
| Land Border Region | VARCHAR | Northern Land Border | Southwest Land Border | 3 | 53,859 | 0 |
| Area of Responsibility | VARCHAR | Atlanta Field Office | Yuma Sector | 44 | 53,859 | 0 |
| AOR (Abbv) | VARCHAR | Atlanta | YUM | 42 | 53,859 | 0 |
| Demographic | VARCHAR | Accompanied Minors | UC / Single Minors | 4 | 53,859 | 0 |
| Citizenship | VARCHAR | BRAZIL | VENEZUELA | 20 | 53,859 | 0 |
| Title of Authority | VARCHAR | Title 42 | Title 8 | 2 | 53,859 | 0 |
| Encounter Type | VARCHAR | Apprehensions | Inadmissibles | 2 | 53,859 | 0 |
| Encounter Count | BIGINT | 0 | 20211 | 2,738 | 53,859 | 0 |

#### Nationwide Encounters by State

| column_name | column_type | min | max | approx_unique | count | null_percentage |
| --- | --- | --- | --- | --- | --- | --- |
| Fiscal Year | BIGINT | 2020 | 2023 | 4 | 42,532 | 0 |
| Month Grouping | VARCHAR | FYTD | FYTD | 1 | 42,532 | 0 |
| Month (abbv) | VARCHAR | APR | SEP | 12 | 42,532 | 0 |
| Land Border Region | VARCHAR | Northern Land Border | Southwest Land Border | 3 | 42,532 | 0 |
| State | VARCHAR | AK | WI | 55 | 42,532 | 0 |
| Demographic | VARCHAR | Accompanied Minors | UC / Single Minors | 4 | 42,532 | 0 |
| Citizenship | VARCHAR | BRAZIL | VENEZUELA | 20 | 42,532 | 0 |
| Title of Authority | VARCHAR | Title 42 | Title 8 | 2 | 42,532 | 0 |
| Encounter Count | BIGINT | 0 | 36802 | 2,062 | 42,532 | 0 |

## Pitanja

#### Istorijski skup

1. Prosečno trajanje pritvora grupisano po državi deportovanja i godini.
    1. Dužina pritvora u danima se dobija kao  `Stay Book Out Date - Stay Book In Date`
    2. Država deportovanja je `Departure Country` iz tabele
    3. Daje nam uvid u dužinu pritvora po nacionalnosti i kako se menjalo kroz vreme
2. Window funkcija - rangiranje promene rangova zatvorskih ustanova po broju dana koje je svaka osoba provela u njima po godini.
    1. `SUM(length_of_stay)` per facility per year, then `RANK() OVER (PARTITION BY fiscal_year ORDER BY total_person_days DESC)` followed by `LAG()` to get the previous year's rank.
    2. Daje uvid u to koje su ustanove rasle i smanjivale se kroz vreme 
3. Window funkcija - Računanje konzistencije kaucije za različite nacionalnosti i nivoe rizika
    1. Ima oko 15% popunjenih informacija o kauciji u tabeli detentions
    2.  `PERCENTILE_CONT(0.5) OVER (PARTITION BY departure_country,case_threat_level)` on `Bond_Posted_Amount`.
    3. Odnos `Bond_Posted_Amount` i `Initial_Bond_Set_Amount`   da bi se izmerilo koliko se često prvobitna kaucija smanjivala
4. Definisanje razloga puštanja iz pritvora po statusu ulaska u pritvor
    1. Grupisanje `Stay_Release_Reason` po `Entry_Status` (e.g. visa overstay vs. EWI vs. parole)
    2. Daje odgovor na pitanje koji načini primanja u pritvor najčešće rezultuju u deportovanju, i sl.
5. Window funkcija - Učestalost koda optužbe tokom vremena
    1. Prebrojavanje događaja svakog `Charge_Code` po godini, i onda sumiranjem tih count-ova preko `(PARTITION BY charge_code ORDER BY fiscal_year ROWS UNBOUNDED PRECEDING)`
6. Hapšenje - pritvor - deportovanje po godini
    1. Za svaku godinu i način hapšenja, kako se gustina hapšenja, gustina pritvora i gustina deportovanja porede međusobno
7. Window - Vreme od konačne odluke o deportaciji do deportacije 
    1. `Departed_Date - Final_Order_Date`  u danima, grupisano po `Processing_Disposition` i `Case_Category`
    2. `AVG() OVER (PARTITION BY processing_disposition ORDER BY fiscal_year)`
    3. Ovako se vidi trend ubrzanja, usporenja ili stagnacije po tipu dispozicije
8. Konzistentnost klasifikacije rizika, da li nivo rizika utiče na odluke o pritvoru, količine kaucije
    1. Svaka osoba koja je pritvorena dobija dodeljen nivo rizika, koliko je opasna po javnost, i koliko su velike šanse da pobegnu ukoliko ih pustimo, i deli se na nivoe High, Medium i Low
    2. Nakon toga, zaposleni u upravi pravi odluku da li će zadržati osobu u pritvoru, pustiti uz kauciju, ili koristiti neku alternativu kao uslovnu slobodu. Može se složiti sa ocenom rizika ili je prepraviti
    3. Upoređivanje podataka unutar tabele risk_classification
9. Window - Mesečna hapšenja po sezonama
    1. arrests tabela, dobijanje meseci hapšenja pa izvlačenje tromesečnih proseka
    2. Dobija se informacija o tome da ali postoji sezona tj, najčešći period pojačanja rada ICE-a i da li postoji neki šablon tokom godina
    3. `AVG() OVER (ORDER BY year, month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)` 
10. Window funkcija - informacije o polu i godinama u odnosu na dužinu ostajanja u ustanovi
    1. Godine se dobijaju iz Birth Year kolone iz detentions tabele, kao i broj dana u pritvoru
    2. Grupisanje u starosne grupe, (ispod 18, 18–25, 26–40, 41–60, 60+)
    3. Medijana ostajanja u pritvoru po polu x starosnoj grupi po godini 

#### Streaming skup

1. Detekcija naglih porasta broja susreta sa istorijskim kontekstom zadržavanja
    1. Korišćenjem kliznog prozora od 7 dana, prebrojimo sve susrete grupisane po `AOR` i `Citizenship`. 
    2. Join sa batch tabelom pre-agregiranom iz tabele `detentions`, ključevima `Departure_Country` (= `Citizenship`), koja nosi `avg_monthly_detentions`, `avg_stay_days` i `avg_removal_rate_pct`. Izračunati `surge_ratio = broj_u_prozoru / (avg_monthly_detentions / broj nedelja u mesecu)`. 
    3. Batch strana obogaćuje stream odgovorom na pitanje: kada dođe do porasta broja susreta određene nacionalnosti, kakvo je istorijsko opterećenje po pitanju zadržavanja i deportacija koje to obično prati? 
2. Praćenje promene demografskog sastava unutar kliznog prozora
    1. Klizni prozor od 1 sat od susreta, podeljen po AOR
    2. Za svaki prozor izračunati udeo svake vrednosti Demographic kao procenat ukupnog broja susreta u tom prozoru, i onda uporediti sa udelima iz prethodnog prozora
    3. Ovako imamo uvid u promenu sastava susreta tokom dana
3. Podela po Title 8 i Title 42 sa istorijskim stopama deportaicja
    1. Klizni prozor od 1 sat broji susrete grupisane po Title Of Authority i Citizenship po Land Border Region
    2. Join sa tabelom removals, ključem Departure Country koja ima prosečno vreme do deportacije i krivičnu optužbu
4. Detekcija održanog pritiska po nacionalnosti
    1. Window funkcija - Session prozor sa tajmautom od 30 minuta bez aktivnosti, grupisanje po `Citizenship` i `AOR`. Nova sesija se otvara kada stigne prvi susret za tu kombinaciju i 
    zatvara se nakon 30 minuta tišine. Za svaku zatvorenu sesiju izračunati ukupan broj susreta i trajanje sesije. Spojiti sa batch baseline tabelom iz `detentions` — konkretno `p90_monthly_volume` po `Departure_Country`
    2. Ovaj upit hvata održani pritisak (duga sesija sa mnogo događaja) za razliku od S1 koji hvata nagle skokove u fiksnim prozorima. 
    3. Izlaz: početak/kraj sesije, AOR, državljanstvo, broj susreta u sesiji, istorijski dnevni p90, oznaka da li je prekoračen.
5. Obogaćivanje susreta sa profilom zadržavanja u pritvoru
    1. Spajanje AOR tok i State tok unutar tumbling prozora od 1 sat po `Citizenship`, `Demographic`, `Title_of_Authority` i `Land_Border_Region`. AOR tok donosi `Component`, `Encounter_Type` i operativnu geografiju, dok State tok donosi državnu dimenziju koje AOR tok nema. 
    2. Na taj spojeni tok primeniti batch join sa tabelom iz `detentions` ključem `Departure_Country`, koja nosi `avg_stay_days`, `avg_removal_rate_pct` i `avg_threat_level`.
