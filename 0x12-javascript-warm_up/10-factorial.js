#!/usr/bin/node
const argv = parseInt(process.argv[2]);
function factorial (argv) {
  if (argv === 0) {
    return (1);
  } else {
    return (factorial(argv - 1) * argv);
  }
}
if (argv) {
  const result = factorial(argv);
  console.log(result);
} else {
  console.log('1');
}
