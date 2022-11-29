#!/usr/bin/node

const process = require('process');
const args = process.argv;

let argsLength = 0;
args.forEach((val, index) => {
  argsLength = index + 1;
  if (index === 2) {
    console.log(val);
  }
});
if (argsLength < 3) {
  console.log('No argument');
}
