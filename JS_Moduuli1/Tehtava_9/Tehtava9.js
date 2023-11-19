//  Write a program that asks the user for an integer and tells if the number is a prime number. (2p)
// Prime numbers are numbers that are only divisible by 1 and itself.
// For example, number 13 is a prime number as it can only be divided by 1 or 13 so that the result
// is an integer.
// On the other hand, number 21 for example is not a prime number
// as it can be also be divided by numbers 3 and 7.
// Print the result on the HTML document.





'use strict';
let fillPrime = document.querySelector('.fillPrime');
const numbers = [2, 3, 5, 7];
let num = parseInt(prompt('Provide a number: '));

function primeNum(num) {
  if (num <= 1) {
    return `${num} is NOT a prime number`;
  }
  else if ((num == 2) || (num == 3))
  {
    return `${num} IS a prime number`;
  }
  for (const i of numbers) {
    if (num % i == 0) {
      return `${num} is NOT a prime number`;
    }
  }
  return `${num} IS a prime number`;
}

if (!isNaN(num)) {
  fillPrime.innerHTML = primeNum(num);
} else {
  fillPrime.innerHTML = 'Invalid input';
}



