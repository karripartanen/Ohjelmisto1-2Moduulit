'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];
const targetElem = document.querySelector('#target');
for (let student of students) {
  let option = document.createElement('option');
  let idAttr = document.createAttribute('value');
  let name = document.createTextNode(student.name);
  idAttr.value = student.id;
  option.setAttributeNode(idAttr);
  option.appendChild(name);
  targetElem.appendChild(option);
}

