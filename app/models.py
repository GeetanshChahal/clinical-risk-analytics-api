from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from app.database import Base

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)

class Vital(Base):
    __tablename__ = "vitals"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    timestamp = Column(DateTime)
    heart_rate = Column(Float)
    bp_sys = Column(Float)
    bp_dia = Column(Float)
    oxygen = Column(Float)
    temperature = Column(Float)