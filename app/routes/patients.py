from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/patients")
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    next_id = (db.query(func.coalesce(func.max(models.Patient.id), 0)).scalar() or 0) + 1
    db_patient = models.Patient(id=next_id, **patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@router.get("/patients")
def list_patients(db: Session = Depends(get_db)):
    return db.query(models.Patient).all()