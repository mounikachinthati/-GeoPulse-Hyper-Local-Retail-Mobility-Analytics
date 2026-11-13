
import json
import pandas as pd
from pathlib import Path

# File paths
raw_folder = Path("data/raw/geo pulse dataset")
output_folder = Path("data/processed")
output_folder.mkdir(parents=True, exist_ok=True)

file_path = next(raw_folder.glob("*place*.geojson"))

# Load original GeoJSON
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# Retail and consumer business categories
retail_categories = {
    "fashion_and_apparel_store",
    "shopping",
    "restaurant",
    "casual_eatery",
    "electronics_store",
    "food_and_beverage_store",
    "warehouse_club_store",
    "sporting_goods_store",
    "flowers_and_gifts_store",
    "books_music_and_video_store",
    "hardware_home_and_garden_store",
    "vehicle_parts_store",
    "pharmacy_and_drug_store",
    "shopping_mall",
    "auto_dealer"
}

records = []

for feature in data["features"]:
    p = feature.get("properties", {})
    geometry = feature.get("geometry") or {}

    coordinates = geometry.get("coordinates") or [None, None]

    address_list = p.get("addresses") or []
    address = address_list[0] if address_list else {}

    taxonomy = p.get("taxonomy") or {}
    names = p.get("names") or {}

    category = p.get("basic_category")

    records.append({
        "place_name": names.get("primary"),
        "category": category or "Unknown",
        "taxonomy_primary": taxonomy.get("primary"),
        "address": address.get("freeform"),
        "city": address.get("locality"),
        "postcode": address.get("postcode"),
        "longitude": coordinates[0],
        "latitude": coordinates[1],
        "phone": (p.get("phones") or [None])[0],
        "email": (p.get("emails") or [None])[0],
        "confidence": p.get("confidence"),
        "is_retail": category in retail_categories
    })

# Convert to DataFrame
df = pd.DataFrame(records)

# Remove exact duplicate rows
df = df.drop_duplicates()

# Save cleaned dataset
output_file = output_folder / "guntur_retail_locations.csv"
df.to_csv(output_file, index=False)

print("DATA CLEANING COMPLETED")
print("-----------------------")
print("Total records:", len(df))
print("Retail records:", df["is_retail"].sum())
print("Other places:", (~df["is_retail"]).sum())
print("Missing categories:", (df["category"] == "Unknown").sum())
print("Duplicate rows remaining:", df.duplicated().sum())
print("\nSaved to:", output_file)
print("\nFirst 5 records:")
print(df.head())
