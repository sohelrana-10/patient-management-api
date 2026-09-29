from database import get_connection


def create_tables():
    """Create database tables if they do not already exist."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            city TEXT,
            age INTEGER,
            gender TEXT,
            height REAL,
            weight REAL,
            bmi REAL,
            verdict TEXT
        )
    """)

    connection.commit()
    connection.close()


def insert_initial_patients():
    """Insert sample patients for learning/demo purposes."""
    patients = [
        ("P001", "Ananya Verma", "Guwahati", 28, "female", 1.65, 90.0, 33.06, "Obese"),
        ("P002", "Ravi Mehta", "Mumbai", 35, "male", 1.75, 85, 27.76, "Overweight"),
        ("P003", "Sneha Kulkarni", "Pune", 22, "female", 1.60, 45, 17.58, "Underweight"),
        ("P004", "Arjun Verma", "Mumbai", 40, "male", 1.80, 90.0, 27.78, "Overweight"),
        ("P005", "Neha Sinha", "Kolkata", 30, "female", 1.55, 75, 31.22, "Obese")
    ]

    connection = get_connection()
    cursor = connection.cursor()

    cursor.executemany("""
        INSERT OR IGNORE INTO patients
        (id, name, city, age, gender, height, weight, bmi, verdict)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, patients)

    connection.commit()
    connection.close()
