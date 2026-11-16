
import pandas as pd
import folium
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = BASE_DIR / "data" / "processed" / "guntur_retail_locations.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load dataset
df = pd.read_csv(CSV_FILE)

# Validate coordinates
df = df.dropna(subset=["latitude", "longitude"])

# Guntur map center based on dataset coordinates
center_lat = df["latitude"].mean()
center_lon = df["longitude"].mean()

geo_map = folium.Map(
    location=[center_lat, center_lon],
    zoom_start=16,
    tiles="OpenStreetMap"
)

# Add location markers
for _, row in df.iterrows():

    if row["is_retail"]:
        color = "red"
        location_type = "Retail"
    else:
        color = "blue"
        location_type = "Non-Retail"

    popup_text = f"""
    <b>Name:</b> {row['place_name']}<br>
    <b>Category:</b> {row['category']}<br>
    <b>Type:</b> {location_type}
    """

    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=5,
        color=color,
        fill=True,
        fill_opacity=0.7,
        popup=folium.Popup(popup_text, max_width=300)
    ).add_to(geo_map)

# Add map legend
legend_html = """
<div style="
position: fixed;
bottom: 30px;
left: 30px;
width: 170px;
background-color: white;
border: 2px solid grey;
z-index: 9999;
padding: 10px;
font-size: 14px;">
<b>GeoPulse Map Legend</b><br>
<span style="color:red;">●</span> Retail<br>
<span style="color:blue;">●</span> Non-Retail
</div>
"""

geo_map.get_root().html.add_child(folium.Element(legend_html))

# Save interactive map
map_file = OUTPUT_DIR / "guntur_retail_map.html"
geo_map.save(map_file)

# Summary
print("GEOPULSE - GEOSPATIAL ANALYSIS")
print("--------------------------------")
print("Total mapped locations:", len(df))
print("Retail locations:", int(df["is_retail"].sum()))
print("Non-retail locations:", int((~df["is_retail"]).sum()))
print("Center latitude:", center_lat)
print("Center longitude:", center_lon)
print("\nInteractive map saved at:", map_file)
