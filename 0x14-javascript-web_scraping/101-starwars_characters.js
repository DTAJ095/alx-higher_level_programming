#!/usr/bin/node

const request = require('request');
const movieUrl = 'https://swapi-api.alx-tools.com/api/films/'.concat(process.argv[2]);

function printCharactersMovie (characters, idx) {
  request(characters[idx], function (_error, _response, body) {
    if (_error) {
      console.log(_error);
    } else {
      body = JSON.parse(body);
      console.log(body.name);
      if (idx + 1 < characters.length) {
        printCharactersMovie(characters, idx + 1);
      }
    }
  });
}

request(movieUrl, function (error, _response, body) {
  if (error) {
    console.log(error);
  } else {
    body = JSON.parse(body);
    const characters = body.characters;
    printCharactersMovie(characters, 0);
  }
});
