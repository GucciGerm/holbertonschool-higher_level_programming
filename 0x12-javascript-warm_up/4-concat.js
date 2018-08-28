#!/usr/bin/node
const add2 = process.argv[2] + ' is ' + process.argv[3];
const add1 = process.argv[2] + ' is undefined';
if (process.argv.length === 4) {
  console.log(add2);
} else if (process.argv.length === 3) {
  console.log(add1);
} else {
  console.log('undefined is undefined');
}
