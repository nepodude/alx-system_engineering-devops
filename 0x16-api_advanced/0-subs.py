#!/usr/bin/python3
"""
Queries the Reddit API to get the number of subscribers in a subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "custom-user-agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data["data"].get("subscribers", 0)
    return 0
