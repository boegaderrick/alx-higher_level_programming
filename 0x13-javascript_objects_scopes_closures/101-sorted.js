#!/usr/bin/node
/* Creates modified dictionary from imported dictionary */
const dict = require('./101-data').dict;

const n = {};
Object.keys(dict).forEach(function (x) {
  if (!n[dict[x]]) {
    n[dict[x]] = [];
  }
  n[dict[x]].push(x);
});
console.log(n);
