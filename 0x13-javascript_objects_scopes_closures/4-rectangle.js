#!/usr/bin/node

// This script will define a rectangle with new methods rotate, double

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    let a;
    let b;
    for (a = 0; a < this.height; a++) {
      let size = '';
      for (b = 0; b < this.width; b++) {
        size += 'X';
      }
      console.log(size);
    }
  }
  rotate () {
    let block;
    block = this.width;
    this.width = this.height;
    this.height = block;
  }
  double () {
    this.width = (this.width * 2);
    this.height = (this.height * 2);
  }
}

module.exports = Rectangle;
