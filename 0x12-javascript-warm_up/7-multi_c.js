#!/usr/bin/node
const argv = process.argv[2];
if (argv) {
  for (let x = 0; x < argv; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
