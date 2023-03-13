#!/usr/bin/node

let num = parseInt(process.argv[2]);

if (num && typeof (num) === 'number') {
  while (num > 0) {
    console.log('C is fun');
    num--;
  }
} else {
  console.log('Missing number of occurrences');
}
