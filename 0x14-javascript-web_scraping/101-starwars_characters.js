#!/usr/bin/node
/* This script request a movie from an API and outputs the names
 * of all characters
 */
let request = require('request');
const util = require('util');
const argv = require('process').argv;
const url = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  async function final () {
    let idx;
    const characters = JSON.parse(body).characters;
    request = util.promisify(request);
    for (idx in characters) {
      const response = await request(characters[idx]);
      body = JSON.parse(response.body);
      console.log(body.name);
    }
  }
  final();
});
