#!/usr/bin/node
exports.logMe = function (item) {
  if (!logMe.counter) {
    logMe.counter = 0;
  }
  console.log(logMe.counter + ': ' + item);
  logMe.counter++;
};
