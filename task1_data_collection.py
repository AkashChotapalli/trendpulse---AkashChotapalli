import requests
import pandas as pd
import sqlite3
import json
from google.colab import userdata


def fetch_data():
    # 🔑 Get API key from Colab secrets
    API_KEY = userdata.get("newsio")

    url = "https://newsdata.io/api/1/latest"

    params = {
        "apikey": API_KEY,
        "language": "en"
    }

    response = requests.get(url, params=params)
    data = response.json()

    articles = data.get("results", [])

    rows = []

    # 🔥 CLEAN DATA + ADD ENDPOINT
    for article in articles:
        clean = {}

        for k, v in article.items():
            if isinstance(v, (list, dict)):
                clean[k] = json.dumps(v)
            else:
                clean[k] = str(v)

        clean["endpoint"] = "latest"   # ✅ IMPORTANT FIX
        rows.append(clean)

    # -------- CREATE DATAFRAME --------
    df = pd.DataFrame(rows)

    if df.empty:
        print("No data fetched")
        return df

    # -------- SQLITE STORAGE --------
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS news_data")

    columns = ", ".join([f'"{col}" TEXT' for col in df.columns])
    cursor.execute(f'CREATE TABLE news_data ({columns})')

    for _, row in df.iterrows():
        values = [str(v) for v in row]
        placeholders = ",".join(["?"] * len(values))
        cursor.execute(f'INSERT INTO news_data VALUES ({placeholders})', values)

    conn.commit()
    conn.close()

    print("Saved", len(df), "rows successfully")

    return df
