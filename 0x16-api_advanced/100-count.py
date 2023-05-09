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

def count_words(subreddit, word_list, after=None, count_dict=None):
    if count_dict is None:
        count_dict = {}

    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data['data']['children']

    for post in posts:
        title = post['data']['title']
        words = re.findall(r'\b\w+\b', title.lower())

        for word in word_list:
            if word.lower() in words:
                count_dict[word.lower()] = count_dict.get(word.lower(), 0) + words.count(word.lower())

    after = data['data']['after']
    if after is not None:
        count_words(subreddit, word_list, after, count_dict)
    else:
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))

        for word, count in sorted_counts:
            print(f"{word}: {count}")
