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
    data.characters.forEach(function (result) {
      request(result, function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          const info = JSON.parse(body);
          matchchar.push(info.name);
        }
      });
    });
    console.log(matchchar);
  }
});
