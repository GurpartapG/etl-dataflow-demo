# 📡 Flight Delay ETL Pipeline  
*A modular, production-style ETL workflow for airline delay analytics*

This project implements a complete **Extract–Transform–Load (ETL) pipeline** to process U.S. flight delay data.  
It simulates a *real-world data engineering system* — starting from raw CSV ingestion, applying feature engineering and cleansing, loading into a relational database, and running SQL-based analysis.

The pipeline is fully modular, logged, reproducible, and ready for extension (dashboard, API, orchestration tools, etc.).

---

## 🧭 Overview

The goal of this project is to build a **clean, maintainable ETL pipeline** that supports analytical questions such as:

- Which airlines have the highest or lowest delays?  
- Which airports perform best and worst?  
- What delay patterns exist across months or years?  
- How much do weather, security, NAS, and airline operations contribute to delays?  
- Which *airline + airport combinations* have the worst passenger experience?

The implementation demonstrates practical data engineering principles:

✔ Modular scripts (extract → transform → load → orchestrate)  
✔ Logging and error handling  
✔ SQL schema design + indexing  
✔ SQL analytics on processed data  
✔ Reproducible end-to-end execution  

---

## 🗂️ Dataset

**Airline_Delay_Cause.csv** 

Monthly statistics per airline & airport, including:

- arrival delays  
- number of delayed, cancelled, diverted flights  
- delay minutes by category:  
  - carrier  
  - weather  
  - NAS  
  - security  
  - late aircraft  
- airport & carrier identifiers  
- date information (year, month)

- **Original source (filtered from Jan'25 - Jul'25)**  
  👉 https://www.transtats.bts.gov/ot_delay/OT_DelayCause1.asp?20=E 
- raw data is stored in:
  `data/raw/`
- Cleaned and engineered output saved to:
  `data/processed/flights_cleaned.csv`
  
---

## 🧱 Architecture

```
             data/raw/*.csv
                    │
        ┌───────────┴───────────┐
        │   PHASE 2 — Extract   │
        └────────────────────────┘
                    │
        ┌───────────┴───────────┐
        │  PHASE 3 — Transform   │
        │  • feature engineering │
        │  • delay rates         │
        │  • cleaning/imputation │
        └────────────────────────┘
                    │
        ┌───────────┴───────────┐
        │     PHASE 4 — Load     │
        │ SQLite DB + indexes    │
        └────────────────────────┘
                    │
        ┌───────────┴───────────┐
        │ PHASE 5 — Orchestration│
        │ run_pipeline.py        │
        └────────────────────────┘
                    │
        ┌───────────┴───────────┐
        │   PHASE 6 — Analysis   │
        │ SQL insights/queries   │
        └────────────────────────┘

```

---

## 📁 Repository Structure

```
flight-delay-etl/
├── config/
│ └── schema.sql
│
├── data/
│ ├── raw/
│ │ ├── Airline_Delay_Cause.csv
│ │ └── Download_Column_Definitions.xlsx
│ └── processed/
│ └── flights_cleaned.csv
│
├── db/
│ └── flights.db
│
├── logs/
│ └── pipeline.log
│
├── notebooks/
│ └── flight_delay_pipeline.ipynb
│
├── scripts/
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ ├── run_pipeline.py
│ └── __init__.py
│
├── sql_queries/
│ └── queries.sql
│
├── README.md

```
---

## 🔧 Tech Stack

- Python  
- Pandas  
- SQLite 
- SQL
- Python Logging

---

## ⚙️ Pipeline Components

### **PHASE 2 — Extract**  
`scripts/extract.py`

- Loads raw CSV from URL or local path  
- Optional sampling  
- Logs row counts  
- Returns raw DataFrame

### **PHASE 3 — Transform**  
`scripts/transform.py`

- Converting `year+month` → proper `datetime`
- Calculating delay rates
- Imputing missing counts
- Normalizing numeric types
- Creating delay_category (good / moderate / poor)
- Filling invalid values
- Saves cleaned CSV

### **PHASE 4 — Load**  
`scripts/load.py`

Schema defined in `config/schema.sql`

Created SQLite DB: `flights.db`

Inlcudes:
- 26+ fields
- Strong typing for counts & delay metrics
- Indexes:
  - (carrier, year, month)
  - (airport, date)

### **PHASE 5 — Orchestration**  
`scripts/run_pipeline.py`

Runs the complete workflow:
1. Extract
2. Transform
3. Load
4. Log end-to-end success or failure

### **PHASE 6 — SQL Analysis**
`sql_queries/queries.sql` includes:

- Top 10 airlines by avg delay minutes
- Worst airports by highest delay %
- Best airports by lowest delay %
- Most reliable airlines
- Delay trend by month
- Delay cause breakdown
- Worst airline–airport combinations

---

## ✨ Key Skills

- Building scalable ingestion and cleaning pipelines
- Cleaning and preparing real-world datasets
- Feature engineering on datetime and categorical variables  
- Designing SQL schema and using indexes  
- Structuring Python code for modular ETL tasks  
- Logging & reproducibility
- Analytical SQL for insights

---

## 🔮 Next Steps

- Add Power BI / Streamlit dashboard
- Introduce Airflow or Prefect orchestration
- Build REST API with FastAPI
- Add pytest unit tests
- Parameterize pipeline with config files
