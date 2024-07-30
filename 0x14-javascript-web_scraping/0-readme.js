#!/usr/bin/node

// import 'fs' module
// get filename from an array of commmand line arguments

const fs = require('fs');
const filename = process.argv[2];


fs.readFile(filename, 'utf-8', (error, content) => {
	if (error) {
		console.log(error);
	} else {
		console.log(content);
	}
});
