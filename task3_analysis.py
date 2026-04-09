import pandas as pd
import numpy as np
import os

# ---------------- LOAD DATA ----------------

file_path = "data/trends_clean.csv"

# Case 1 — GitHub submission file
if os.path.exists(file_path):
    pass

# Fallback for Colab testing
if not os.path.exists(file_path):
    if os.path.exists("data"):
        csv_files = [f for f in os.listdir("data") if f.endswith(".csv")]
        if csv_files:
            file_path = "data/" + csv_files[0]
        else:
            raise FileNotFoundError("No CSV file found in data/")
    else:
        raise FileNotFoundError("data/ folder not found. Run Task2 first.")

# Load CSV
df = pd.read_csv(file_path)

# ---------------- TASK 1: LOAD & EXPLORE ----------------

print("First 5 rows:\n")
print(df.head())

print("\nShape of DataFrame:", df.shape)

print("\nAverage score:", df["score"].mean())
print("Average comments:", df["num_comments"].mean())

# ---------------- TASK 2: NUMPY ANALYSIS ----------------

scores = df["score"].values
comments = df["num_comments"].values

print("\n--- Score Statistics ---")
print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Standard Deviation:", np.std(scores))

print("\nHighest score:", np.max(scores))
print("Lowest score:", np.min(scores))

# Category with most stories
top_category = df["category"].value_counts().idxmax()
print("\nCategory with most stories:", top_category)

# Story with most comments
max_comments_idx = np.argmax(comments)
top_story = df.iloc[max_comments_idx]

print("\nMost commented story:")
print("Title:", top_story["title"])
print("Comments:", top_story["num_comments"])

# ---------------- TASK 3: NEW COLUMNS ----------------

# Engagement = comments / (score + 1)
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# is_popular = score > average score
avg_score = df["score"].mean()
df["is_popular"] = df["score"] > avg_score

# ---------------- TASK 4: SAVE RESULT ----------------

output_path = "data/trends_analysed.csv"
df.to_csv(output_path, index=False)

print(f"\nSaved analysed data to {output_path}")
print(f"Total rows saved: {len(df)}")
