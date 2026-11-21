# GeoPulse – Search and Pagination API Report

## 1. Overview

The GeoPulse FastAPI backend was enhanced with search, filtering, pagination, and input validation features for retail location data in Guntur.

## 2. New API Features

- **Search:** Search locations using part of a place name.
- **Category Filter:** Retrieve locations belonging to a specific category.
- **Retail Filter:** Retrieve only retail locations.
- **Pagination:** Retrieve records in smaller pages using `skip` and `limit`.
- **Validation:** Reject invalid pagination values.

## 3. API Endpoint

`GET /locations`

### Parameters

| Parameter | Description |
|---|---|
| category | Filter by location category |
| retail_only | Show only retail locations |
| search | Search by place name |
| skip | Number of records to skip |
| limit | Maximum number of records to return |

## 4. Testing Results

| Test | Feature | Result |
|---|---|---|
| 1 | Search using India1 | Passed |
| 2 | Retail-only filtering | Passed |
| 3 | Pagination | Passed |
| 4 | Category and retail filtering | Passed |
| 5 | Invalid limit and skip validation | Passed |

## 5. Validation

- Maximum allowed limit: 200.
- Minimum allowed limit: 1.
- Skip cannot be negative.
- Invalid values return HTTP 400.

## 6. Response Structure

The API returns:
- `total_count`: Total matching records before pagination.
- `count`: Number of records in the current response.
- `skip`: Number of skipped records.
- `limit`: Maximum records requested.
- `locations`: Matching location records.

## 7. Conclusion

The GeoPulse API now provides improved search, filtering, pagination, and validation capabilities. All five manual API test groups passed successfully using Swagger UI.