
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = BASE_DIR / "data" / "processed" / "guntur_retail_locations.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load dataset
df = pd.read_csv(CSV_FILE)

sns.set_theme(style="whitegrid")

print("GEOPULSE - EXPLORATORY DATA ANALYSIS")
print("------------------------------------")

print("\nDataset shape:", df.shape)

print("\nRetail distribution:")
print(df["is_retail"].value_counts())

# 1. Retail vs Non-Retail
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="is_retail")
plt.title("Retail vs Non-Retail Locations")
plt.xlabel("Is Retail (0 = No, 1 = Yes)")
plt.ylabel("Number of Locations")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "retail_distribution.png")
plt.close()

# 2. Top 10 Retail Categories
retail_df = df[df["is_retail"] == 1]

category_counts = (
    retail_df["category"]
    .value_counts()
    .head(10)
    .reset_index()
)
category_counts.columns = ["category", "count"]

plt.figure(figsize=(10, 6))
sns.barplot(
    data=category_counts,
    x="count",
    y="category",
    color="steelblue"
)
plt.title("Top 10 Retail Categories in Guntur")
plt.xlabel("Number of Locations")
plt.ylabel("Retail Category")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "top_retail_categories.png")
plt.close()

# 3. Geographic Distribution
plt.figure(figsize=(9, 6))
sns.scatterplot(
    data=df,
    x="longitude",
    y="latitude",
    hue="is_retail",
    palette={0: "gray", 1: "red"},
    alpha=0.8
)
plt.title("Geographic Distribution of Retail Locations")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(title="Is Retail")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "geographic_distribution.png")
plt.close()

# Summary
print("\nTop 10 Retail Categories:")
print(category_counts.to_string(index=False))

print("\nEDA charts saved successfully in outputs folder!")
