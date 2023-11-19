//  Write a program that asks the user for the number of participants.
//  After this, the program asks for the names of all participants.
//  Finally, the program prints the names of the participants on the web page in an
//  ordered list (<ol>) in alphabetical order.

'use strict';

let fillParticipants = document.querySelector('.fillParticipants');
const ol = document.createElement('ol');
fillParticipants.append(ol);

let i = 0;  // iterator for loops
let personCount = 0;
let participants = [];
let participant = '';
personCount = +prompt("Enter the number of participants you'd like to enter: ");

for (i=0; i<personCount; i++) {
  participant = prompt('Provide the name of a participant: ');
  participants.push(participant);
}
participants.sort()

for (i=0; i<personCount; i++) {
  const newLi = document.createElement('li');
  newLi.innerText = `${participants[i]}`;
  ol.append(newLi);
}

ol.style = 'list-style-type: none';