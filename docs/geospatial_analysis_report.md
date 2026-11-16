# GeoPulse – Geospatial Analysis Report

## 1. Introduction

Geospatial analysis is used to understand the geographic distribution of retail and non-retail locations in Guntur, Andhra Pradesh.

The purpose of this analysis is to visualize business locations on an interactive map and identify the spatial distribution of retail businesses.

## 2. Dataset Overview

- Total mapped locations: 200
- Retail locations: 62
- Non-retail locations: 138
- Missing coordinates: 0
- Data source: Overture Maps Places dataset
- Study area: Selected area of Guntur, Andhra Pradesh

## 3. Geographic Center

The average geographic coordinates of the mapped locations are:

- Center Latitude: 16.291853
- Center Longitude: 80.452242

These coordinates are used to set the initial center of the interactive map.

## 4. Interactive Map

An interactive map was created using Python and Folium.

Map file: `outputs/guntur_retail_map.html`

Map features:
- Red markers represent retail locations.
- Blue markers represent non-retail locations.
- Clicking a marker displays the place name and category.
- OpenStreetMap provides the background map.

## 5. Key Findings

1. A total of 200 locations were successfully mapped.
2. Out of 200 locations, 62 were classified as retail.
3. The remaining 138 locations were classified as non-retail.
4. All 200 records contained valid latitude and longitude values.
5. The map helps visualize the geographic distribution of businesses in the selected study area.

## 6. Business Applications

- Identify areas with existing retail businesses.
- Support location-based retail planning.
- Understand the geographic spread of nearby businesses.
- Help retailers explore potential market opportunities.

## 7. Limitations

- The dataset covers only a selected geographic area of Guntur.
- Retail classification is based on predefined category rules.
- Actual customer footfall and sales data are not available.
- Map markers show business locations, not actual customer movement or traffic density.

## 8. Tools and Technologies

- Python
- Pandas
- Folium
- OpenStreetMap
- VS Code

## 9. Conclusion

The geospatial analysis successfully visualized 200 business locations in the selected area of Guntur. The interactive map provides a useful foundation for further location-based retail analysis and business decision-making.
