var fs = require('fs');

// //readFileSync
// // 출력 : ABC
// console.log('A');
// var result = fs.readFileSync('syntax/sample.txt', 'utf8');
// console.log(result);
// console.log('C');


// readFile
// 출력 : ACB
console.log('A');
fs.readFile('syntax/sample.txt', 'utf8', function(err, result) {
  console.log(result);
});
console.log('C');
