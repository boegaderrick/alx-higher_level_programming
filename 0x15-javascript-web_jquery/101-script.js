$().ready(() => {
  $('#add_item').on('click', () => {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('#remove_item').on('click', () => {
    $('li').eq(0).remove();
  });
  $('#clear_list').on('click', () => {
    $('li').remove();
  });
});
