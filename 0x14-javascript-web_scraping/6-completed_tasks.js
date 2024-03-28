#!/usr/bin/node
const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the provided API URL
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
  const tasks = JSON.parse(body);
  // Initialize an object to store the number of completed tasks for each user ID
  const completedTasksByUserId = {};
  // Iterate through the tasks
  tasks.forEach(task => {
    // Check if the task is completed
    if (task.completed) {
      // Increment the count of completed tasks for the user ID
      if (completedTasksByUserId[task.userId]) {
        completedTasksByUserId[task.userId]++;
      } else {
        completedTasksByUserId[task.userId] = 1;
      }
    }
  });
  // Print the number of completed tasks for each user ID
  console.log(completedTasksByUserId);
});
