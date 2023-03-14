#!/usr/bin/node
/* This script reads two files and writes content to third file */
const fs = require('fs').promises;

/*
for (let i = 2; i < 4; i--) {
  fs.readFile(process.argv[i], 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
    }
    fs.writeFile(process.argv[4], data, { flag: 'a' }, () => {});
  });
} */

const src = [process.argv[2], process.argv[3]];

Promise.all(src.map(x => fs.readFile(x, 'utf-8')))
  .then(data => fs.writeFile(process.argv[4], data.join('')));
