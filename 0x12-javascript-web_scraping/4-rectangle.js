#!/usr/bin/node
/* this keyword refers to the current
object the code is being written inside */
exports.Rectangle = function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
  this.rotate = function () {
    let temp = 0;
    temp = this.height;
    this.height = this.width;
    this.width = temp;
  };
  this.double = function () {
    this.height = (this.height * 2);
    this.width = (this.width * 2);
  };
  this.print = function () {
    let res = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        res += 'X';
      }
      console.log(res);
      res = '';
    }
  };
};
