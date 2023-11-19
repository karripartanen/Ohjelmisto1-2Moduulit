'use strict';
const fillYear = document.querySelector('.fillYear');

const startYear = parseInt(prompt('Provide the first year'));
const endYear = parseInt(prompt('Provide the last year'));
const ul = document.createElement('ul');
fillYear.append(ul);

for (let i=startYear; i<endYear; i++) {
  if (i % 4 == 0 && i % 100 != 0 || i % 400 == 0) {
    const newLi = document.createElement('li');
    newLi.innerText = `${i} on karkausvuosi`;
    ul.append(newLi);

  }
}
//  poistaa listalta tyylin (bullet points)
ul.style = 'list-style-type: none';
