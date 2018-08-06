#!/usr/bin/python3
import sys
import requests

"""
This script will take in a url, send a rqst to url, display the val of
 X-request-Id in response header using requests and sys
"""

if __name__ == "__main__":

    arg = sys.argv[1]
    req = requests.get(arg)
    print(req.headers.get("X-Request-Id"))
