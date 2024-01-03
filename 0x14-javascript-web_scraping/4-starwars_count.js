#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
        const filmsData = JSON.parse(body).results;
        const moviesWithWedgeAntilles = filmsData.filter((film) =>
            film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
        );

        console.log(moviesWithWedgeAntilles.length);
    } else {
        console.error(error);
    }
});
