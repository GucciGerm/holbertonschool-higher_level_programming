#!/bin/bash
# This script will take in a url, send a get request, display the body
curl -sLX GET "$1"
