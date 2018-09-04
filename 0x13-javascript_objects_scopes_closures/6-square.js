#!/usr/bin/node

const SquareImport = require('./5-square');

// This square class will inherit from 5 square, and method charprint is used

class Square extends SquareImport {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let a;
    let b;
    for (a = 0; a < this.height; a++) {
      let Size = '';
      for (b = 0; b < this.width; b++) {
        Size += c;
      }
      console.log(Size);
    }
  }
}

module.exports = Square;
