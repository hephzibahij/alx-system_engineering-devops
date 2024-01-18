#!/usr/bin/python3
"""
Module for interacting with the Reddit API and printing titles of
the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given
    subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=user_agent, params=params)
    results = response.json()

    try:
        my_data = results.get('data').get('children')

        for i in my_data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
