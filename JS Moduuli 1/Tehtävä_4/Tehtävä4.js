'use strict';

let fillHouse = document.querySelector('#fillHouse');

// Tylypahkan talot:
let house1 = 'Gryffindor';
let house2 = 'Slytherin';
let house3 = 'Ravenclaw';
let house4 = 'Hufflepuff';

//  pyydetään käyttäjän nimi:
let name = prompt("What's your name?");

//  arvotaan käyttäjälle talo Tylypahkasta
function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}
let int = getRandomInt(4);
if (int == 1) {
  fillHouse.innerHTML = `${name}, you are ${house1}.`

} else if (int == 2) {
  fillHouse.innerHTML = `${name}, you are ${house2}.`

} else if (int == 3) {
  fillHouse.innerHTML = `${name}, you are ${house3}.`

} else {
  fillHouse.innerHTML = `${name}, you are ${house4}.`
}

