#!/usr/bin/node
/* This script writes to a file specified by a cmd-line argument */
const fs = require('fs');
const argv = require('process').argv;

fs.writeFile(argv[2], argv[3], 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
