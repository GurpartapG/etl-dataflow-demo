# 📡 Flight Delay ETL Pipeline

This project implements a full **ETL pipeline** for flight delay data, simulating a real‑world data engineering workflow.  
Using raw flight records (departure/arrival times, delays, airlines, airports), the pipeline extracts, transforms, and loads data into a structured database for analysis.

---

## 📌 Project Scope

The pipeline processes large‑scale flight data to enable analysis of airline punctuality, airport efficiency, and operational delays. The steps include:

- Extraction of raw CSV flight records  
- Transformation: datetime parsing, feature engineering (delay categories, day of week, hour of day), data cleansing  
- Load: Insert into a PostgreSQL or SQLite table with optimized schema and indexes  
- Logging and pipeline orchestration  
- (Optional) A visualization/dashboard layer on top of the cleaned data

---

## 🗂️ Dataset

Example dataset: U.S. flights from 2022‑2025 (~25 million rows) — includes scheduled/actual times, delays, cancellations, origin/destination airports. :contentReference[oaicite:2]{index=2}

---

## 🔧 Tech Stack

- Python  
- Pandas  
- SQLite or PostgreSQL  
- Logging (Python `logging` module)  
- Scripts: `extract.py`, `transform.py`, `load.py`, `run_pipeline.py`  
- (Optional) Power BI / Streamlit dashboard layer

---

## 📁 Project Structure

