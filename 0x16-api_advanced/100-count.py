#!usr/bin/python3
"""a script for counting the words in a case insensitive way"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """Recursively fetches hot posts and counts keyword occurrences"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "custom-user-agent"}
    params = {"after": after, "limit": 100}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])
    
    # Normalize word_list (case-insensitive and remove duplicates)
    word_list = [word.lower() for word in word_list]

    # Initialize word_count dictionary
    if not word_count:
        word_count = {word: 0 for word in word_list}

    for post in posts:
        title = post["data"]["title"].lower().split()
        for word in title:
            cleaned_word = ''.join(filter(str.isalpha, word))  # Remove punctuation
            if cleaned_word in word_count:
                word_count[cleaned_word] += 1

    after = data.get("after")
    if after:
        return count_words(subreddit, word_list, word_count, after)

    # Print sorted results
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_words:
        if count > 0:
            print(f"{word}: {count}")
