import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def safe_int(val):
    try:
        if val is None or (isinstance(val, float) and pd.isna(val)):
            return None
        return int(val)
    except:
        return None

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
cursor.execute("TRUNCATE TABLE Game")
cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
conn.commit()
print("Game table cleared")

# Read CSV
df = pd.read_csv("data/raw/games.csv")

# Insert each row
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO Game (stadium_id, home_id, away_id, game_date, tournament_stage, home_score, away_score, attendance)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        safe_int(row["stadium_id"]),
        safe_int(row["home_id"]),
        safe_int(row["away_id"]),
        row["game_date"],
        row["tournament_stage"],
        safe_int(row["home_score"]),
        safe_int(row["away_score"]),
        safe_int(row["attendance"]),
    ))

conn.commit()

# Verify
cursor.execute("SELECT COUNT(*) FROM Game")
count = cursor.fetchone()
print(f"Rows in Game table: {count[0]}")

cursor.close()
conn.close()