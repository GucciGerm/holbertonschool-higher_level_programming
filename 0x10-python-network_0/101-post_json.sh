#!/bin/bash
# This script will send a json post request to a url as arg, display body
curl -sX POST "$1" -d "@$2" -H "Content-Type: application/json"
