#!/usr/bin/node
if (process.argv[2] === undefined || process.argv.length < 4) {
  console.log('0');
} else {
  console.log(process.argv.sort()[process.argv.length - 2]);
}
