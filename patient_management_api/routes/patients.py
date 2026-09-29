from fastapi import APIRouter, HTTPException, Query

from crud import (
    create_patient,
    delete_patient,
    get_all_patients,
    get_patient,
    search_patients_by_city,
    sort_patients,
)
from schemas import PatientCreate

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


@router.get("/")
def all_patients():
    return get_all_patients()


@router.get("/search")
def search(city: str = Query(..., description="City to search for")):
    return search_patients_by_city(city)


@router.get("/sort")
def sort(
    sort_by: str = Query("bmi", description="height, weight, or bmi"),
    order: str = Query("asc", description="asc or desc")
):
    try:
        return sort_patients(sort_by, order)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.get("/{patient_id}")
def patient(patient_id: str):
    patient_data = get_patient(patient_id)

    if patient_data is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient_data


@router.post("/")
def add_patient(patient: PatientCreate):
    if get_patient(patient.id) is not None:
        raise HTTPException(
            status_code=409,
            detail="Patient ID already exists"
        )

    create_patient(patient)

    return {
        "message": "Patient created successfully",
        "patient": patient
    }


@router.delete("/{patient_id}")
def remove_patient(patient_id: str):
    deleted = delete_patient(patient_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return {"message": "Patient deleted successfully"}
