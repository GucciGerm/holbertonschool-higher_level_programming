#!/usr/bin/python3
import requests
from sys import argv

"""
This script will take in a url, send a rqst to url, and display the
body of the response using requests and sys
if http status code is >= 400 print Errorcode: (value) of http status
code
"""

if __name__ == "__main__":

    req = requests.get(argv[1])

    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
