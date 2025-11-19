import pandas as pd
import logging

# configure logging for this module
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s"
)

def transform_data(df: pd.DataFrame) -> pd.DataFrame:

    logging.info("Starting data transformation...")
    try:

      # ensure all numeric count cols are integers since these represent count of flights
      count_cols = [
          "arr_flights", "arr_del15", "arr_cancelled", "arr_diverted"
      ]

      # convert type
      for col in count_cols:
        # use Int64 in case there are any missing values
        df[col] = df[col].fillna(0).astype("Int64")


      # avoid division by zero for rate calculation
      flights_nonzero = df["arr_flights"].replace(0, pd.NA)

      # feature engineer the rates
      df["delay_rate"] = df["arr_del15"] / flights_nonzero
      df["cancel_rate"] = df["arr_cancelled"] / flights_nonzero
      df["divert_rate"] = df["arr_diverted"] / flights_nonzero

      # feature engineer new date col
      df["date"] = pd.to_datetime(df[["year", "month"]].assign(day=1))

      # fill missing rate with 0
      for col in ["delay_rate", "cancel_rate", "divert_rate"]:
        df[col] = df[col].fillna(0)

      # delay category based on delay rates
      # 0-5% -> good
      # 5-10% -> moderate
      # 10%+ -> excellent
      df["delay_category"] = pd.cut(
          df["delay_rate"],
          bins = [-0.01, 0.05, 0.10, 1.0],
          labels = ["good", "moderate", "poor"]
      )


      # list of all delay/count/duration columns
      delay_cols = [
      "arr_del15", "arr_cancelled", "arr_diverted",
      "arr_delay", "carrier_ct", "weather_ct", "nas_ct",
      "security_ct", "late_aircraft_ct",
      "carrier_delay", "weather_delay", "nas_delay",
      "security_delay", "late_aircraft_delay"
      ]

      # case a: flights == 0 → set everything to 0
      df.loc[df["arr_flights"] == 0, delay_cols] = 0
      # case B: flights > 0 but delay values are missing → treat as 0
      df[delay_cols] = df[delay_cols].fillna(0)


      logging.info("Transformation completed successfully.")
      return df

    except Exception as e:
      logging.error(f"Transformation failed: {e}")
      raise
