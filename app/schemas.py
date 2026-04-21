from pydantic import BaseModel
from datetime import datetime

class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str

class VitalCreate(BaseModel):
    patient_id: int
    timestamp: datetime
    heart_rate: float
    bp_sys: float
    bp_dia: float
    oxygen: float
    temperature: float