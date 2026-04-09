
import requests
import json
import time
import os
from datetime import datetime
from google.colab import files
import pandas as pd

import pandas as pd
import os

file_path = "data/trends_sample.json" # this file will be uploaded in github for validation

# Case 1 — GitHub submission file
if os.path.exists(file_path):
    pass

# Case 2 — Colab dynamic file
elif os.path.exists("data"):
    files = [f for f in os.listdir("data") if f.endswith(".json")]
    
    if files:
        file_path = "data/" + files[0]
    else:
        raise FileNotFoundError("No JSON file found inside data/")

# Case 3 — Nothing exists
else:
    raise FileNotFoundError("data/ folder not found. Run Task1 first or upload JSON.")

# Load
df = pd.read_json(file_path)

print(f"Loaded {len(df)} stories from {file_path}")

#below chunk is for removing the duplicates

before = len(df)

df = df.drop_duplicates(subset=["post_id"]) #used for removing duplicates

after = len(df)
print(f"After removing duplicates: {after}")

#below is for droping nulls


df = df.dropna(subset=["post_id", "title", "score"])

print(f"After removing nulls: {len(df)}")

#below chunk is for making sure of datatypes


df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

#below chunk is for removing low scores

df = df[df["score"] >= 5]

print(f"After removing low scores: {len(df)}")

##below chunk is for removing spaces

df["title"] = df["title"].str.strip() #strip is used for removing spaces


#below chunk is for saving data in outputpath

output_path = "data/trends_clean.csv" #trends_clean is the file in csv format post cleaning

df.to_csv(output_path, index=False)

print(f"\nSaved {len(df)} rows to {output_path}")
