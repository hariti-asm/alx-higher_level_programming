#!/usr/bin/node
// import module fs to read a file

const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
