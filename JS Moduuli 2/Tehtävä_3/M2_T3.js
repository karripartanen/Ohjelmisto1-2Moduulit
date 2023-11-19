//  Write a program that asks for the names of six dogs. The program prints dog names
//  to unordered list <ul> in reverse alphabetical order.

'use strict';
let fillDogs = document.querySelector('.fillDogs');
const ul = document.createElement('ul');
fillDogs.append(ul)

let i = 0; // iterator
let dogName = '';
const dogList = [];

for (i=0; i<6; i++) {
  dogName = prompt('Provide a name of a dog');
  dogList.push(dogName);
}
dogList.sort().reverse();

for (i=0; i<6; i++) {
  const newLi = document.createElement('li');
  newLi.innerText = `${dogList[i]}`;
  ul.append(newLi);
}

ul.style = 'list-style-type: none';

