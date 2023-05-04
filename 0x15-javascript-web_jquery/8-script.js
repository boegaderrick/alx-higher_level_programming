const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.getJSON(url, (response) => {
  const movies = response.results;
  $.each(movies, (idx) => {
    $('ul#list_movies').append(`<li> ${movies[idx].title} </li>`);
  });
});
