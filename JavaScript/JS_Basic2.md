## 2. 콘솔에 출력, script async와 defer의 차이점 및 앞으로의 공부 방향
- API : [link](https://developer.mozilla.org/ko/docs/Web/API)
- 여기서 Console API 참고
- 웹페이지의 검사 -> Console 탭에서 자바스크립트 코드를 작성하고 실행할 수 있음. 동적으로 요소들을 검사하고, 지우고, 작성하는 간단한 기능을 수행하는 데 유용함.
- Source 탭에서 디버깅 가능
- 기본적으로 자바스크립트를 공부할 때 [MDN](https://developer.mozilla.org)에서 참고하는 게 좋다!
- html에서 javascript를 포함하는 방식(async vs defer)
  1. `<head>` 안에 `<script src="main.js">`를 포함
  - 이 경우 웹 브라우저가 html 코드를 parsing 해오다가 parsing을 멈추고 js 파일을 불러오고 끝나면 다시 parsing을 하기 때문에 js 파일의 크기가 클 경우 로딩이 느려질 수 있다는 단점이 있음.
  2. `<body>` 안의 제일 마지막에 `<scirpt src="main.js">`를 포함
  - 이 경우 웹 브라우저가 parsing을 끝낸 다음에 js 파일을 다운받기 때문에 만약 웹 페이지가 javascript에 의존적인 페이지라면 parsing이 끝나고 사용자가 js파일을 fetching하는 시간과 실행하는 시간을 기다려야 한다는 단점이 있음.
  3. `<head>` 안에 `<script asyn src="main.js">`
  - 이 경우 웹 브라우저가 parsing을 하다가 `asyn`을 만나면 js파일을 병렬적으로 fetching을 해오고, fetching이 끝남과 동시에 parsing을 멈추고 js파일을 실행하고, 실행이 끝나면 parsing을 다시 하기 때문에 다운로드 시간을 절약할 수 있다는 장점이 있음
  - 하지만 html이 parsing 되기도 전에 js파일이 실행되기 때문에 아직 정의되지 않은 요소가 있을 수도 있고, js파일을 실행하는 시간동안 parsing을 하지 못하기 때문에 여전히 시간이 더 걸린다는 단점이 있음.
  4. `<head>` 안에 `<script defer src="main.js">`
  - 이 경우 웹 브라우저가 parsing을 하다가 `defer`를 만나면 바로 js파일을 병렬적으로 fetching하고, parsing이 끝나면 js파일을 실행하기 때문에 다운로드 시간을 가장 절약할 수 있다는 장점이 있음.
- `'use strict';` : js 파일을 작성할 때 가장 첫 줄에 이 라인을 적어두는 것을 추천.
  - javascript는 굉장히 유연한 언어이기 때문에 작성자에게 strict하게 작성하도록 요구하여 비상식적인 코딩을 방지하는 역할을 함.
  - ex) 비상식적인 경우 : 그냥 `a=6;`이라고 변수 타입 정의 없이 변수를 정의하면 콘솔창에서 Error가 발생함.

## 3. 데이터 타입, let vs var, hoisting
- `{}` Block scope : 이 안에서 정의된 변수는 안에서만 사용 가능하고 밖에서는 사용할 수 없음. 
- var hoisting : 변수를 어디에서 선언했는지에 상관없이 변수의 선언을 제일 위로 끌어올려주는 것.
1. `var` vs `let`
  - `let`은 read/write가 둘 다 가능.
  - `var`는 변수를 선언하기도 전에 값을 할당할 수 있음.
    ```html
    age = 4;
    var age;
    ```
  - 또한 `var`는 block scope이 없음. local variable의 개념이 없음.
  - 그렇기 때문에 이제는 `var`보다는 `let`만 사용해야 함.
    - `let`은 hoisting이 불가능.
2. Constant (`const`)
  - const는 read only.
  - 값을 한 번 할당하면 절대 바뀌지 않음.
  - 값의 변경이 불가하기 때문에 보안상 유리함.
  - 여러 thread가 동시에 값을 변경시킬 수 없도록 함.
  - 작업자의 실수를 방지할 수 있음.
3. 데이터 타입
  - primitive : single item(number, string, boolean, null, undefined, symbol)
  - object : box container
  - function, first-class function
  1. **primitive**
    - number : 모든 숫자는 다 number 타입. ($-2^{53} ~ 2^{53}$)
      - bigInt : 최근에 추가된 타입. ($-2^{53} ~ 2^{53}$의 범위를 넘어섬)
    - string : 모든 글자는 다 string 타입.
      - `template literals` : 출력할 때 \`\` 안에 ${변수명}을 넣어서 출력할 수 있음. => string을 `+`로 일일이 쪼개지 않아도 되어서 편함
    - boolean : True / False
    - null : 비워져 있는 상태
      - `let nothing = null;`
    - undefined : 변수에 할당이 되지 않은 상태
      - `let x;`
    - symbol : 고유한 식별자
      ```javascript
      const symbol1 = Symbol('id');
      const symbol2 = Symbol('id');
      console.log(symbol1 === symbol2); // False
      ```
      - `Symbol()`은 고유한 식별자를 만들기 때문에 안에 같은 내용을 입력해도 다른 symbol이 됨.
      ```javascript
      const gSymbol1 = Symbol.for('id');
      const gSymbol2 = Symbol.for('id');
      console.log(gSymbol1 === gSymbol2); // true
      ```
      - 같은 string의 symbol로 만들어주기 위해서는 `.for()`을 사용해 선언해주어야 함.
      ```javascript
      console.log(`value : ${symbol1.description}, type: ${typeof symbol1}`);
      ```
      - symbol의 내용을 출력하기 위해선 `.description`을 붙여서 출력해야 함
- Dynamic typing : dynamically typed language
  ```javascript
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
  ```
  2. object
  - container라고 생각하면 쉬움
    ```javascript
    const = ellie = { name : 'ellie', age : 20};
    ellie.age = 21;
    ```
4. Immutable data type vs Mutable data type
  - Immutable data type : primitive types, frozen objects
    - ex) 'ellie'라는 string을 통째로 다른 값으로 바꾸는 건 가능하지만 알파벳 하나만 i를 e로 바꾼다던가 하는 건 안 됨.
  - Mutable data type : all objects by default are mutable
    - 변할 수 있음
    
## 4. 코딩의 기본 operator, if, for loop 코드리뷰 팁
1. Increment and decrement operators
  ```javascript
  let counter = 2;

  const preIncrement = ++counter;
  // counter = counter + 1;
  // preIncrement = counter;
  // 출력 - counter : 3, preIncrement : 3
  const postIncrement = counter++;
  // postIncrement = counter;
  // counter = counter + 1;
  // 출력 - postIncrement : 3, counter : 4
  ```
2. Logical operators : `||` (or), `&&` (and), `!` (not)
- `||` : 전체 중 하나라도 true이기만 하면 true.
  ```javascript
  console.log(`or: ${value1 || value2 || check()}`);
    
  function check() {
    for(let i = 0; i < 10; i++){
      console.log(':fire:');
    }
    return true;
  }
  ```
  - 이 경우 or로 묶인 3개의 변수 중 맨 첫번째가 true이기만 하면 || 연산을 그만두고 무조건 true를 출력하게 됨.
- `&&` : 전체 모두 true여야만 true.
  ```javascript
  const value3 = false;
  console.log(`or: ${value3 && value2 && check()}`);
  ```
  - 이 경우 value3가 false이기 때문에 여기서 연산을 멈추고 false가 출력됨.
3. Equality
  ```javascript
  const stringFive = '5';
  const numberFive = 5;

  // loose equality, type은 같지 않아도 됨
  console.log(stringFive == numberFive); // true
  console.log(stringFive != numberFive); // false

  // strict equality, type까지 같아야 함
  console.log(stringFive === numberFive); // false
  console.log(stringFive !== numberFive); // true
  ```
4. Ternary operator : `?`
- `condition ? value1 : value2;`
- 이건 간단한 조건문일때만 사용
  ```javascript
  name = 'ellie';
  console.log(name === 'ellie' ? 'yes' : 'no');
  ```
5. Switch statement
  ```javascript
  const browser = 'IE';

  switch (browser) {
    case 'IE' :
      console.log('go away!');
      break;
    case 'chrome' :
    case 'firefox' :
      console.log('love you!');
      break;
    default:
      console.log('same all!');
      break;
  }
  ```

## 5. Arrow Function은 무엇인가? 함수의 선언과 표현
