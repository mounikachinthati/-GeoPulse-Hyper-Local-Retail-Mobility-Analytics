
from fastapi import FastAPI, HTTPException
from pathlib import Path
import sqlite3

app = FastAPI(
    title="GeoPulse API",
    description="Hyper-Local Retail Mobility Analytics API for Guntur",
    version="1.0.0"
)

# Locate the SQLite database
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "geopulse.db"


def get_connection():
    if not DB_PATH.exists():
        raise FileNotFoundError(f"Database not found: {DB_PATH}")

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


@app.get("/")
def home():
    return {
        "message": "Welcome to GeoPulse API",
        "project": "Hyper-Local Retail Mobility Analytics",
        "location": "Guntur",
        "status": "Running"
    }


@app.get("/summary")
def get_summary():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                COUNT(*) AS total_locations,
                SUM(CASE WHEN is_retail = 1 THEN 1 ELSE 0 END) AS retail_locations,
                SUM(CASE WHEN is_retail = 0 THEN 1 ELSE 0 END) AS non_retail_locations
            FROM retail_locations
        """)

        result = dict(cursor.fetchone())
        connection.close()

        return result

    except sqlite3.Error as error:
        raise HTTPException(status_code=500, detail=str(error))
    except FileNotFoundError as error:
        raise HTTPException(status_code=500, detail=str(error))


@app.get("/locations")
def get_locations(
    category: str = None,
    retail_only: bool = False,
    limit: int = 100
):
    if limit < 1 or limit > 200:
        raise HTTPException(
            status_code=400,
            detail="Limit must be between 1 and 200"
        )

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = "SELECT rowid AS id, * FROM retail_locations WHERE 1=1"
        parameters = []

        if category:
            query += " AND category = ?"
            parameters.append(category)

        if retail_only:
            query += " AND is_retail = 1"

        query += " ORDER BY place_name LIMIT ?"
        parameters.append(limit)

        cursor.execute(query, parameters)
        locations = [dict(row) for row in cursor.fetchall()]

        connection.close()

        return {
            "count": len(locations),
            "locations": locations
        }

    except sqlite3.Error as error:
        raise HTTPException(status_code=500, detail=str(error))
    except FileNotFoundError as error:
        raise HTTPException(status_code=500, detail=str(error))


@app.get("/locations/{location_id}")
def get_location(location_id: int):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT rowid AS id, * FROM retail_locations WHERE rowid = ?",
            (location_id,)
        )

        location = cursor.fetchone()
        connection.close()

        if location is None:
            raise HTTPException(
                status_code=404,
                detail="Location not found"
            )

        return dict(location)

    except sqlite3.Error as error:
        raise HTTPException(status_code=500, detail=str(error))
    except FileNotFoundError as error:
        raise HTTPException(status_code=500, detail=str(error))
