
import streamlit as st
import pandas as pd
import requests
import plotly.express as px

# -------------------------------
# PAGE CONFIGURATION
# -------------------------------

st.set_page_config(
    page_title="GeoPulse Dashboard",
    page_icon="📍",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000"

st.title("📍 GeoPulse – Retail Mobility Analytics")
st.subheader("Hyper-Local Retail Analytics | Guntur, Andhra Pradesh")

st.markdown("---")


# -------------------------------
# FETCH API DATA
# -------------------------------

@st.cache_data(ttl=30)
def get_summary():
    response = requests.get(f"{API_URL}/summary", timeout=10)
    response.raise_for_status()
    return response.json()


@st.cache_data(ttl=30)
def get_locations(params):
    response = requests.get(
        f"{API_URL}/locations",
        params=params,
        timeout=15
    )
    response.raise_for_status()
    return response.json()


try:
    summary = get_summary()

except requests.RequestException as error:
    st.error(f"Cannot connect to GeoPulse API: {error}")
    st.info(
        "Start the backend using: "
        "python -m uvicorn backend.main:app --reload"
    )
    st.stop()


# -------------------------------
# KPI CARDS
# -------------------------------

st.header("📊 Business Overview")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Locations",
    summary["total_locations"]
)

col2.metric(
    "Retail Locations",
    summary["retail_locations"]
)

col3.metric(
    "Non-Retail Locations",
    summary["non_retail_locations"]
)

st.markdown("---")


# -------------------------------
# FILTERS
# -------------------------------

st.header("🔍 Search and Filter Locations")

filter_col1, filter_col2, filter_col3 = st.columns(3)

with filter_col1:
    search = st.text_input(
        "Search Place Name",
        placeholder="Enter a place name"
    )

with filter_col2:
    retail_only = st.checkbox("Show Retail Locations Only")

with filter_col3:
    category = st.text_input(
        "Category Filter",
        placeholder="Example: restaurant"
    )

params = {
    "skip": 0,
    "limit": 200,
    "retail_only": retail_only
}

if search.strip():
    params["search"] = search.strip()

if category.strip():
    params["category"] = category.strip()


# -------------------------------
# FETCH FILTERED LOCATIONS
# -------------------------------

try:
    result = get_locations(params)
    locations = result["locations"]
    df = pd.DataFrame(locations)

except (requests.RequestException, KeyError, ValueError) as error:
    st.error(f"Unable to retrieve location data: {error}")
    st.stop()


st.write(f"**Matching Locations:** {result['total_count']}")

if df.empty:
    st.warning("No matching locations found.")

else:

    # -------------------------------
    # CATEGORY CHART
    # -------------------------------

    st.markdown("---")
    st.header("📈 Retail Category Analysis")

    if "category" in df.columns:
        category_data = (
            df["category"]
            .fillna("Unknown")
            .value_counts()
            .reset_index()
        )

        category_data.columns = ["Category", "Count"]

        fig = px.bar(
            category_data.head(10),
            x="Category",
            y="Count",
            title="Top 10 Categories",
            color="Count",
            text="Count"
        )

        fig.update_layout(
            xaxis_tickangle=-45,
            height=450
        )

        st.plotly_chart(fig, use_container_width=True)

    
    # -------------------------------
    # LOCATION MAP
    # -------------------------------

    st.markdown("---")
    st.header("🗺️ Guntur Location Map")

    map_df = df.dropna(
        subset=["latitude", "longitude"]
    ).copy()

    if not map_df.empty:

        map_df["Location Type"] = map_df["is_retail"].map({
            1: "Retail",
            0: "Non-Retail",
            True: "Retail",
            False: "Non-Retail"
        })

        fig_map = px.scatter_map(
            map_df,
            lat="latitude",
            lon="longitude",
            color="Location Type",
            hover_name="place_name",
            hover_data=["category", "address"],
            zoom=13,
            height=550,
            map_style="open-street-map",
            title="Retail and Non-Retail Locations in Guntur"
        )

        st.plotly_chart(
            fig_map,
            use_container_width=True
        )

    else:
        st.warning("No coordinates available for the map.")


    # -------------------------------
    # LOCATION TABLE
    # -------------------------------

    st.markdown("---")
    st.header("📋 Location Details")

    display_columns = [
        "place_name",
        "category",
        "address",
        "latitude",
        "longitude",
        "is_retail"
    ]

    available_columns = [
        column for column in display_columns
        if column in df.columns
    ]

    st.dataframe(
        df[available_columns],
        use_container_width=True,
        hide_index=True
    )


st.markdown("---")
st.caption("GeoPulse | Hyper-Local Retail Mobility Analytics | Guntur")

