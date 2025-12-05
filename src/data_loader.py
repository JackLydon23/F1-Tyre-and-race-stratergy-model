import pandas as pd

def load_stint(path):
    df = pd.read_csv(path)
    required = ["lap", "lap_time", "tyre_temp"]
    if not all(col in df.columns for col in required):
        raise ValueError("Missing required telemetry columns")
    return df
