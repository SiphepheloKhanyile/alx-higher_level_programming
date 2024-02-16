#!/usr/bin/node
exports.converter = function (base) {
  return function convertToBaseN (number) {
    if (number === 0) {
      return '';
    } else {
      return convertToBaseN(Math.floor(number / base)) + '0123456789abcdef'[number % base];
    }
  };
};
