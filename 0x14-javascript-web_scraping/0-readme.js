#!/usr/bin/node
/* This script reads a file and outputs its contents */
const fs = require('fs');
const argv = require('process').argv;

fs.readFile(argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
