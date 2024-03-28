#!/usr/bin/node
const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// Define the URL for the Star Wars API endpoint
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
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
  const film = JSON.parse(body);
  // Extract and print the title of the movie
  console.log(film.title);
});
