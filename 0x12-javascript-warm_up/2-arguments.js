#!/usr/bin/node
const counter = process.argv.lenght;
console.log(counter === 2 ? 'No argument' : counter === 3 ? 'Argument found' : 'Arguments found');
