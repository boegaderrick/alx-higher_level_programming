#!/usr/bin/node

let num = parseInt(process.argv[2]);
let string = '';

if (num && typeof (num) === 'number') {
  for (let i = 0; i < num; i++) {
    string += 'X';
  }
  while (num > 0) {
    console.log(string);
    num--;
  }
} else {
  console.log('Missing size');
}
