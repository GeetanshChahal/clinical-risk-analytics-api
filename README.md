# 🏥 Clinical Risk Analytics API

A production-style healthcare data system that simulates patient monitoring, processes clinical data, and detects early risk patterns using **Python, Numpy, Pandas, FastAPI and PostgreSQL**.

---

## 🚀 Overview

This project implements an end-to-end **data pipeline + analytics API**:

* Synthetic patient data generation
* Data ingestion into PostgreSQL
* Backend APIs for analytics & risk detection
* Real-world clinical insights from time-series vitals

It mimics how healthcare systems monitor patients and detect early signs of deterioration.

---

## 🧠 Key Features

* 📊 **Synthetic Healthcare Data Generator**
* 🗄️ **Automated Data Ingestion Pipeline**
* ⚡ **FastAPI Backend APIs**
* 📈 **Vitals Trend Analysis (Pandas)**
* 🚨 **Rule-Based Risk Detection Engine**
* 🔁 **Full Database Refresh Pipeline**

---

## 🧪 Data Pipeline

### 1️⃣ Generate Synthetic Data

```bash
python generate_data.py
```

Creates:

```
healthcare_data.csv
```

Includes:

* Patient details (name, age, gender)
* Time-series vitals (heart rate, BP, oxygen, temperature)

---

### 2️⃣ Load Data into Database

```bash
python load_data.py
```

Pipeline actions:

* Deletes existing data from DB
* Splits CSV into normalized tables
* Inserts into:

  * `patients`
  * `vitals`

---

## 🗄️ Database Schema

### 👤 patients

```id="schema1"
id (PK)
name
age
gender
```

### ❤️ vitals

```id="schema2"
id (PK)
patient_id (FK)
timestamp
heart_rate
bp_sys
bp_dia
oxygen
temperature
```

---

## ⚡ API Endpoints

### 👤 Patients

* `GET /patients` → List all patients
* `POST /patients` → Create patient

---

### ❤️ Vitals

* `POST /vitals` → Add patient vitals

---

### 📊 Analytics

* `GET /patients/{id}/analysis`
  → Returns statistical trends

* `GET /patients/{id}/risk`
  → Returns risk score & level

---

## 🧠 Risk Detection Logic

Risk is calculated using rule-based scoring:

| Condition         | Score |
| ----------------- | ----- |
| Heart rate > 110  | +2    |
| Oxygen < 92       | +3    |
| Temperature > 38  | +2    |
| BP systolic > 140 | +1    |

### Output:

* **Low Risk**
* **Medium Risk**
* **High Risk**

---

## 📁 Project Structure

```id="struct01"
project/
│── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── routes/
│   ├── services/
│
│── generate_data.py
│── load_data.py
│── healthcare_data.csv
│── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/clinical-risk-analytics-api.git
cd clinical-risk-analytics-api
```

---

### 2️⃣ Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2 pandas python-dotenv
```

---

### 3️⃣ Configure Environment

Create `.env` file:

```env
DATABASE_URL=postgresql://postgres:password@localhost/healthcare
```

---

### 4️⃣ Run Data Pipeline

```bash
python generate_data.py
python load_data.py
```

---

### 5️⃣ Start API Server

```bash
uvicorn app.main:app --reload
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

## 🔥 What Makes This Project Strong

* Real-world healthcare use case
* End-to-end pipeline (data → DB → API)
* Clean backend architecture
* No unnecessary tools—focused and efficient
* Demonstrates data engineering + analytics + backend

---

## 🚀 Future Improvements

* Add real-time streaming data
* Implement ML-based risk prediction
* Add authentication & role-based access
* Deploy using Docker & cloud

