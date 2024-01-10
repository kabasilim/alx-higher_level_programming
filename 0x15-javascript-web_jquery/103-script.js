$('document').ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (e) {
      if (e.which === 13) {
        translate();
      }
    });
  });
});

function translate () {
  $.get('https://www.fourtonfish.com/hellosalut/hello/' + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    $('DIV#hello').text = data.hello;
  });
}
