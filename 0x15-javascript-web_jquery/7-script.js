const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$.getJSON(url, (character) => {
  $('div#character').text(character.name);
});
