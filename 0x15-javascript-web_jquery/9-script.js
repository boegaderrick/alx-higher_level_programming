const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$().ready(() => {
  $.getJSON(url, (response) => {
    $('div#hello').text(response.hello);
  });
});
