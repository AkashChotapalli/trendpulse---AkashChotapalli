"""
Task 2: Data Processing
Clean data safely
"""

import pandas as pd
import sqlite3
import os
from task1_data_collection import fetch_data


def process_data():
    import sqlite3
    import pandas as pd
    import os
    from task1_data_collection import fetch_data

    # 🔥 Step 1: Check DB exists
    if not os.path.exists("news.db"):
        print("DB not found → fetching data...")
        fetch_data()

    conn = sqlite3.connect("news.db")

    # 🔥 Step 2: Check table exists
    try:
        df = pd.read_sql("SELECT * FROM news_data", conn)
    except:
        print("Table not found → fetching data...")
        conn.close()
        fetch_data()
        conn = sqlite3.connect("news.db")
        df = pd.read_sql("SELECT * FROM news_data", conn)

    conn.close()

    # 🔥 Step 3: If empty → fetch again
    if df.empty:
        print("DB empty → refetching...")
        fetch_data()
        conn = sqlite3.connect("news.db")
        df = pd.read_sql("SELECT * FROM news_data", conn)
        conn.close()

    print("Before cleaning:", len(df))

    # ✅ Clean safely
    if "pubDate" in df.columns:
        df["date"] = pd.to_datetime(df["pubDate"], errors="coerce")

    if "title" in df.columns:
        df = df[df["title"].notna()]
        df = df.drop_duplicates(subset=["title"])

    print("After cleaning:", len(df))

    return df
