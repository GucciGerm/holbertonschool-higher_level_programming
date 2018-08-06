#!/usr/bin/python3
import requests
import sys

"""
This script will take a url + email, send a post request to url
"""

if __name__ == "__main__":

    arg = sys.argv[1]
    email = {"email": sys.argv[2]}
    req = requests.post(arg, email)
    print(req.text)
