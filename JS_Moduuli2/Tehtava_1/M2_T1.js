'use strict';

let numbers = [];  //  array for the numbers
let i
let number = 0;


for (i=0; i<5; i++) {
  number = parseInt(prompt('Provide a number: '));
  numbers.push(number);
}

for (i=4; i>=0; i--) {
  console.log(numbers[i]);
}
