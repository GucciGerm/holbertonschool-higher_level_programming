#!/bin/bash
# This bash script will take a url, send a request to that url + display size
curl -sI "$1" | grep Content-Length | cut -d " " -f2
