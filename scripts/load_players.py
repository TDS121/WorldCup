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
cursor.execute("TRUNCATE TABLE Player")
cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
conn.commit()
print("Player table cleared")

# Read CSV and handle missing values
df = pd.read_csv("data/cleaned/players.csv")
df["last_name"] = df["last_name"].fillna("")
df = df.where(pd.notnull(df), None)

# Insert each row
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO Player (nation_id, first_name, last_name, position, kit_number, date_of_birth)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        int(row["nation_id"]) if row["nation_id"] is not None else None,
        row["first_name"],
        row["last_name"],
        row["position"],
        int(row["kit_number"]) if row["kit_number"] is not None else None,
        row["date_of_birth"]
    ))

conn.commit()

# Verify
cursor.execute("SELECT COUNT(*) FROM Player")
count = cursor.fetchone()
print(f"Rows in Player table: {count[0]}")

cursor.close()
conn.close()