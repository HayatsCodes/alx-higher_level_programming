#!/usr/bin/node

const process = require('process');
args = process.argv.slice(2, 3);

if (!(args[0]) || isNaN(args)) {
  console.log('Missing size');
} else if (!(isNaN(args))) {
    const toNum = +(args[0]);
    let square = '';
    let i = 0;
    for (; i < toNum; i++) {
      square += 'X';  
    }
    i = 0;
    while (i < toNum) {
      console.log(square);
      i++;
    }
  }

    
