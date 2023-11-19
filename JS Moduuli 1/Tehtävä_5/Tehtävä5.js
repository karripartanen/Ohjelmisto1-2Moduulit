'use strict';
let fillLeapYear = document.querySelector('#fillLeapYear');

let year = parseInt(prompt("Enter a year"));
let answer = '';

if ((year % 4 == 0) && (year % 100 != 0) || (year % 400 == 0)) {
   fillLeapYear.innerHTML = `Year ${year} is a leap year!`;
} else {
   fillLeapYear.innerHTML = `Year ${year} is not a leap year!`;
}
