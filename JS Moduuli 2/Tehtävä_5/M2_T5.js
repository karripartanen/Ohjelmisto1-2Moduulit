//  Write a program that prompts the user for numbers. When the user enters one of the numbers he
//  previously entered, the program will announce that the number has already been given and stops its
//  operation and then prints all the given numbers to the console in ascending order.

'use strict';

let num;
const numbers = [];
let i = 0  // iterator
let game = true;

while (true) {
  num = +prompt('Provide a number: ')
  if (!isNaN(num)) {
    if (numbers.includes(num)) {
      console.log(`Number ${num} has already been given. Stopping operation.`);
      break;
    } else {
      numbers.push(num);
    }
  } else {
    console.log('Invalid input');
  }
}

numbers.sort(function(a, b){return a-b});
for (i=0; i<numbers.length; i++) {
  console.log(numbers[i]);
}
