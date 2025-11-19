
from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_to_sqlite
import logging
from datetime import datetime

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s"
)

def run_pipeline():
  logging.info("====== STARTING PIPELINE RUN ======")

  try:

    #extract
    FILE_URL = "https://raw.githubusercontent.com/GurpartapG/etl-dataflow-demo/main/data/raw/Airline_Delay_Cause.csv"
    df_raw = extract_data(FILE_URL)
    logging.info(f"Extract step completed. Rows: {len(df_raw)}")

    # transform
    df_transformed = transform_data(df_raw)
    logging.info(f"Transform step completed. Rows: {len(df_transformed)}")

    # load
    load_to_sqlite(df_transformed)
    logging.info(f"Load step completed")

    logging.info("====== PIPELINE COMPLETED SUCCESSFULLY ======")

  except Exception as e:
    logging.error(f"Pipeline run failed: {e}")
    raise

if __name__ == "__main__":
  run_pipeline()
