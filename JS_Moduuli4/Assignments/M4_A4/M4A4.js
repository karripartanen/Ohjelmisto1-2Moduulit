'use strict';

const search = document.querySelector('#query');
const btn = document.querySelector('input[type="submit"]');
const targetELem = document.querySelector('#result');
let showData

btn.addEventListener('click', async function (event) {
  event.preventDefault();
  const query = search.value;
  showData = await searchData(query);
  targetELem.innerHTML = '';
  createArticle(showData);
})

async function searchData(input) {
  let jsonData;
  try {
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${input}`);
    jsonData = await response.json()
    return jsonData;
  } catch (error) {
    console.log(error.message);
    return null;
  }
}

function createArticle(data) {
  for (let tv of data) {
    const article = document.createElement('article');
        const header = document.createElement('h2');
        const link = document.createElement('a');
        const image = document.createElement('img');
        const summary = document.createElement('div');
        header.textContent = tv.show.name;
        article.appendChild(header);
        image.src = tv.show.image ? tv.show.image?.medium : 'https://via.placeholder.com/210x295?text=Not%20Found';
        image.alt = tv.show.name;
        article.appendChild(image);
        link.href = tv.show.url;
        link.textContent = tv.show.url;
        link.target = "_blank"
        article.appendChild(link);
        summary.innerHTML = tv.show.summary;
        article.appendChild(summary);
        targetELem.appendChild(article);
  }
}