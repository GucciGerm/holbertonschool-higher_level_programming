#!/usr/bin/node
function factorial (input) {
  if (isNaN(input)) {
    return 1;
  }
  if (input === 0) {
    return 1;
  } else {
    return input * factorial(input - 1);
  }
}

console.log(factorial(process.argv[2]));
