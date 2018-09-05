#!/usr/bin/node

// This func will convert a num from base 10 to another base passed as arg

exports.converter = function (base) {
  return function (arg) {
    return arg.toString(base);
  };
};
