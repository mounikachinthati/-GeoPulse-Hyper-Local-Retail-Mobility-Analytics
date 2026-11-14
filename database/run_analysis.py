import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_FILE = BASE_DIR / "database" / "geopulse.db"
SQL_FILE = BASE_DIR / "database" / "analysis_queries.sql"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

with open(SQL_FILE, "r", encoding="utf-8") as file:
    sql_content = file.read()

queries = [q.strip() for q in sql_content.split(";") if q.strip()]

for i, query in enumerate(queries, start=1):
    print(f"\n--- Query {i} Results ---")
    cursor.execute(query)

    if cursor.description:
        print([column[0] for column in cursor.description])
        for row in cursor.fetchall():
            print(row)

conn.close()
print("\nSQL analysis completed successfully!")
