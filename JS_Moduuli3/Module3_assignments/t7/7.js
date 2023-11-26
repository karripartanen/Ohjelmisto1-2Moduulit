'use strict';
const trigger = document.querySelector('#trigger');
const target = document.querySelector('#target');

function mousesOver() {
  target.src = 'img/picB.jpg';
}


function mousesAway() {
  target.src = 'img/picA.jpg';
}
trigger.addEventListener('mouseover', mousesOver);
trigger.addEventListener('mouseout', mousesAway);
