#!/usr/bin/node
/* This script requests movie objects from an API using ids passed
 * in the command-line as arguments and outputs their titles
 */
const request = require('request');
const argv = require('process').argv;

const url = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log(JSON.parse(body).title);
});
