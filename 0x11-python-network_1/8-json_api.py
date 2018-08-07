#!/usr/bin/python3
import sys
import requests

"""
This script will take in a letter and send post request to address
with letter as parameter
"""

if __name__ == "__main__":

    input = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    try:
        dict = {'q': q}
        req = requests.post(input, dict)
        values = req.json()

        if 'id' and 'name' in values:
            print("[{}] {}".format(values['id'], values['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
