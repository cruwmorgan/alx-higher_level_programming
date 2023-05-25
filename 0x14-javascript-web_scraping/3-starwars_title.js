#!/usr/bin/node
const request = require('request');
const idMovie = parseInt(process.argv[2]);
const url = 'https://swapi-api.hbtn.io/api/films/' + idMovie;
let data;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    data = JSON.parse(body);
    console.log(data.title);
  }
});
