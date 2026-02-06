const add_item = document.getElementById('add_item');
const my_list = document.querySelector('.my_list');
add_item.addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    my_list.appendChild(newItem);
});