#!/usr/bin/node
/* This script requests a list of tasks from an API passed as a
 * command-line argument and then computes the number of tasks
 * completed by each user and outputs the users alongside their
 * respective number of completed tasks. Users without at least
 * one completed task are ignored.
 */
const request = require('request');
const argv = require('process').argv;

request(argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const tasks = JSON.parse(body);
  const final = {};
  let idx;
  let user;
  for (idx in tasks) {
    if (tasks[idx].completed) {
      user = tasks[idx].userId;
      if (final[user] === undefined) {
        final[user] = 1;
      } else {
        final[user]++;
      }
    }
  }
  console.log(final);
});
