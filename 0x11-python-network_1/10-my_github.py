#!/usr/bin/python3
import requests
import sys

"""
This script will take github credentials(usrname, pswrd)
Use github API to display id
Use Basic Authentication to access information

"""

if __name__ == "__main__":

    req = requests.get("https://api.github.com/user",
                       auth=(sys.argv[1], sys.argv[2]))
    values = req.json()

    try:
        print(values["id"])

    except:
        print(None)
