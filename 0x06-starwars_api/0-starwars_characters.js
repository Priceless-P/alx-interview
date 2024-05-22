#!/usr/local/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

function fetchMovieDetails (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }
      if (response.statusCode !== 200) {
        reject(new Error('Could not retrieve movie detials'));
        return;
      }
      const film = JSON.parse(body);
      resolve(film.characters);
    });
  });
}

function fetchCharacterDetails (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }
      if (response.statusCode !== 200) {
        reject(new Error('Could not fetch Character'));
        return;
      }
      const character = JSON.parse(body);
      resolve(character.name);
    });
  });
}

fetchMovieDetails(url)
  .then((character) => {
    const characterPromise = character.map((characterURL) =>
      fetchCharacterDetails(characterURL));
    return Promise.all(characterPromise);
  })
  .then((characterName) => {
    characterName.forEach((name) => console.log(name));
  })
  .catch((error) => {
    console.error('Error:', error);
  });
