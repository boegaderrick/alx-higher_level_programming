#!/usr/bin/node
/* This module contains a function that checks occurrences */

exports.nbOccurences = function (list, searchElement) {
  /**
   * Function takes two arguments and searches for occurrences
   * list: iterable to be traversed in search of occurrences
   * searchElement: element being searched for
   *
   * Return: number of occurrences
   */
  let count = 0;
  let i = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      count++;
    }
    i++;
  }
  return count;
};
