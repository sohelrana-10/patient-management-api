from database import get_connection


def _patient_from_row(row):
    """Convert a database row into a dictionary for the API."""
    if row is None:
        return None

    return {
        "id": row[0],
        "name": row[1],
        "city": row[2],
        "age": row[3],
        "gender": row[4],
        "height": row[5],
        "weight": row[6],
        "bmi": row[7],
        "verdict": row[8],
    }


def get_all_patients():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()

    connection.close()

    return [_patient_from_row(row) for row in rows]


def get_patient(patient_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM patients WHERE id = ?",
        (patient_id,)
    )

    row = cursor.fetchone()
    connection.close()

    return _patient_from_row(row)


def create_patient(patient):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO patients
        (id, name, city, age, gender, height, weight, bmi, verdict)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        patient.id,
        patient.name,
        patient.city,
        patient.age,
        patient.gender,
        patient.height,
        patient.weight,
        patient.bmi,
        patient.verdict
    ))

    connection.commit()
    connection.close()


def delete_patient(patient_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM patients WHERE id = ?",
        (patient_id,)
    )

    deleted = cursor.rowcount > 0

    connection.commit()
    connection.close()

    return deleted


def search_patients_by_city(city):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM patients WHERE city = ?",
        (city,)
    )

    rows = cursor.fetchall()
    connection.close()

    return [_patient_from_row(row) for row in rows]


def sort_patients(sort_by, order):
    allowed_fields = {"height", "weight", "bmi"}

    if sort_by not in allowed_fields:
        raise ValueError("sort_by must be height, weight, or bmi")

    if order not in {"asc", "desc"}:
        raise ValueError("order must be asc or desc")

    direction = "ASC" if order == "asc" else "DESC"

    # sort_by comes only from the allow-list above.
    query = f"SELECT * FROM patients ORDER BY {sort_by} {direction}"

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()

    connection.close()

    return [_patient_from_row(row) for row in rows]