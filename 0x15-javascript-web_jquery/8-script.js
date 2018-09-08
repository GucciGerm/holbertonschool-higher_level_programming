// This script fetches and lists all movies title by this url

let content = 'https://swapi.co/api/films/?format=json';
$.get(content, function (data) {
  for (let films of data.results) {
    $('UL#list_movies').append($('<li></li>').text(films.title));
  }
});
