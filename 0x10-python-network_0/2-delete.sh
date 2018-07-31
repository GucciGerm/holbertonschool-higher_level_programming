#!/bin/bash
# This bash script will send a delete request to the Url and display the body
# of our response "im a delete request"
curl -sX DELETE "$1"
