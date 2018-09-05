#!/usr/bin/node

// This script will print the title of starwars movie w/ epi # matches given int

let request = require('request');
let url = ('http://swapi.co/api/films/' + process.argv[2]);

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
