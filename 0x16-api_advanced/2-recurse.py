#!/usr/bin/python3
"""
A recursive function that queries Reddit API & returns a list containing
titles of all hot articles for a given subreddit. If no results are found for
the given subreddit, the function should return None.

Hint: The Reddit API uses pagination for separating pages of responses.

Requirements:
    Prototype: def recurse(subreddit, hot_list=[])
    Note: You may change the prototype, but it must be able to be called with
          just a subreddit supplied. AKA you can add a counter, but it must
          work without supplying a starting value in the main.
    If not a valid subreddit, return None.
    NOTE: Invalid subreddits may return a redirect to search results.
          Ensure that you are not following redirects.

Your code willn't pass if you're using a loop and not recursively calling the
function! This /can/ be done with a loop but use a recursive function.
"""
import requests
import sys


def add_title(hot_list, hot_posts):
    """ Adds item into a list """
    if len(hot_posts) == 0:
        return
    hot_list.append(hot_posts[0]['data']['title'])
    hot_posts.pop(0)
    add_title(hot_list, hot_posts)


def recurse(subreddit, hot_list=[], after=None):
    """ Queries to Reddit API """
    u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    dic = res.json()
    hot_posts = dic['data']['children']
    add_title(hot_list, hot_posts)
    after = dic['data']['after']
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)
