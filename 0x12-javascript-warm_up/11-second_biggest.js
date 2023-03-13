#!/usr/bin/node

const arr = process.argv.slice(2).sort().reverse();
if (arr.length < 2) {
  console.log(0);
} else {
  console.log(arr[1]);
}
