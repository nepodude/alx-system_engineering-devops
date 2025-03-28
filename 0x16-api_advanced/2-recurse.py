#!/usr/bin/python3
"""Goes through the subreddit to find how many things are there"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetches all hot post titles from a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "custom-user-agent"}
    params = {"after": after, "limit": 100}  # Pagination handling

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    posts = data.get("children", [])
    hot_list.extend(post["data"]["title"] for post in posts)

    after = data.get("after")
    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
