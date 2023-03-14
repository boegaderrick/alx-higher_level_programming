#!/usr/bin/node
/* This module contains a function that prints and keeps count of number of calls */

let count = 0;
exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
