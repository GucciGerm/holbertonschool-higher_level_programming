#!/bin/bash
# This script will take in a url, send a get request, display the body
curl -LX GET "$1"
