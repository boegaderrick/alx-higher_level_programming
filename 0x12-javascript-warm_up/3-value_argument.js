#!/usr/bin/node

const temp = process.argv[2];
if (temp) {
  console.log(temp);
} else {
  console.log('No argument');
}
