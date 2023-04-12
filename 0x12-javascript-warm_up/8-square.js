#!/usr/bin/node
const size = process.argv[2];
if (!parseInt(size)) {
  console.log('Missing size');
} else {
  let string = '';
  for (let x = 0; x < size; x++) {
    for (let y = 0; y < size; y++) {
      string += 'X';
    }
    string += '\n';
  }
  console.log(string);
}
