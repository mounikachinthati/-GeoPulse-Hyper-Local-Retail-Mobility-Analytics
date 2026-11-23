# GeoPulse Dashboard Report

## Overview
Developed an interactive Streamlit dashboard for GeoPulse Hyper-Local Retail Mobility Analytics.

## Technologies
- Python
- Streamlit
- Plotly
- FastAPI
- Requests

## Dashboard Features
1. Total, retail, and non-retail location KPI cards.
2. Search locations by place name.
3. Filter retail locations.
4. Filter by category.
5. Interactive category visualization.
6. Geographic location map.
7. Location details table.

## API Integration
The dashboard connects to the GeoPulse FastAPI backend at http://127.0.0.1:8000.

Endpoints used:
- /summary
- /locations

## Limitations
The current dataset contains location information. Actual customer footfall and sales data are not available.

## Conclusion
The dashboard provides an interactive interface for exploring and filtering retail locations in Guntur.
