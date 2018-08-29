#!/usr/bin/node

if (Number(process.argv[2])) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else if (process.argv[2]) {
  console.log('Not a number');
} else {
  console.log('Not a number');
}
