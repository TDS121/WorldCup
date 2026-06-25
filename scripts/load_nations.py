import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    ssl_disabled=False
)

cursor = conn.cursor()

# Clear existing data
cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
cursor.execute("TRUNCATE TABLE Nation")
cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
conn.commit()
print("Table cleared")

# Read CSV
df = pd.read_csv("data/raw/nations.csv")

# Insert each row
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO Nation (nation_name, confederation, fifa_ranking, group_letter)
        VALUES (%s, %s, %s, %s)
    """, (row["nation_name"], row["confederation"], row["fifa_ranking"], row["group_letter"]))

conn.commit()

# Verify
cursor.execute("SELECT COUNT(*) FROM Nation")
count = cursor.fetchone()
print(f"Rows in Nation table: {count[0]}")

cursor.close()
conn.close()