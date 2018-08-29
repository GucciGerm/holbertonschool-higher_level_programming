#!/usr/bin/node
const printme = 'C is fun';

if (process.argv[2] > 0) {
  for (let x = 0; x !== parseInt(process.argv[2]); x++) {
    console.log(printme);
  }
} else if (process.argv[2] < 0) {
} else {
  console.log('Missing number of occurrences');
}
