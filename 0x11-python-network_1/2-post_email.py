#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response (decoded in utf-8)
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    param = {"email": email}
    query = urllib.parse.urlencode(param)
    data = query.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        response_txt = response.read().decode("utf-8")
        print(response_txt)
