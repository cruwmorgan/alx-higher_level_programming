#!/usr/bin/node
const size = process.argv[2];
if (!parseInt(size)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < size; x++) {
    for (let y = 0; y < size; y++) {
      console.log('X');
    }
  }
}
