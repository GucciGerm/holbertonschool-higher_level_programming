#!/usr/bin/node

// This function will print the num of args already printed + new arg value

let current = 0;
exports.logMe = function (item) {
  let printout = current + ': ' + item;
  console.log(printout);
  current++;
};
