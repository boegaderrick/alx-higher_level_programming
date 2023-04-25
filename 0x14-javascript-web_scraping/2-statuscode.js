#!/usr/bin/node
/* This script sends a get request and prints the returned status code */
const request = require('request');
const argv = require('process').argv;

request(argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log('code:', response.statusCode);
});
