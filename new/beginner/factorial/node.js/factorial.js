var library = require('./library');

var number = process.argv[2];
var factorial = library.factorial(number);

console.log(number + '! = ' + factorial);