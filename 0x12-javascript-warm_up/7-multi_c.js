#!/usr/bin/node

const process = require('process');
const args = process.argv.slice(2, 3);

if (!(args[0]) || isNaN(args[0])) {
  console.log('Missing number of occurrences');
} else if (!(isNaN(args[0]))) {
    let toNum = +(args[0]);
    toNum = Math.trunc(toNum);
    let i = 0;
    for (; i < toNum; i++) {
      console.log('C is fun');
    }
}

