#!/usr/bin/node

// Comment

class Rectangle {
  constructor (w, h, print) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    // Need to create loops for accounting for width & height
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
}

module.exports = Rectangle;
