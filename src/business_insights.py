
import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = BASE_DIR / "data" / "processed" / "guntur_retail_locations.csv"

# Load dataset
df = pd.read_csv(CSV_FILE)

# Filter retail locations
retail_df = df[df["is_retail"] == True].copy()

print("GEOPULSE - BUSINESS INSIGHTS")
print("=" * 40)

print("\n1. Overall Business Overview")
print("Total locations:", len(df))
print("Retail locations:", len(retail_df))
print("Non-retail locations:", len(df) - len(retail_df))

# Top retail categories
print("\n2. Top Retail Categories")
category_counts = retail_df["category"].value_counts()
print(category_counts.head(10).to_string())

# Top retail category
top_category = category_counts.idxmax()
top_count = category_counts.max()

print("\n3. Leading Retail Category")
print("Category:", top_category)
print("Number of locations:", top_count)

# Geographic coverage
print("\n4. Geographic Coverage")
print("Latitude range:",
      df["latitude"].min(), "to", df["latitude"].max())
print("Longitude range:",
      df["longitude"].min(), "to", df["longitude"].max())

# Retail percentage
retail_percentage = len(retail_df) / len(df) * 100

print("\n5. Retail Market Share")
print(f"Retail percentage: {retail_percentage:.2f}%")
print(f"Non-retail percentage: {100-retail_percentage:.2f}%")

print("\nBusiness insights analysis completed!")
