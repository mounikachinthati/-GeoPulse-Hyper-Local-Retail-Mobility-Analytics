# GeoPulse – Exploratory Data Analysis Report

## 1. Overview
Exploratory Data Analysis (EDA) was performed on the cleaned Guntur retail location dataset using Python.

- Total records: 200
- Total columns: 12
- Retail locations: 62
- Non-retail locations: 138

## 2. Retail Distribution
The dataset contains:
- 62 retail locations
- 138 non-retail locations

Retail classification is based on predefined category rules.

## 3. Top Retail Categories

| Category | Count |
|---|---:|
| Fashion and apparel stores | 17 |
| Shopping | 10 |
| Restaurants | 7 |
| Casual eateries | 5 |
| Electronics stores | 5 |
| Food and beverage stores | 3 |
| Auto dealers | 3 |
| Warehouse club stores | 2 |
| Sporting goods stores | 2 |
| Hardware and home and garden stores | 2 |

## 4. Geographic Analysis
A scatter plot was created using longitude and latitude to visualize the geographic distribution of locations and distinguish retail from non-retail places.

## 5. Visualizations
The following charts were generated and saved in the outputs folder:

1. retail_distribution.png
2. top_retail_categories.png
3. geographic_distribution.png

## 6. Business Insights
1. Fashion and apparel stores form the largest identified retail category.
2. Shopping and restaurant businesses are also significant categories.
3. Geographic coordinates allow spatial distribution analysis.
4. The dataset can support future hyper-local retail planning.

## 7. Limitations
- Retail classification is rule-based.
- Actual customer footfall and sales data are unavailable.
- The dataset covers only a small geographic area of Guntur.

## 8. Tools Used
- Python
- Pandas
- Matplotlib
- Seaborn