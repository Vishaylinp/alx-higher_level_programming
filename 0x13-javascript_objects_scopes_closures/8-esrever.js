#!/usr/bin/node

exports.esrever = function (list) {
  const inverse = [];
  for (let x = list.length - 1; x >= 0; x--) {
    inverse.push(list[x]);
  }
  return (inverse);
};
