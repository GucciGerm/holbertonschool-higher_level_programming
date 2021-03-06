#!/usr/bin/python3
"""
This script will take in url, send request to url, display body utf-8
learning to manage urllib.error.HTTPError
"""

import urllib.request
import sys
import urllib.error

if __name__ == "__main__":

    arg = sys.argv[1]

    try:
        with urllib.request.urlopen(arg) as url:
            val = url.read().decode("utf-8")
            print(val)
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
