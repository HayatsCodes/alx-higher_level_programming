#!/usr/bin/node

const process = require('process');
const args = process.argv.slice(2, 4);

function add(a, b) {
  return (a + b);
}
if (!(isNaN(args[0])) && !(isNaN(args[1]))) {
  console.log(add(+(args[0]), +(args[1])));
} else {
    console.log(NaN);
}
