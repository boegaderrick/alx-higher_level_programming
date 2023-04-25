#!/usr/bin/node
/* This script request the star wars API for a character and outputs
 * the number of films they've made appearances in the franchise
 */
const request = require('request');
const argv = require('process').argv;

const url = argv[2].replace('films', 'people/18');
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log(JSON.parse(body).films.length);
});
