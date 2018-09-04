#!/usr/bin/node

// This function will return the number of occurences in a list

exports.nbOccurences = function (list, searchElement) {
  let instances = 0;
  let count;
  for (count = 0; count < list.length; count++) {
    if (list[count] === searchElement) {
      instances += 1;
    }
  }
  return (instances);
};
