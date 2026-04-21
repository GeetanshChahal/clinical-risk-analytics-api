from fastapi import FastAPI
from app.database import engine, Base
from app.routes import patients, vitals, analytics

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(patients.router)
app.include_router(vitals.router)
app.include_router(analytics.router)