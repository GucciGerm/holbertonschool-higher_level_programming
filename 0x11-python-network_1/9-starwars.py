#!/usr/bin/python3
import requests
import sys

"""
This script takes in a string and sends search request to
star wars API
"""

if __name__ == "__main__":

    input = 'https://swapi.co/api/people/?search={}'.format(sys.argv[1])
    req = requests.get(input)
    Charc = req.json()
    print("Number of results: {}".format(Charc["count"]))

    for each in Charc["results"]:
        print(each["name"])
