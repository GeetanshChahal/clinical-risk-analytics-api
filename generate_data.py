import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

num_patients = 50
records_per_patient = 100

data = []

for patient_id in range(1, num_patients + 1):
    base_time = datetime.now() - timedelta(days=10)

    for i in range(records_per_patient):
        timestamp = base_time + timedelta(minutes=30 * i)

        heart_rate = np.random.normal(75, 10)
        oxygen = np.random.normal(97, 2)
        temp = np.random.normal(37, 0.5)
        bp_sys = np.random.normal(120, 15)
        bp_dia = np.random.normal(80, 10)

        # Inject anomalies
        if random.random() < 0.05:
            heart_rate += random.randint(30, 60)
            oxygen -= random.randint(5, 10)

        data.append([
            patient_id,
            timestamp,
            round(heart_rate, 2),
            round(bp_sys, 2),
            round(bp_dia, 2),
            round(oxygen, 2),
            round(temp, 2)
        ])

df = pd.DataFrame(data, columns=[
    "patient_id", "timestamp", "heart_rate",
    "bp_sys", "bp_dia", "oxygen", "temperature"
])

df.to_csv("vitals.csv", index=False)
print("Dataset generated!")