//  Write a program that rolls user defined number of dice and displays the sum
//  of the results of the dice rolls.(2p)
// First, program asks the user for the number of dice rolls.
// Then the program throws a die as many times as the user defined.
// Print the sum of the results in the console or in the HTML document.


'use strict';
let fillDice = document.querySelector('.fillDice');

let diceCount = 0;  //  käyttäjän antama määrä heitetyille nopille
let diceSum = 0;  //  noppien summa
let randDice = 0;  // tallettaa satunnaisen silmäluvun nopan heitosta
let i = 1;  //  iteraattori

function getRandomInt(max) {
  return Math.floor(Math.random() * max)+1;
}

diceCount = +prompt("Kuinka monta noppaa haluat heittää? ");
while (i <= diceCount) {
  randDice = getRandomInt(6);
  diceSum += randDice;
  i++;
} fillDice.innerHTML = `Heitit ${diceCount} noppaa,
                        joiden silmälukujen summa on ${diceSum}`;

