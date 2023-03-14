#!/usr/bin/node
/* This module contains square class that inherits from rectangle class */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  /* Square class definition */
  constructor (size) {
    /* Instance initialization */
    super(size, size);
  }
}

module.exports = Square;
