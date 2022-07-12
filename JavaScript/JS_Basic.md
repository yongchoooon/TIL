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
- [ex18.html](./exercise/ex18.html)에서, 
  - `document.querySelector('#night_day')`는 `<input>` tag 자기 자신을 가리키고 있기 때문에 `this`를 사용할 수 있음
    - 그렇게 되면 `id`는 필요없어지기 때문에 제거 가능
  - `document.querySelector('body')`는 중복이 4번이나 되기 때문에 다른 변수로 치환하여 사용 가능
    - `var target = document.querySelector('body');`


### 20. 배열
- 배열에 원소를 추가할 때는 `push()` method 사용
```html
<script>
  var coworkers = ['AAA', 'BBB'];

  coworkers.push('CCC');
</script>
```

### 21. 반복문
```html
<script>
  var i = 0;
  while(i < 3) {
    document.write('<li>1</li>');
    document.write('<li>2</li>');
    i = i + 1;
  }
</script>
```
=> 1과 2로 이루어진 리스트가 3번 출력됨

## 22. 배열과 반복문
- [ex22.html](./exercise/ex22.html)

## 23. 배열과 반복문의 활용
- [ex23.html](./exercise/ex23.html)
- `querySelector()`는 가장 첫 번째 element만을 가져오기 때문에 해당하는 element를 모두 가져오기 위해서는 `querySelectorAll()`를 사용하면 됨.

## 24. 함수
- [ex24.html](./exercise/ex24.html)
- `<head>` tag 내에 `function` 으로 함수를 정의해주고, `<body>` tag 내에서 그 함수를 사용.

## 29. 객체
- [ex29.html](./exercise/ex29.html) : [ex24.html](./exercise/ex24.html)의 코드의 내용을 `LinksSetColor()`, `BodySetColor()`, `BodySetBackgroundColor()`의 3개 함수로 만들어 코드를 수정했다.
- 이러한 방법도 가능하지만 이 경우 함수의 이름이 계속해서 길어질 수 있다는 문제점이 있기 때문에 아쉬움이 있다.
- `BodySetBackgroundColor()`를 `Body`라는 객체의 `SetBackgroundColor()`라는 method를 이용하도록 할 수도 있다.
- ex) `document.querySelector()`에서 `document`는 객체, `querySelector()`는 method이다. 
  - 여기서 method는 함수인데, 객체 내의 함수는 method라고 한다.

## 30. 객체 쓰기와 읽기
- 배열을 생성할때는 `[]`로 생성하지만, 객체는 `{}`로 생성한다.
  - ***약간 파이썬의 `dict`와 비슷한 듯***
- 객체에는 반드시 `"programmer" : "egoing"`처럼 key : value의 형태로 데이터의 이름을 붙여서 입력해 주어야 함.
- 객체에 새로운 데이터를 추가할 때는
  - `coworkers.bookkeeper = "duru";`
- 새로 추가할 데이터에 띄어쓰기가 있다면
  - `coworkers["data scientist"] = "taeho";`
- [ex30.html](./exercise/ex30.html)

## 31. 객체와 반복문
```html
<script>
  for(var key in coworkers) {
    // 여기에 반복문 작성
  }
</script>
```
- [ex31.html](./exercise/ex31.html)

## 32. 객체 프로퍼티와 메소드
- 함수를 정의할 때는,
  - `function showAll() {}` 이렇게 해도 되지만
  - `showAll = function() {}` 이렇게 해도 됨.
- 이렇게 `coworkers`라는 객체 내에 `showAll()`이라는 함수를 정의하고자 할 때, `coworkers.showAll() = function() {}` 이렇게 할 건데
- 이 경우 함수 안에서 해당 함수가 소속되어 있는 객체를 가리키는 약속된 기호가 바로 `this`이다.
- 따라서 함수 내에서 `coworkers` 대신 `this`라고 써도 된다는 것이다.
  - 이렇게 하면 객체의 이름이 바뀌어도 함수 자신이 속한 객체를 가리키게 되어 활용성이 높다.  
