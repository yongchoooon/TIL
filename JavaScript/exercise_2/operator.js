// Increment and decrement operators
let counter = 2;

const preIncrement = ++counter;
// counter = counter + 1;
// preIncrement = counter;

const postIncrement = counter++;
// postIncrement = counter;
// counter = counter + 1;

// Logical opertors
const value1 = true;
const value2 = 4 < 2;

console.log(`or: ${value1 || value2 || check()}`);
  // 이 경우 or로 묶인 3개의 변수 중 맨 첫번째가 true이기만 하면 || 연산을 그만두고 무조건 true를 출력하게 됨.
  
function check() {
  for(let i = 0; i < 10; i++){
    console.log(':fire:');
  }
  return true;
}

// Equality
const stringFive = '5';
const numberFive = 5;

// loose equality, with type conversion
console.log(stringFive == numberFive); // true
console.log(stringFive != numberFive); // false

// strict equality, no type conversion
console.log(stringFive === numberFive); // false
console.log(stringFive !== numberFive); // true
