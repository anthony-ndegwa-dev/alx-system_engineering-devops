#!/usr/bin/python3
"""
A function that queries Reddit API & returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If invalid
subreddit is given, function should return 0.

Hint: No authentication is necessary for most features of the Reddit API.
If you’re getting errors related to Too Many Requests, ensure you’re
setting a custom User-Agent.

Requirements:
    Prototype: def number_of_subscribers(subreddit)
    If not a valid subreddit, return 0.
    NOTE: Invalid subreddits may return a redirect to search results.
    Ensure that you are not following redirects.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """ Queries to Reddit API """
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    dic = res.json()
    if 'data' not in dic:
        return 0
    if 'subscribers' not in dic.get('data'):
        return 0
    return res.json()['data']['subscribers']
