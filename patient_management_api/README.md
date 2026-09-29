# Patient Management API

A small learning project using:

- FastAPI
- SQLite
- Raw SQL
- Pydantic

## 1. Install dependencies

```bash
pip install fastapi uvicorn
```

## 2. Run the API

From this project folder:

```bash
uvicorn main:app --reload
```

## 3. Try these endpoints

Open:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/patients/`
- `http://127.0.0.1:8000/patients/P001`
- `http://127.0.0.1:8000/patients/search?city=Mumbai`
- `http://127.0.0.1:8000/patients/sort?sort_by=bmi&order=desc`

FastAPI's interactive documentation:

- `http://127.0.0.1:8000/docs`

## What to examine

Start with `main.py`, then follow the request flow:

`routes/patients.py`
→ `crud.py`
→ `database.py`
→ `patient_management.db`

Then inspect `schemas.py` to see how Pydantic validates POST data.

`models.py` contains the SQLite table definition and sample data insertion.

## Suggested exercises

1. Add a PUT endpoint to update a patient.
2. Add a search endpoint for `gender`.
3. Add a BMI filter such as `min_bmi`.
4. Add a `doctors` table.
5. Add an `appointments` table and connect patients to doctors.
6. Later replace raw `sqlite3` with SQLAlchemy.
