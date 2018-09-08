// This script adds a list element to a list when a user clicks DIV#add_item

$('DIV#add_item').click(function () {
  $('<li>Item</li>').appendTo('UL.my_list');
});
