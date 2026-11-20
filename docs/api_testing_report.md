
# GeoPulse API Testing Report

## 1. Overview
This report documents the testing of the GeoPulse FastAPI backend.

## 2. Testing Method
Automated API tests were executed using Python's urllib library.

## 3. Test Results

| Test Case | Endpoint | Result |
|---|---|---|
| Root endpoint | GET / | Passed |
| Summary | GET /summary | Passed |
| Retail-only filter | GET /locations | Passed |
| Category filter | GET /locations | Passed |
| Individual location | GET /locations/200 | Passed |

## 4. Validation
- Verified successful HTTP responses.
- Checked total, retail and non-retail counts.
- Verified retail-only filtering.
- Verified category filtering.
- Checked individual location retrieval.

## 5. Conclusion
All five automated API tests passed successfully. The GeoPulse backend is functioning correctly for the tested endpoints and filters.
