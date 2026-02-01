#!/usr/bin/node
const process = require('process');

const argsCount = process.argv.length;
const firstArg = process.argv[2];

if (argsCount === 2) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
