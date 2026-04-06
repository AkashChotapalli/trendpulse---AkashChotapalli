"""
Task 3: Analysis
"""

from task2_data_processing import process_data


def analyze():
    df = process_data()

    if df.empty:
        print("No data available")
        return

    print("\nArticles per endpoint:")
    print(df["endpoint"].value_counts())

    print("\nTop sources:")
    print(df["source_id"].value_counts().head())

    print("\nArticles per day:")
    print(df.groupby(df["date"].dt.date).size())


if __name__ == "__main__":
    analyze()
