#!/usr/bin/python3
""" Python script that takes 2 arguments
in order to solve this challenge.
"""
import sys
import requests


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(repo_name,
                                                              owner_name)
    session = requests.Session()
    response = session.get(url)
    res = response.json()
    i = 0
    for commit in res:
        if i < 10:
            name = commit.get('commit').get('author').get('name')
            print('{}: {}'.format(commit.get('sha'), name))
        i += 1
