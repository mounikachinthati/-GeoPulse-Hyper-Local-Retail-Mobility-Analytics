
import json
from pathlib import Path
from collections import Counter

folder = Path("data/raw/geo pulse dataset")
file_path = next(folder.glob("*place*.geojson"))

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

features = data["features"]

categories = Counter()
missing_names = 0
missing_categories = 0
missing_coordinates = 0

for feature in features:
    properties = feature.get("properties", {})
    geometry = feature.get("geometry") or {}

    category = properties.get("basic_category")
    name = (properties.get("names") or {}).get("primary")

    if category:
        categories[category] += 1
    else:
        missing_categories += 1

    if not name:
        missing_names += 1

    if not geometry.get("coordinates"):
        missing_coordinates += 1

print("GEOPULSE DATA QUALITY REPORT")
print("----------------------------")

print("\nTotal records:", len(features))

print("\nBusiness category counts:")
for category, count in categories.most_common():
    print(category, ":", count)

print("\nMissing values:")
print("Names:", missing_names)
print("Categories:", missing_categories)
print("Coordinates:", missing_coordinates)

print("\nTop 5 business records:")
for feature in features[:5]:
    p = feature.get("properties", {})
    print(
        (p.get("names") or {}).get("primary"),
        "|",
        p.get("basic_category")
    )
