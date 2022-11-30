#!/usr/bin/node

const process = require('process');
const args = process.argv.slice(2, 3);

function fact (a) {
  if (a === 1) {
    return (1);
  }
  return (a * fact(a - 1));
}

if (isNaN(args[0])) {
  args[0] = 1;
} else if (!(isNaN(args[0]))) {
  args[0] = +(args[0]);
}

console.log(fact(args[0]));
