#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (_error, response) {
  console.log('code:', response.statusCode); // print the response status code if a response was received
});
