import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set")

engine = create_engine(DATABASE_URL)

# Load CSV
df = pd.read_csv("healthcare_data.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Clear both tables
with engine.connect() as conn:
    conn.execute(text("TRUNCATE TABLE vitals RESTART IDENTITY CASCADE;"))
    conn.execute(text("TRUNCATE TABLE patients RESTART IDENTITY CASCADE;"))
    conn.commit()

# patients table
patients_df = df[["patient_id", "name", "age", "gender"]].drop_duplicates()

# rename for DB schema (id instead of patient_id)
patients_df = patients_df.rename(columns={"patient_id": "id"})

# Insert into patients
patients_df.to_sql("patients", engine, if_exists="append", index=False)

# vitals table
vitals_df = df[[
    "patient_id", "timestamp",
    "heart_rate", "bp_sys", "bp_dia",
    "oxygen", "temperature"
]]

# Insert into vitals
vitals_df.to_sql("vitals", engine, if_exists="append", index=False)

print("Data loaded successfully into database!")