#!/usr/bin/node

const process = require('process');
const args = process.argv.slice(2, 4);

console.log(args[0] + ' is ' + args[1]);
