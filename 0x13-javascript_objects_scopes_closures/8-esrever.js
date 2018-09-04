#!/usr/bin/node

// This script will return the reversed version of contents a list

exports.esrever = function (list) {
  let counter;
  let holder = [];

  // get end of list for start point then we need to add element as we -1
  for (counter = list.length - 1; counter >= 0; counter--) {
    holder.push(list[counter]);
  }
  return (holder);
};
