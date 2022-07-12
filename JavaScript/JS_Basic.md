# JavaScript
- 웹페이지가 사용자와 동적으로 상호작용할 수 있도록 하기 위해 만들어 진 언어.
---

### 4. 이벤트 (Event)
- 웹페이지 내에서 마우스를 클릭하거나 키를 입력했을 때, 특정 요소에 포커스가 이동되었을 때 등 어떤 사건을 발생시키는 것.
- ex) click, mouseover, keydown, focus, change, load, scroll 등
- 사용자가 실제 이벤트를 발생시켰을 때 그 이벤트데 대응하여 처리하는 것을 `이벤트 핸들러`라고 함
  - `<input>` tag 내의 `onclick`, `onchange` 속성 등을 의미함.

### 6. 데이터 타입 - 문자열과 숫자
> Boolean, Null, Undefined, Number, BigInt, String, Symbol
- 아래 모든 내용은 웹페이지의 Console 창에서 입력한 것
  - `'aaaa'.length` : `'aaaa'`의 길이 출력 (4) - Properties
  - `'aaaa'.toUpperCase()` : `'aaaa'`를 대문자로 만들어서 출력 - Method
  - `'aaaa'.indexOf('b')` : () 안의 내용이 `'aaaa'`의 문자열 중 몇 번째부터 시작하는지 출력 - Method
    - 문자열에 없는 내용일 때는 `-1` 출력
  - `'    aaa   '.trim()` : 문자열 양 쪽의 공백 제거 - Method

### 8. 웹브라우저 제어
- [ex8.html](./exercise/ex8.html)

### 12. 제어할 태그 선택하기
- CSS 선택자는 크게 tag selector, class selector, id selector가 있음.
- `document.querySelector(selectors);` : 제공한 selector(선택자) 또는 선택자 그룹과 일치하는 문서 내 첫 번째 `element`를 반환함
  - `var el = document.querySelector("body");`
  - `var el = document.querySelector(".myclass");`
  - `var el = document.querySelector("#myid");`
- 이렇게 선택한 element의 style을 제어하기 위해서는
  - `document.querySelector("body").style.backgroundColor = 'black';`
  - 이렇게 하면 `<body>` tag의 style이 변경됨.
- [ex8.html](./exercise/ex8.html)

### 13. 프로그램
- HTML은 프로그래밍 언어라고는 하지 않음.
- 프로그램 : '순서'대로 실행되어야 한다는 점을 내포하고 있음.
- 그러나 HTML은 작업자가 작성한 내용에 대해 순서에 상관없이 웹페이지를 출력하는 일을 하는 언어이므로 프로그래밍 언어라고 할 수 없음. 
- HTML은 MarkUp 언어라고 함.
- 반면에 JavaScript는 웹페이지에서 사용자와 동적으로 상호작용하기 위한 목적을 가지고 있기 때문에, 순서가 중요하다. 따라서 JavaScript는 프로그래밍 언어라고 할 수 있다.

### 14. 조건문
- 앞서 실습한 night, day 버튼을 toggle 기능을 가지도록 한 button으로 나타낼 수 있음.
- if문을 사용해서 현재 mode가 day라면 night로 바꾸고, night라면 day로 mode를 바꾸는 형식.

### 15. 비교 연산자와 불리언
- `1===2` : 여기서 `===`는 비교 연산자로, 좌항과 우항의 관계에 따라서 True / False를 출력하는 연산자
- 여기서 True / False를 Boolean 타입이라고 함.
- [ex15.html](./exercise/ex15.html)

### 16. 조건문
```html
<script>
  if() {

  } else {

  }
</script>
```
- [ex16.html](./exercise/ex16.html)

### 17. 조건문의 활용
-  if문을 사용해서 현재 button의 value가 day라면 night로 바꾸고, night라면 day로 바꾸는 형식.
- 이 때 button의 value를 가져오기 위해서는
  - `document.querySelector('#night_day').value`
- 이게 'night'인지 아닌지 알아보기 위해서는
  - `document.querySelector('#night_day').value === 'night`
- [ex17.html](./exercise/ex17.html)

### 18. 리팩토링 중복의 제거
- Refactoring : 결과의 변경 없이 코드의 구조를 재조정함을 뜻함. 가독성을 높이고 유지보수를 편하게 하는 작업. 외부화면은 그대로 두면서 내부 논리나 구조를 바꾸고 개선하는 유지보수 행위.