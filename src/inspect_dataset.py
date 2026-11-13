
import json
from pathlib import Path
from collections import Counter

# Locate the retail places GeoJSON file
folder = Path("data/raw/geo pulse dataset")
files = list(folder.glob("*place*.geojson"))

if not files:
    print("Places GeoJSON file not found!")
    raise SystemExit

file_path = files[0]

# Load dataset
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

features = data.get("features", [])

print("DATASET INSPECTION")
print("------------------")
print("File:", file_path.name)
print("Total records:", len(features))

# Inspect columns
if features:
    properties = features[0].get("properties", {})
    print("\nAvailable columns:")
    for column in properties.keys():
        print("-", column)

    # Display first 5 records (properties only)
    print("\nFirst 5 records:")
    for feature in features[:5]:
        print(json.dumps(feature.get("properties", {}), indent=2))

    # Geometry types
    geometry_types = Counter(
        feature.get("geometry", {}).get("type", "Unknown")
        for feature in features
        if feature.get("geometry")
    )
    print("\nGeometry types:", geometry_types)
else:
    print("No records found.")
