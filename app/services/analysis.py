import pandas as pd

def analyze_vitals(vitals):
    df = pd.DataFrame(vitals)

    if df.empty:
        return {}

    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values("timestamp")

    result = {
        "avg_heart_rate": df["heart_rate"].mean(),
        "avg_oxygen": df["oxygen"].mean(),
        "trend_heart_rate": df["heart_rate"].iloc[-1] - df["heart_rate"].iloc[0],
    }

    return result