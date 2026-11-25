
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = BASE_DIR / "data" / "processed" / "guntur_retail_locations.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
REPORT_DIR = BASE_DIR / "docs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

# Load dataset
df = pd.read_csv(CSV_FILE)

# Validate coordinates
df = df.dropna(subset=["latitude", "longitude"]).copy()

# Identify retail locations
retail_df = df[
    df["is_retail"].astype(str).str.lower().isin(["true", "1", "yes"])
].copy()

if retail_df.empty:
    raise ValueError("No retail locations found in the dataset.")

# Divide the geographic area into a 5 x 5 grid
lat_edges = pd.Series(
    pd.cut(retail_df["latitude"], bins=5, retbins=True)[1]
)
lon_edges = pd.Series(
    pd.cut(retail_df["longitude"], bins=5, retbins=True)[1]
)

retail_df["lat_grid"] = pd.cut(
    retail_df["latitude"], bins=lat_edges
)
retail_df["lon_grid"] = pd.cut(
    retail_df["longitude"], bins=lon_edges
)

# Calculate retail counts per grid cell
density = (
    retail_df.groupby(
        ["lat_grid", "lon_grid"], observed=True
    )
    .agg(
        retail_count=("place_name", "count"),
        center_lat=("latitude", "mean"),
        center_lon=("longitude", "mean")
    )
    .reset_index()
)

# Classify density levels among occupied cells
if len(density) >= 2:
    high_threshold = density["retail_count"].quantile(0.75)
    medium_threshold = density["retail_count"].median()

    def classify(count):
        if count >= high_threshold:
            return "High"
        elif count >= medium_threshold:
            return "Medium"
        return "Low"

    density["density_level"] = density["retail_count"].apply(classify)
else:
    density["density_level"] = "High"

# Calculate summary
total_retail = len(retail_df)
occupied_cells = len(density)
high_cells = int((density["density_level"] == "High").sum())
medium_cells = int((density["density_level"] == "Medium").sum())
low_cells = int((density["density_level"] == "Low").sum())

# Save density data
density_file = OUTPUT_DIR / "retail_density_by_grid.csv"
density.to_csv(density_file, index=False)

# Create density visualization
plt.figure(figsize=(10, 7))

scatter = plt.scatter(
    density["center_lon"],
    density["center_lat"],
    s=density["retail_count"] * 100,
    c=density["retail_count"],
    cmap="YlOrRd",
    alpha=0.8,
    edgecolors="black"
)

for _, row in density.iterrows():
    plt.annotate(
        int(row["retail_count"]),
        (row["center_lon"], row["center_lat"]),
        ha="center",
        va="center",
        fontsize=8
    )

plt.colorbar(scatter, label="Retail locations per grid cell")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("GeoPulse - Retail Location Density in Guntur")
plt.grid(alpha=0.3)
plt.tight_layout()

chart_file = OUTPUT_DIR / "retail_density_heatmap.png"
plt.savefig(chart_file, dpi=300)
plt.close()

# Generate report
report = f"""# GeoPulse - Retail Density Analysis

## 1. Objective
Analyze the geographic concentration of retail locations in Guntur.

## 2. Dataset Summary
- Total mapped locations: {len(df)}
- Retail locations: {total_retail}
- Occupied geographic grid cells: {occupied_cells}
- Grid configuration: 5 x 5

## 3. Density Classification
- High-density cells: {high_cells}
- Medium-density cells: {medium_cells}
- Low-density cells: {low_cells}

## 4. Highest Retail Concentration
{density.nlargest(5, 'retail_count')[
    ['center_lat', 'center_lon', 'retail_count', 'density_level']
].to_markdown(index=False)}

## 5. Output Files
- outputs/retail_density_by_grid.csv
- outputs/retail_density_heatmap.png

## 6. Methodology
The geographic coordinate ranges were divided into five latitude
intervals and five longitude intervals. Retail locations were grouped
into these grid cells and counted.

Density levels were assigned using the distribution of counts
among occupied grid cells.

## 7. Limitations
This is a coordinate-grid-based analysis. It does not account for
actual land area, population, customer footfall, or road accessibility.
The density classifications are relative to this dataset.

## 8. Conclusion
The analysis identifies geographic grid cells with higher and lower
concentrations of recorded retail locations.
"""

report_file = REPORT_DIR / "retail_density_analysis_report.md"
report_file.write_text(report, encoding="utf-8")

print("GEOPULSE - RETAIL DENSITY ANALYSIS")
print("=" * 40)
print("Total retail locations:", total_retail)
print("Occupied grid cells:", occupied_cells)
print("High-density cells:", high_cells)
print("Medium-density cells:", medium_cells)
print("Low-density cells:", low_cells)
print("\nTop 5 density cells:")
print(density.nlargest(5, "retail_count")[
    ["center_lat", "center_lon", "retail_count", "density_level"]
].to_string(index=False))

print("\nDensity CSV saved:", density_file)
print("Heatmap saved:", chart_file)
print("Report saved:", report_file)
