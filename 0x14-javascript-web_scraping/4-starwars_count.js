#!/usr/bin/node
const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Character ID for "Wedge Antilles"
const characterId = 18;

// Make a GET request to the Star Wars API endpoint for films
request.get(apiUrl, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }
    if (response.statusCode !== 200) {
        console.error(`Error: Status code ${response.statusCode}`);
        return;
    }
    // Parse the JSON response
    const films = JSON.parse(body).results;
    // Filter the films where "Wedge Antilles" is present
    const filmsWithWedgeAntilles = films.filter(film => {
        return film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`);
    });
    // Print the number of films where "Wedge Antilles" is present
    console.log(filmsWithWedgeAntilles.length);
});
