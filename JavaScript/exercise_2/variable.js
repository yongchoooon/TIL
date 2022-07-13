// string
const char = 'c';
const brandan = 'brandan';
const greeting = 'hello ' + brandon;

console.log(`value: ${greeting}, type: ${typeof greeting}`);

const helloBob = 'hi ${brandan}!'; // template literals (string)

console.log(`value: ${helloBob} + type: ${typeof helloBob}`);
console.log('value: ' + helloBob + ' type: ' + typeof helloBob);

// symbol 
const symbol1 = Symbol('id');
const symbol2 = Symbol('id');
console.log(symbol1 === symbol2); // False

const gSymbol1 = Symbol.for('id');
const gSymbol2 = Symbol.for('id');
console.log(gSymbol1 === gSymbol2); // true

console.log(`value : ${symbol1}, type: ${typeof symbol1}`); // Error
console.log(`value : ${symbol1.description}, type: ${typeof symbol1}`); // 제대로 출력

// dynamic typing
let text = 'hello';
console.log(text.charAt(0)); // h

console.log(`value : ${text}, type : ${typeof text}`);
// value : hello, type : string
text = 1; 
console.log(`value : ${text}, type : ${typeof text}`);
// value : 1, type : nubmer
text = '7' + 5;
console.log(`value : ${text}, type : ${typeof text}`);
// value : 75, type : string
text = '8' / '2';
console.log(`value : ${text}, type : ${typeof text}`);
// value : 4, type : nubmer

console.log(text.charAt(0)); // Error