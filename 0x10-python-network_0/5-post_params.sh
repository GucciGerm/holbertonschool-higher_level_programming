#!/bin/bash
# This bash script will take in a url, send a post request to url passed
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
