# GeoPulse – Data Dictionary

## 1. Dataset Information

- **Project:** GeoPulse – Hyper-Local Retail Mobility Analytics
- **Source:** Overture Maps Places
- **Location:** Guntur, Andhra Pradesh, India
- **Source format:** GeoJSON
- **Processed format:** CSV
- **Total records:** 200
- **Retail records identified:** 62
- **Other places:** 138

## 2. Dataset Columns

| Column | Description | Data Type |
|---|---|---|
| place_name | Name of the business or place | String |
| category | Basic business category | String |
| taxonomy_primary | Detailed primary category | String |
| address | Street or locality address | String |
| city | City name | String |
| postcode | Postal code | String |
| longitude | Geographic longitude | Float |
| latitude | Geographic latitude | Float |
| phone | Contact phone number | String |
| email | Contact email address | String |
| confidence | Source confidence score | Float |
| is_retail | Indicates whether a record matches our selected retail categories | Boolean |

## 3. Data Quality Findings

- Total records: 200
- Missing place names: 0
- Missing categories: 8
- Missing coordinates: 0
- Duplicate rows remaining after cleaning: 0

Records with missing categories were retained and labelled as Unknown.

## 4. Data Processing

1. Loaded the original GeoJSON file using Python.
2. Extracted business names, categories, addresses and coordinates.
3. Selected relevant retail categories using a rule-based classification.
4. Created the is_retail column.
5. Removed exact duplicate rows.
6. Exported the cleaned dataset into CSV format.

## 5. Output File

`data/processed/guntur_retail_locations.csv`

## 6. Important Limitation

The current dataset represents mapped places and business locations. It does not contain actual customer movement, pedestrian footfall or retail transaction data. These will require additional datasets or clearly labelled synthetic data in later project phases.