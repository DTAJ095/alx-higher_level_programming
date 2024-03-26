#!/usr/bin/node

const request = require('request');
const starWarUrl = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);

request(starWarUrl, function (_error, _response, body) {
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; ++i) {
    request(characters[i], function (_cError, _cResponse, cBody) {
      console.log(JSON.parse(cBody).name);
    });
  }
});
