#!/usr/bin/node

const request = require('request');
const starWarUrl = process.argv[2];
let count = 0;

request(starWarUrl, function (_error, _response, body) {
  body = JSON.parse(body).results;

  for (let i = 0; i < body.length; ++i) {
    const characters = body[i].characters;

    for (let j = 0; j < characters.length; ++j) {
      const character = characters[j];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        count += 1;
      }
    }
  }
  console.log(count);
});
