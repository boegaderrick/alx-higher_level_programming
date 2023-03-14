#!/usr/bin/node
/* This module contains a square class */
const baseSquare = require('./5-square');

class Square extends baseSquare {
  charPrint (c = 'X') {
    /* This method prints square using passed char or 'X' as default */
    let string = '';
    let h = this.height;
    for (let i = 0; i < this.width; i++) {
      string += c;
    }
    while (h > 0) {
      console.log(string);
      h--;
    }
  }
}

module.exports = Square;
