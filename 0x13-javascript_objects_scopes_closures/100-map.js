#!/usr/bin/node
/* Multiplies contents of imported list by index and stores results in new list */

const list = require('./100-data.js').list;
const n = list.map(function (x, index) { return x * index; });
console.log(list);
console.log(n);
