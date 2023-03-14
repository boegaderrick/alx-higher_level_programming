#!/usr/bin/node
/* This script reads two files and writes content to third file */
const fs = require('fs');

for (let i = 3; i > 1; i--) {
  fs.readFile(process.argv[i], 'utf-8', (err, content) => {
    if (err) {
      console.error(err);
    }
    fs.appendFile(process.argv[4], content, () => {});
  });
}
