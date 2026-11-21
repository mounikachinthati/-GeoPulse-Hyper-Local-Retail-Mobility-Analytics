
from fastapi import FastAPI, HTTPException
from pathlib import Path
import sqlite3

app = FastAPI(
    title="GeoPulse API",
    description="Hyper-Local Retail Mobility Analytics API for Guntur",
    version="1.1.0"
)

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "geopulse.db"


# Database connection
def get_connection():
    if not DB_PATH.exists():
        raise FileNotFoundError(f"Database not found: {DB_PATH}")

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to GeoPulse API",
        "project": "Hyper-Local Retail Mobility Analytics",
        "location": "Guntur",
        "status": "Running"
    }


# Summary endpoint
@app.get("/summary")
def get_summary():
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                COUNT(*) AS total_locations,
                SUM(
                    CASE WHEN is_retail = 1 THEN 1 ELSE 0 END
                ) AS retail_locations,
                SUM(
                    CASE WHEN is_retail = 0 THEN 1 ELSE 0 END
                ) AS non_retail_locations
            FROM retail_locations
        """)

        result = dict(cursor.fetchone())
        return result

    except sqlite3.Error as error:
        raise HTTPException(status_code=500, detail=str(error))

    except FileNotFoundError as error:
        raise HTTPException(status_code=500, detail=str(error))

    finally:
        if connection:
            connection.close()


# Search, filter and pagination endpoint
@app.get("/locations")
def get_locations(
    category: str = None,
    retail_only: bool = False,
    search: str = None,
    skip: int = 0,
    limit: int = 100
):
    if limit < 1 or limit > 200:
        raise HTTPException(
            status_code=400,
            detail="Limit must be between 1 and 200"
        )

    if skip < 0:
        raise HTTPException(
            status_code=400,
            detail="Skip cannot be negative"
        )

    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            SELECT rowid AS id, *
            FROM retail_locations
            WHERE 1=1
        """

        count_query = """
            SELECT COUNT(*)
            FROM retail_locations
            WHERE 1=1
        """

        conditions = []
        parameters = []

        # Category filter
        if category:
            conditions.append("category = ?")
            parameters.append(category)

        # Retail-only filter
        if retail_only:
            conditions.append("is_retail = 1")

        # Search by place name
        if search:
            conditions.append("place_name LIKE ?")
            parameters.append(f"%{search}%")

        # Apply filters
        if conditions:
            where_clause = " AND " + " AND ".join(conditions)
            query += where_clause
            count_query += where_clause

        # Total matching records
        cursor.execute(count_query, parameters)
        total_count = cursor.fetchone()[0]

        # Pagination
        query += " ORDER BY place_name LIMIT ? OFFSET ?"

        parameters.extend([limit, skip])

        cursor.execute(query, parameters)

        locations = [
            dict(row) for row in cursor.fetchall()
        ]

        return {
            "total_count": total_count,
            "count": len(locations),
            "skip": skip,
            "limit": limit,
            "locations": locations
        }

    except sqlite3.Error as error:
        raise HTTPException(status_code=500, detail=str(error))

    except FileNotFoundError as error:
        raise HTTPException(status_code=500, detail=str(error))

    finally:
        if connection:
            connection.close()


# Individual location lookup
@app.get("/locations/{location_id}")
def get_location(location_id: int):
    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT rowid AS id, *
            FROM retail_locations
            WHERE rowid = ?
            """,
            (location_id,)
        )

        location = cursor.fetchone()

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

    finally:
        if connection:
            connection.close()
