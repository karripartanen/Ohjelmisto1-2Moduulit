'use strict'
const targetElem = document.querySelector('#target');
const items = ['First item', 'Second item', 'Third item'];  // array of items
for (let item of items) {
  let listItem = document.createElement('li');
  let txtNode = document.createTextNode(item);
  listItem.appendChild(txtNode);
  targetElem.appendChild(listItem);
}
const second = targetElem.getElementsByTagName('li')[1]; // adding class 'my-item' to second list item
second.classList.add('my-item');
