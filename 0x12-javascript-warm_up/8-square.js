#!/usr/bin/node

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  const num = Number(process.argv[2]);
  for (let x = 0; x < num; x++) {
    console.log('x'.repeat(num));
  }
}
