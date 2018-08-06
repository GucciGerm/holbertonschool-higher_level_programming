#!/usr/bin/python3
# This script will take in a url, display x-request-Id
import urllib.request
import sys

if __name__ == "__main__":

    arg = sys.argv[1]

    with urllib.request.urlopen(arg) as response:
        obj = response.getheader("X-Request-Id")
        print(obj)
