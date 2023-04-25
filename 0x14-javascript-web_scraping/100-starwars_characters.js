#!/usr/bin/node
/* This script request a movie from an API and outputs the names
 * of all characters
 */
const request = require('request');
const argv = require('process').argv;
const url = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const characters = JSON.parse(body).characters;
  let idx;
  for (idx in characters) {
    request(characters[idx], (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  }
});
