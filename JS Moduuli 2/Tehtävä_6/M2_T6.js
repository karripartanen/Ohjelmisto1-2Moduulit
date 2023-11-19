//  Write a function that returns a random dice roll between 1 and 6. The function should
//  not have any parameters. Write a main program that rolls the dice until the result is 6.
//  The main program should print out the result of each roll in an unordered list (<ul>).

'use strict';
let fillDice = document.querySelector('.fillDice');


function rollDice() {
  return Math.floor(Math.random()*6)+1;
}

// Main program to roll the dice until the result is 6
function main() {
  const ul = document.createElement('ul');
  ul.style = 'list-style-type: none';
  fillDice.append(ul)

  let roll;
  let count = 0;

  do {
    roll = rollDice();
    count++;

    const newLi = document.createElement('li');
    newLi.textContent = `Roll ${count}: ${roll}`;
    ul.append(newLi);
  } while (roll !== 6);

}

// Run the main program
main();



