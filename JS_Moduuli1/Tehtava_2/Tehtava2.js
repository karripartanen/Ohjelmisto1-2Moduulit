'use strict';
//  haetaan html-elementti
let fillName = document.querySelector('#fillName');

//  pyydetään nimi
let name = prompt("What's your name?");

//  printataan käyttäjän nimi
fillName.innerHTML = `Hello, ${name}!`;
