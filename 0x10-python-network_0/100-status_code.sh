#!/bin/bash
# This script will send a request to a url passed as arg, display status code
curl -sLw "%{http_code}" "$1" -o /dev/null