- 객체 내의 함수는 `method`라고 하고, 객체 내의 변수는 `Property`라고 부른다.

## 33. 객체의 활용
- [ex33.html](./exercise/ex33.html)
- `LinksSetColor()`라는 함수를 `Links`라는 객체의 `SetColor()` method로 구현함.

## 34. 파일로 쪼개서 정리 정돈하기
- [colors.js](./exercise/colors.js)
- [ex34.html](./exercise/ex34.html)
- `<script>` 안에 있던 내용들을 별도로 js파일을 만들어서 저장하고, html 파일의 `<head>` 내의 `<script>` 에는 `<script src="colors.js">`의 형식으로 사용하면 편리함.
- 이렇게 하면 `colors.js` 파일의 내용만 바꾸면 많은 html 파일의 color를 한 번에 바꿀 수 있어 좋음.
- 웹페이지의 `검사` 창의 `Network` 탭을 보면 이 페이지를 불러오기 위해 어떤 파일들을 download했는지 알 수 있는데, `colors.js`도 포함되어 있는 것을 알 수 있음. 
- :bulb: 이런 방식을 사용하면 좋은 점
  - 웹서버 입장에서는 페이지를 로드하기 위해 다운로드를 두 번 해야하는 번거로움이 있지만, 
  - 한 번 웹 브라우저에 다운로드된 `colors.js`와 같은 파일은 웹 브라우저가 저장(cache)하고 있다.
  - 그래서 다음에 다시 이 페이지에 접속할 때, 저장된 파일을 가지고 로드하기 때문에 서버 입장에서도 비용을 절감할 수 있고, 사용자 입장에서도 적은 트래픽으로 페이지를 로드할 수 있기 때문에 빠른 로딩이 가능하다.
  - 그렇기 때문에 이렇게 파일로 쪼개서 정리하는 방식은 다운로드를 두 번 해야하는 번거롭다는 단점이 있긴 하지만 효율적인 관리와 로딩이 가능하다는 더 큰 이점이 있다고 할 수 있다.

## 35. 라이브러리와 프레임워크
- 라이브러리(Library) : 단순 활용 가능한 도구들의 집합.
  - 개발자가 만든 클래스에서 호출하여 사용
  - 클래스들의 나열로 필요한 클래스를 불러서 사용하는 방식을 취하고 있음.
  - ex) **jQuery**
- 프레임워크(Framework) : 소프트웨어의 특정 문제를 해결하기 위해서 상호 협력하는 클래스와 인터페이스의 집합.
  - 완성된 어플리케이션이 아니기 때문에 프로그래머가 완성시키는 작업을 해야 함.
  - 특정 개념들의 추상화를 제공하는 여러 클래스나 컴포넌트로 구성되어 있음.
 
- jQuery : [link](https://jquery.com/download/)에서 다운받을 수 있음.
  - CDN : Contetn Delivery Network
    - 라이브러리를 가져와 사용할 때 로컬에 다운로드해서 사용할 수도 있고, 웹 주소를 입력해도 되는데, 여기서 웹 주소를 입력하는 것이 CDN.
    - [Google CDN](https://developers.google.com/speed/libraries#jquery)의 `jQuery 3.x snippet`의 코드를 [ex35.html](./exercise/ex35.html)의 `<head>` 에 삽입
    ```html
    var Links = {
      SetColor : function (color) {
        // var alist = document.querySelectorAll('a');
        // var i = 0;
        // while(i < alist.length) {
        //   alist[i].style.color = color;
        //   i = i + 1;
        //   }
        $('a').css('color', color);
      }
    }
    ```
    - `$('a')` : 모든 `<a>` tag는 jQuery로 제어하겠다는 의미.
    - `.css()` : css에 대한 제어 (다른 방법은 필요할 때마다 찾기)
    - 위 코드에서 알 수 있듯이 jQuery를 사용하면 매우 간단하게 코드를 짤 수 있음. 
- [ex35.html](./exercise/ex35.html)
- [colors_googlecdn.js](./exercise/colors_googlecdn.js)
