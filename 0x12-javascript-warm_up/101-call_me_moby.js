#!/usr/bin/node

exports.callMeMoby = function (num, theFunction) {
  while (num > 0) {
    theFunction();
    num--;
  }
};
