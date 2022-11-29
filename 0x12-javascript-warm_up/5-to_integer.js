#!/usr/bin/node

const process = require('process');
const args = process.argv.slice(2, 3);

if (!(args[0]) || isNaN(args[0])) {
  console.log('Not a number');
} else if (!(isNaN(args[0]))) {
  const toNum = +(args[0]);
  console.log('My number: ', Math.trunc(toNum));
}
