#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            res_txt = response.read().decode("utf-8")
            print(res_txt)
    except urllib.error.HTTPError as mess:
        print("Error code: {}".format(mess.code))
