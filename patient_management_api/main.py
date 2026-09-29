from fastapi import FastAPI

from models import create_tables, insert_initial_patients
from routes.patients import router

app = FastAPI(
    title="Patient Management API",
    description="A small FastAPI + SQLite learning project"
)

# Create the database table and insert sample data when the app starts.
create_tables()
insert_initial_patients()

# Register patient API routes.
app.include_router(router)


@app.get("/")
def home():
    return {"message": "Patient Management API is running"}
