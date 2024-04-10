#!/usr/bin/node

function Secondlargest (args) {
  if (args.length === 0) {
    console.log(0);
  } else if (args.length === 1) {
    console.log(0);
  } else {
    let Max1 = -Infinity;
    let Max2 = -Infinity;
    let curr;

    for (let x = 0; x < args.length; x++) {
      curr = Number(args[x]);
      if (curr > Max1) {
        Max2 = Max1;
        Max1 = curr;
      } else if (curr > Max2 && curr !== Max1) {
        Max2 = curr;
      }
    }
    console.log(Max2);
  }
}
Secondlargest(process.argv.slice(2));
