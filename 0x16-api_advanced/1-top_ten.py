#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts"""

import requests


def top_ten(subreddit):
    """Prints the top 10 hot post titles from a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "my_reddit_scraper/1.0"}
    params = {"limit": 10}  # Get only the first 10 posts

    response = requests.get(url, headers=headers,
    params=params, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data", {}).get("children", [])

    if not data:
        print(None)
        return

    for post in data:
        print(post["data"]["title"])
