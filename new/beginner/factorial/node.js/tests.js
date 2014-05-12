var assert = require('assert');
var library = require('./library');

describe('Factorial', function () {
  it('should return 1 when value is 1', function () {
    assert.equal(1, library.factorial(1));
  });

  it('should return 2 when value is 2', function () {
    assert.equal(2, library.factorial(2));
  });

  it('should return 6 when value is 3', function () {
    assert.equal(6, library.factorial(3));
  });

  it('should return 120 when value is 5', function () {
    assert.equal(120, library.factorial(5));
  });
});