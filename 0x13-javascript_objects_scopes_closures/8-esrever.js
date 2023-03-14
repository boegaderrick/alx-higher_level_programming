#!/usr/bin/node
/* This module contains a custom reverse function */

exports.esrever = function (list) {
  if (!list) {
    return list;
  }

  let x = 0;
  let y = list.length - 1;
  let temp;

  while (x < y) {
    temp = list[x];
    list[x] = list[y];
    list[y] = temp;
    x++;
    y--;
  }
  return list;
};
