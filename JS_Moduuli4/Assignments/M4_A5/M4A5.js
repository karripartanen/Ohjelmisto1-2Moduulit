'use strict';


async function getJoke() {
  let jokeContent;
  try {
    const response = await fetch('https://api.chucknorris.io/jokes/random');
    const joke = await response.json()
    console.log('Joke: ', joke);
    jokeContent = joke.value;
  }
  catch (error) {
    console.log('fetch error', error)
    const joke = {};
    jokeContent = 'Joke not found';
  }
  console.log(jokeContent);
}
getJoke()
