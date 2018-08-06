#!/usr/bin/python3
# This script will take in url + email, send a post request

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":

    arg = sys.argv[1]
    email = {"email": sys.argv[2]}

    data = urllib.parse.urlencode(email)
    data = data.encode("ascii")
    req = urllib.request.Request(arg, data)
    with urllib.request.urlopen(req) as response:
        val = response.read().decode("utf-8")
        print(val)
