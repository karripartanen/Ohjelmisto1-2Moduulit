'use strict';

const search = document.querySelector('#query');
const btn = document.querySelector('input[type="submit"]');  // "btn" = button

async function searchFunction(input) {
  try {
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${input}`);
    console.log(response);
  } catch (error) {  // unexpected error handling
    console.log(error.message);
  }
}


btn.addEventListener('click', (event) => {
  event.preventDefault();
  const query = search.value;
  searchFunction(query);
})
