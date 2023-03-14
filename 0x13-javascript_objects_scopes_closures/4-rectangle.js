#!/usr/bin/node
/* This module contains a Rectangle class */

class Rectangle {
  /* Rectangle class definition */
  constructor (w, h) {
    /* Instance initializer */
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    /* This method prints rectangle using 'X' */
    let string = '';
    let h = this.height;
    for (let i = 0; i < this.width; i++) {
      string += 'X';
    }
    while (h > 0) {
      console.log(string);
      h--;
    }
  }

  rotate () {
    /* This method swaps the width and height values */
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    /* This method doubles width and height */
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
