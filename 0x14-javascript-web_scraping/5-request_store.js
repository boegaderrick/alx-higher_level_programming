#!/usr/bin/node
/* This script sends a request to an API and writes the response
 * to a file.
 * It takes the API url and the name of the file to write to as
 * the first and second arguments respectively.
 */
const request = require('request');
const fs = require('fs');
const argv = require('process').argv;

request(argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  fs.writeFile(argv[3], body, 'utf-8', (error) => {
    if (error) {
      console.log(error);
    }
  });
});
