from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models
from app.services.analysis import analyze_vitals
from app.services.risk_engine import calculate_risk

router = APIRouter()

def get_db():
    db = SessionLocal()
    yield db
    db.close()

@router.get("/patients/{patient_id}/analysis")
def get_analysis(patient_id: int, db: Session = Depends(get_db)):
    vitals = db.query(models.Vital).filter(models.Vital.patient_id == patient_id).all()

    vitals_data = [v.__dict__ for v in vitals]
    return analyze_vitals(vitals_data)

@router.get("/patients/{patient_id}/risk")
def get_risk(patient_id: int, db: Session = Depends(get_db)):
    vitals = db.query(models.Vital).filter(models.Vital.patient_id == patient_id).all()

    vitals_data = [v.__dict__ for v in vitals]
    return calculate_risk(vitals_data)