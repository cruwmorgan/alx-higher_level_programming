$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const len = data.results.length;
    for (let x = 0; x < len; x++) {
      $('UL#list_movies').append('<li>' + data.results[x].title + '</li>');
    }
  });
});
