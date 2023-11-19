'use strict';
let fillCabin = document.querySelector('.fillCabin')

const cabinClass = prompt('Enter the cabin class: A/B/C').toUpperCase();

switch (cabinClass) {
  case 'A':
    fillCabin.innerHTML = 'Top deck cabin with a window.';
    break;

  case 'B':
    fillCabin.innerHTML = 'Top deck cabin without a window';
    break;

  case 'C':
    fillCabin.innerHTML = 'Windowless cabin under the car deck';
    break;

  default:
    fillCabin.innerHTML = 'Invalid cabin class';
}

//  silmukat = loopit = toistorakenteet

//  While, toimii käytännössä kuin pythonissa

let counter = 0;
while (counter <= 5) {
  counter++;
  console.log('tämä ehto oli tosi');
}