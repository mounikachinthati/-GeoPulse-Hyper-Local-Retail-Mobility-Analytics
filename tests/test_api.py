
import json
from urllib.request import urlopen
from urllib.parse import urlencode

BASE_URL = "http://127.0.0.1:8000"


def get_api_data(endpoint):
    url = BASE_URL + endpoint

    with urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))
        return response.status, data


# Test 1: Root endpoint
status, data = get_api_data("/")
assert status == 200
assert data["status"] == "Running"
print("Test 1 passed: Root endpoint")


# Test 2: Summary endpoint
status, data = get_api_data("/summary")
assert status == 200
assert data["total_locations"] == 200
assert data["retail_locations"] == 62
assert data["non_retail_locations"] == 138
print("Test 2 passed: Summary endpoint")


# Test 3: Retail-only filter
params = urlencode({"retail_only": "true", "limit": 200})
status, data = get_api_data("/locations?" + params)

assert status == 200
assert data["count"] == 62
assert all(location["is_retail"] for location in data["locations"])
print("Test 3 passed: Retail-only filter")


# Test 4: Category filter
params = urlencode({
    "category": "fashion_and_apparel_store",
    "limit": 200
})
status, data = get_api_data("/locations?" + params)

assert status == 200
assert all(
    location["category"] == "fashion_and_apparel_store"
    for location in data["locations"]
)
print("Test 4 passed: Category filter")


# Test 5: Individual location
status, data = get_api_data("/locations/200")

assert status == 200
assert data["place_name"]
print("Test 5 passed: Individual location lookup")


print("\nAll 5 API tests passed successfully!")
