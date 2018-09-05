#!/usr/bin/node

// This script that displays the status code of a get request

let request = require('request');

request.get(process.argv[2]).on('response', function (response) {
  console.log('code: ' + response.statusCode);
});
