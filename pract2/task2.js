const express = require('express');

console.log(`Express version: ${require('express/package.json').version}`);

console.log(`Express path: ${require.resolve('express')}`);

console.log(`Express description: ${require('express/package.json').description}`);

// npm info express

// git clone https://github.com/expressjs/express.git

// cd express
// npm install