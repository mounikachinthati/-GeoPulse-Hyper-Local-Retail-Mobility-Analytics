
import sqlite3
import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = BASE_DIR / "data" / "processed" / "guntur_retail_locations.csv"
DB_FILE = BASE_DIR / "database" / "geopulse.db"

# Load cleaned dataset
df = pd.read_csv(CSV_FILE)

# Create SQLite database
conn = sqlite3.connect(DB_FILE)

# Load all location records into SQLite
df.to_sql("retail_locations", conn, if_exists="replace", index=False)

# Verify records
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM retail_locations")
total_records = cursor.fetchone()[0]

cursor.execute("""
    SELECT COUNT(*)
    FROM retail_locations
    WHERE is_retail = 1
""")
retail_records = cursor.fetchone()[0]

print("GeoPulse database created successfully!")
print("Database:", DB_FILE)
print("Total location records:", total_records)
print("Retail records:", retail_records)

conn.close()
