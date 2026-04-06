"""
Task 4: Visualization
"""

import matplotlib.pyplot as plt
from task2_data_processing import process_data


def visualize():
    df = process_data()

    if df.empty:
        print("No data to visualize")
        return

    # Endpoint distribution
    df["endpoint"].value_counts().plot(kind="bar", title="Articles by Endpoint")
    plt.show()

    # Time series
    df.groupby(df["date"].dt.date).size().plot(title="Articles Over Time")
    plt.show()


if __name__ == "__main__":
    visualize()
