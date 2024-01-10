$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (character) {
  $('DIV#character').text(character.name);
});
