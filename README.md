# trendpulse---AkashChotapalli

# 📊 TrendPulse – Data Pipeline Project

## 📌 Overview

TrendPulse is a data pipeline project that fetches live trending data from a public API, processes it, analyzes patterns, and visualizes insights.

This project demonstrates an end-to-end pipeline built using Python, covering:

* Data Collection
* Data Processing
* Data Analysis
* Data Visualization

---

## ⚙️ Tech Stack

* Python 🐍
* Pandas
* SQLite
* Matplotlib
* NewsData.io API

---

## 📁 Project Structure

```
trendpulse-yourname/
│
├── task1_data_collection.py      # Fetch data from API & store in SQLite
├── task2_data_processing.py     # Clean & prepare data
├── task3_analysis.py            # Generate insights
├── task4_visualization.py       # Create visualizations
```

---

## 🔄 Pipeline Flow

1️⃣ **Data Collection**

* Fetch live news data from NewsData.io API
* Convert nested JSON into SQL-safe format
* Store data in SQLite database (`news.db`)

2️⃣ **Data Processing**

* Load data from SQLite
* Handle missing values
* Remove duplicates
* Convert date formats

3️⃣ **Data Analysis**

* Articles count by source
* Articles trend over time
* Distribution analysis

4️⃣ **Data Visualization**

* Bar charts (articles by endpoint/source)
* Time-series trends

---

## 🔑 API Used

* NewsData.io (Free Public API)

---

## ▶️ How to Run

### Step 1: Fetch Data

```python
from task1_data_collection import fetch_data
fetch_data()
```

### Step 2: Process Data

```python
from task2_data_processing import process_data
process_data()
```

### Step 3: Analyze Data

```python
from task3_analysis import analyze
analyze()
```

### Step 4: Visualize Data

```python
from task4_visualization import visualize
visualize()
```

---

## ⚠️ Important Notes

* API key is stored securely using environment variables / Colab secrets
* No CSV files are used — data is stored in SQLite
* Pipeline is modular and each step feeds into the next

---

## 📈 Key Learnings

* Handling real-world API data (nested JSON)
* Building ETL pipelines
* Data cleaning & transformation
* SQLite integration
* Visualization using Matplotlib

---

## 🚀 Future Improvements

* Add more APIs (multi-source pipeline)
* Automate pipeline using scheduling
* Deploy as a dashboard

---

## 👨‍💻 Author

Akash Chotapalli
---
