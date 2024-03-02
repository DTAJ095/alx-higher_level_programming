#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    try:
        data = {'q': sys.argv[1]}
    except Exception:
        data = {'q': ''}
    session = requests.Session()
    response = session.post(url, data=data)
    try:
        json_res = response.json()
        if len(json_res) == 0:
            print('No result')
        else:
            _id = json_res.get('id')
            _name = json_res.get('name')
            print('[{}] {}'.format(_id, _name))
    except ValueError as invalid_json:
        print('Not a valid json')
