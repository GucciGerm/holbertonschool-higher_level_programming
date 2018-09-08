// This script will fetch and replace the name of this url

let content = 'https://swapi.co/api/people/5/?format=json';
$.getJSON(content, function (data, status) {
  $('DIV#character').text(data.name);
});
