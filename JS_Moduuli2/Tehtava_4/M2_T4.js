//  Write a program that asks the user for numbers until he gives zero.
//  The given numbers are printed in the console from the largest to the smallest.
'use strict'

let num;
const numbers = [];
let i = 0;
while (num != 0) {
  num = +prompt('Provide a number or end the process with a 0: ');
  numbers.push(num);
}

numbers.sort(function(a, b){return b-a});

for (i=0; i<numbers.length; i++) {
  console.log(numbers[i]);
}
