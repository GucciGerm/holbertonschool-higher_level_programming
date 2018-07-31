#!/bin/bash
# This bash script will take in a url and display http methods server will acpt
curl -sI "$1" | grep Allow | cut -d " " -f2-
