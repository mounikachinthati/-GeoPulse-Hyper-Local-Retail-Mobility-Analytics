# GeoPulse Backend API Report

## 1. Overview
GeoPulse uses FastAPI to provide API access to the Guntur retail locations database.

## 2. Technology Used
- Python
- FastAPI
- Uvicorn
- SQLite

## 3. API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | API welcome message |
| GET | /summary | Total, retail and non-retail counts |
| GET | /locations | Retrieve and filter locations |
| GET | /locations/{location_id} | Retrieve a location by ID |

## 4. Filtering Options
- category: Filter locations by category.
- retail_only: Show only retail locations.
- limit: Control the number of returned records.

## 5. Database
The API connects to the SQLite database:
database/geopulse.db

## 6. Testing
API endpoints were tested using FastAPI Swagger UI.

## 7. Conclusion
The backend API provides structured access to GeoPulse retail location data and supports filtering and individual location lookup.