#!/usr/bin/node
// import module fs to write a file
const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  }
});
