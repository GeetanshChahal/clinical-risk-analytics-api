from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    yield db
    db.close()

@router.post("/vitals")
def add_vital(vital: schemas.VitalCreate, db: Session = Depends(get_db)):
    db_vital = models.Vital(**vital.model_dump())
    db.add(db_vital)
    db.commit()
    return db_vital