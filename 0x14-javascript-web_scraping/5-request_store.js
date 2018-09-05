#!/usr/bin/node

// This script gets the content of a webpage and stores it in a file

let request = require('request');
let fs = require('fs');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let newbody = body;
    fs.writeFile(process.argv[3], newbody, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
