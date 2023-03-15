#!/usr/bin/node
/* This script finds second largest number of arguments passed */

const arr = process.argv.slice(2);
if (arr.length < 2) {
  console.log(0);
} else {
  let largest = parseInt(arr[0]);
  for (let i = 0; i < arr.length; i++) {
    arr[i] = parseInt(arr[i]);
    if (arr[i] > largest) {
      largest = arr[i];
    }
  }
  let sLargest = arr[0];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > sLargest && arr[i] < largest) {
      sLargest = arr[i];
    }
  }
  console.log(sLargest);
}
