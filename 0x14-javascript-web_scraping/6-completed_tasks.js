#!/usr/bin/node

// This script computes the number of tasks completed by user id

let request = require('request');
let completed = {};

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let arg = JSON.parse(body);
    let count;
    for (count = 0; count < arg.length; count++) {
      let objective = arg[count];
      if (objective['completed'] === true) {
        if (completed[objective['userId']] !== undefined) {
	  // Only include +1 if userId present and true
          completed[objective['userId']] += 1;
        } else {
          completed[objective['userId']] = 1;
        }
      }
    }
    console.log(completed);
  }
});
