#!/usr/bin/node

const request = require('request');
const starWarUrl = process.argv[2];
let count = 0;

request(starWarUrl, function (error, response, body) {
  body = JSON.parse(body).results;

  for (let i = 0; i < body.lenght; i++) {
    const characters = body[i].characters;

    for (let j = 0; j < characters.lenght; j++) {
      const character = characters[j];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        count += 1;
      }
    }
  }
});
