'use strict';

let fillInt = document.querySelector('#intCalc');

//  pyydetään numerot
let int1 = parseFloat(prompt('Provide the first number:'));
let int2 = parseFloat(prompt('Provide the second number:'));
let int3 = parseFloat(prompt('Provide the third number:'));

//  lasketaan summa, tulo ja keskiarvo
let sum = int1 + int2 + int3;
let product = int1 * int2 * int3;
let avg = sum / 3;

//  printataan tulokset
fillInt.innerHTML = `Sum: ${sum}, product: ${product}, average: ${avg}`;
