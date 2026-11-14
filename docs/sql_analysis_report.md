# GeoPulse – SQL Analysis Report

## 1. Overview
SQL analysis was performed on the Guntur retail locations dataset using SQLite and Python.

- Total locations: 200
- Rule-classified retail locations: 62
- Other locations: 138

## 2. Key Findings
- Fashion and apparel stores are the largest retail category (17).
- Shopping locations: 10.
- Restaurants: 7.
- Electronics stores: 5.
- Casual eateries: 5.

## 3. Data Quality
- Missing place names: 0
- Missing categories: 0
- Missing latitudes: 0
- Missing longitudes: 0
- Repeated place-name groups: 3
- Missing postcodes: 2

## 4. Geographic Observations
The most frequent postcodes were:
- 522003: 31 locations
- 522001: 25 locations
- 522006: 2 locations

Two records have postcodes 941735 and 500003. These require further geographic validation.

## 5. Business Insights
1. Fashion and apparel stores represent the largest identified retail category.
2. Shopping and food businesses are important parts of the local retail landscape.
3. The dataset can support further geographic distribution analysis.
4. Repeated business names and unusual postcodes should be investigated.

## 6. Limitations
- Retail classification is rule-based and not ground truth.
- Actual customer footfall and sales data are not available.
- Repeated names do not necessarily represent duplicate businesses.

## 7. Tools Used
- Python
- Pandas
- SQLite
- SQL