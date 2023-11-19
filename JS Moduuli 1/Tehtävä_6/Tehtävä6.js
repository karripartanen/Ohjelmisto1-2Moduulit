'use strict';
let fillSqrt = document.querySelector('.fillSqrt');

const answer = confirm('Should I calculate the square root?');

if (answer) {
  const num = parseFloat(prompt('Provide a number: '));
  if (num >= 0) {
    const sqrt = Math.sqrt(num)
    fillSqrt.innerHTML = `The square root of ${num} is ${sqrt}.`;
  } else {
    fillSqrt.innerHTML = "That's not a positive number.";
  }
} else {
  fillSqrt.innerHTML = 'The square root is not calculated.';
}
