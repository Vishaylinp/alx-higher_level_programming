#!/usr/bin/node

function factorial (Val) {
  if (isNaN(Val) || Val === 1) {
    return (1);
  } else {
    return (Val * factorial(Val - 1));
  }
}
console.log(factorial(process.argv[2]));
