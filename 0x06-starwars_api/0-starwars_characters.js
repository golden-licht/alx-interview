#!/usr/bin/node
const request = require('request');

const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const data = JSON.parse(body);
    const characters = data.characters;

    const characterPromises = characters.map(characterUrl => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch(err => console.error('Error fetching character names:', err));
  }
});
