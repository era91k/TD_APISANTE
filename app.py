from fastapi import FastAPI, HTTPException
from model_patient import Patient
from pymongo import MongoClient

app = FastAPI()
# 1. Établir une connexion avec MongoDB
client = MongoClient("mongo_sante_c")

# 2. Sélectionner une base de données
db = client.databases

# 3. Sélectionner une collection
patients = db.Patient

@app.get("/patients")
async def read_patients():
    return list(patients.find({}, {'_id': 0}))

@app.post("/patients", status_code=201)
async def create_patient(patient: Patient):
    if patients.find_one({"ssn": patient.ssn}):
        raise HTTPException(status_code=400, detail="SSN already registered")
    db.patients.insert_one(patient.dict())
    return {"message": "Patient added successfully"}

@app.get("/patients/{ssn}")
async def read_patient(ssn: str):
    patient = patients.find_one({"ssn": ssn}, {'_id': 0})
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@app.delete("/patients/{ssn}")
async def delete_patient(ssn: str):
    result = patients.delete_one({"ssn": ssn})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"message": "Patient deleted"}

@app.put("/patients/{ssn}")
async def update_patient(ssn: str, patient: Patient):
    updated_data = {k: v for k, v in patient.dict().items() if v is not None}
    result = patients.update_one({"ssn": ssn}, {"$set": updated_data})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Patient not found or data unchanged")
    return {"message": "Patient updated"}