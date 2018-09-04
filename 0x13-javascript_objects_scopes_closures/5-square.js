#!/usr/bin/node

const Rectangle = require('./4-rectangle');

// This script will define a class square and inherit from Rectangle

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
