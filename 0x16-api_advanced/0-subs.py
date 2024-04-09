#!/usr/bin/python3

""" Function that queries the Reddit api and
return the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """ Return the number of subscribers """
    data = requests.get("https://www.reddit.com/r/{}/about.json"
                        .format(subreddit),
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    
    if data.status_code >= 300:
        return 0
    return data.json().get("data").get("subscribers")
