import setup

import requests
import json
import time
import os
from datetime import datetime
from google.colab import files
import pandas as pd

defining categories

def assign_category(title):
    title = title.lower()

    # Technology
    if any(keyword in title for keyword in [
        "ai", "software", "tech", "code", "computer",
        "data", "cloud", "api", "gpu", "llm"
    ]):
        return "technology"

    # World News
    elif any(keyword in title for keyword in [
        "war", "government", "country", "president",
        "election", "climate", "attack", "global"
    ]):
        return "worldnews"

    # Sports
    elif any(keyword in title for keyword in [
        "nfl", "nba", "fifa", "sport", "game",
        "team", "player", "league", "championship"
    ]):
        return "sports"

    # Science
    elif any(keyword in title for keyword in [
        "research", "study", "space", "physics",
        "biology", "discovery", "nasa", "genome"
    ]):
        return "science"

    # Entertainment
    elif any(keyword in title for keyword in [
        "movie", "film", "music", "netflix",
        "game", "book", "show", "award", "streaming"
    ]):
        return "entertainment"

    else:
        return "general"

fetch data


def get_story_ids():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"

    try: # used for any exception
        response = requests.get(url)
        return response.json()
    except:
        print("Failed to fetch story IDs")
        return []

fetch id wise data

def fetch_story(story_id): #story_id refers to the id of each story from the previous cell
    url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"

    try:
        response = requests.get(url)
        return response.json()
    except:
        print(f"Failed to fetch story {story_id}")
        return None

# main part of collecting the data

def collect_data():
    story_ids = get_story_ids()

    collected = []
    category_count = {
    "technology": 0,
    "worldnews": 0,
    "sports": 0,
    "science": 0,
    "entertainment": 0,
    "general": 0
}
#iteration for each category
    for story_id in story_ids:
        story = fetch_story(story_id)

        if not story:
            continue

        title = story.get("title", "")
        category = assign_category(title)

        # limit 25 per category
        if category_count[category] >= 25:
            continue

        data = {
            "post_id": story.get("id"),
            "title": title,
            "category": category,
            "score": story.get("score"),
            "num_comments": story.get("descendants"),
            "author": story.get("by"),
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        collected.append(data)
        category_count[category] += 1

        # stop if 125 collected
        if len(collected) >= 125:
            break

    # sleep AFTER category loop
    time.sleep(2)

    return collected

#save to JSON


def save_to_json(data):
    # create folder if not exists
    if not os.path.exists("data"):
        os.makedirs("data")

    filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Saved {len(data)} stories to {filename}")

    return filename

#
to collect data in some filepath


data = collect_data()
file_path = save_to_json(data)
