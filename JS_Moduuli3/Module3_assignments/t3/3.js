'use strict';
const names = ['John', 'Paul', 'Jones'];
let nameString = '';
for (let name of names) {
  nameString += `<li>${name}</li>\n`; // adding the value of names into li-elements through a for-loop
}
document.querySelector('#target').innerHTML = nameString;
