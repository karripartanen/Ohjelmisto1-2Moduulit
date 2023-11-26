'use strict';
const num1 = document.querySelector('#num1');
const num2 = document.querySelector('#num2');
const userSelection = document.querySelector('#operation');
const result = document.querySelector('#result');
const btn = document.querySelector('#start');

function calc() {
  const value1 = parseFloat(num1.value);  // change user input from string to float
  const value2 = parseFloat(num2.value);
  switch (userSelection.value) {
    case 'multi':
      result.innerHTML = `${value1 * value2}`;
      break;

    case 'div':
      result.innerHTML = `${value1 / value2}`;
      break;

    case 'add':
      result.innerHTML = `${value1 + value2}`;
      break;

    case 'sub':
      result.innerHTML = `${value1 - value2}`;
      break;
  }
}
btn.addEventListener('click', calc);