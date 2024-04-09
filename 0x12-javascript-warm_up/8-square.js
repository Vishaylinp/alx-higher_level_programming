#!/usr/bin/node

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let x = 0; x < parseInt(process.argv[2]); x++) {
    let row = '';
    for (let y = 0; y < parseInt(process.argv[2]); y++) {
      row += 'x';
    }
    console.log(row);
  }
}
