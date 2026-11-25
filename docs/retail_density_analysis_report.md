# GeoPulse - Retail Density Analysis

## 1. Objective
Analyze the geographic concentration of retail locations in Guntur.

## 2. Dataset Summary
- Total mapped locations: 200
- Retail locations: 62
- Occupied geographic grid cells: 17
- Grid configuration: 5 x 5

## 3. Density Classification
- High-density cells: 6
- Medium-density cells: 3
- Low-density cells: 8

## 4. Highest Retail Concentration
|   center_lat |   center_lon |   retail_count | density_level   |
|-------------:|-------------:|---------------:|:----------------|
|      16.2893 |      80.4473 |             10 | High            |
|      16.2936 |      80.448  |              9 | High            |
|      16.2918 |      80.4477 |              6 | High            |
|      16.2926 |      80.4527 |              6 | High            |
|      16.2903 |      80.4468 |              5 | High            |

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
