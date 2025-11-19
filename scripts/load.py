import sqlite3
import pandas as pd
import logging

# configure logging for this module
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s"
)

def load_to_sqlite(df: pd.DataFrame, db_path: str = "db/flights.db", table_name: str = "flight_delays"):
  logging.info("Starting data loading...")
  try:
    # connect to db
    conn = sqlite3.connect(db_path)

    # wipe and recreate using pandas
    df.to_sql(table_name, conn, if_exists="replace", index=False)

    # reapple schema
    with open("config/schema.sql", "r") as f:
      conn.executescript(f.read())

    logging.info("Load completed successfully")
    conn.close()

  except Exception as e:
    logging.error(f"Load failed: {e}")
    raise
