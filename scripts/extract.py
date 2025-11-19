import pandas as pd
import logging
from datetime import datetime

# configure logging -> runs when the script is imported
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s"
)


def extract_data(url: str, sample_rows: int = None) -> pd.DataFrame:
    logging.info("Starting data extraction...")
    try:
        df = pd.read_csv(url)

        if sample_rows:
            df = df.head(sample_rows)
            logging.info(f"Dataset sampled to {sample_rows} rows.")

        logging.info(f"Extraction successful. Loaded {len(df)} rows and {len(df.columns)} columns.")
        return df

    except Exception as e:
        logging.error(f"Extraction failed: {e}")
        raise
