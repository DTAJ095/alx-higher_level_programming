#!/usr/bin/python3
""" Python script that takes 2 arguments
in order to solve this challenge.
"""
import sys
import requests


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = 'https://api.github.com/reppos/{}/{}/commits'.format(repo_name,
                                                               owner_name)
    session = requests.Session()
    response = session.get(url)
    res = response.json()
    i = 0
    for commit in res:
        if i < 10:
            if type(commit) == dict:
                print('{}: {}'.format(commit.get('sha'),
                                  commit.get('commit').get('author')
                                  .get('name')))
        i += 1
