#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body
   Handles HTTP errors
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    rq = requests.get(url)
    if rq.status_code >= 400:
        print("Error code: {}".format(rq.status_code))
    else:
        print(rq.text)
