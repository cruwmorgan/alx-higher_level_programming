#!/usr/bin/node
const request = require('request');
const idMovie = parseInt(process.argv[2]);
const url = 'https://swapi-api.hbtn.io/api/films/' + idMovie;
let data;
const matchchar = [];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    data = JSON.parse(body);
    data.characters.forEach(function (character) {
      matchchar.push(character);
    });
  }
  matchchar.forEach(function (chat) {
    request(chat, function (error, response, body) {
      if (!error && response.statusCode === 200) {
        const info = JSON.parse(body);
        console.log(info.name);
      }
    });
  });
});
