#!/usr/bin/python3
""" sends a request to a url"""


import urllib.request
import sys

if __name__ == "__main__":
    link = sys.argv[1]

    val = urllib.request.Request(link)
    with urllib.request.urlopen(val) as reply:
        print(dict(reply.headers).get("X-Request-Id"))
