#!/usr/bin/node

// This script prints the number of movies that Wedge Antilles is present

let request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    // Get results
    let allcontent = JSON.parse(body).results;
    // Account for how many movies they've been in
    for (let mcount of allcontent) {
      // Access characters from previous for loop
      for (let ccount of mcount.characters) {
        if (ccount.search('18') > 0) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
