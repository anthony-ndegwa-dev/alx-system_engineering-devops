#!/usr/bin/python3
"""
A recursive function that queries Reddit API, parses titles of all hot
articles, & prints a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript should count as javascript,
but java should not).

Requirements:
    Prototype: def count_words(subreddit, word_list)
    Note: You may change the prototype, but it must be able to be called with
           just a subreddit supplied & a list of keywords. AKA you can add a
           counter or anything else, but the function must work without
           supplying a starting value in the main.
    If word_list contains the same word (case-insensitive), the final count
      should be the sum of each duplicate (example below with java)
    Results should be printed in descending order, by the count, & if count is
      same for separate keywords, they should then be sorted alphabetically
      (ascending, from A to Z). Words with no matches should be skipped & not
      printed. Words must be printed in lowercase.
    Results are based on number of times a keyword appears, not titles it
      appears in. java java java counts as 3 separate occurrences of java.
    To make life easier, java. or java! or java_ should not count as java
    If no posts match or the subreddit is invalid, print nothing.
    NOTE: Invalid subreddits may return a redirect to search results.
          Ensure that you are NOT following redirects.

Your code willn't pass if you're using a loop & not recursively calling the
function! This /can/ be done with a loop but use a recursive function.
"""
import re
import requests
import sys


def add_title(dictionary, hot_posts):
    """ Adds item into a list """
    if len(hot_posts) == 0:
        return

    title = hot_posts[0]['data']['title'].split()
    for word in title:
        for key in dictionary.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(word):
                dictionary[key] += 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
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
    add_title(dictionary, hot_posts)
    after = dic['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list):
    """ Init function """
    dictionary = {}

    for word in word_list:
        dictionary[word] = 0

    recurse(subreddit, dictionary)

    n = sorted(dictionary.items(), key=lambda kv: kv[1])
    n.reverse()

    if len(n) != 0:
        for item in n:
            if item[1] is not 0:
                print("{}: {}".format(item[0], item[1]))
    else:
        print("")
