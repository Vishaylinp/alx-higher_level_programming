#!/usr/bin/node

const Square0 = require('./5-square.js');

class Square extends Square0 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let x = 0; x < this.height; x++) {
      let row = '';
      for (let y = 0; y < this.width; y++) {
        row += c;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
