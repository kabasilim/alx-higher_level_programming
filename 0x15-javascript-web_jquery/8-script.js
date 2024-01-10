$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (films) {
  $.each(films.results, function (index, film) {
    console.log(film.title);
    $('UL#list_movies').append('<li>' + film.title + '</li>');
  });
});
