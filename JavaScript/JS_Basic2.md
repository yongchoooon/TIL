## 2. 콘솔에 출력, script async와 defer의 차이점 및 앞으로의 공부 방향
- API : [link](https://developer.mozilla.org/ko/docs/Web/API)
- 여기서 Console API 참고
- 웹페이지의 검사 -> Console 탭에서 자바스크립트 코드를 작성하고 실행할 수 있음. 동적으로 요소들을 검사하고, 지우고, 작성하는 간단한 기능을 수행하는 데 유용함.
- Source 탭에서 디버깅 가능
- 기본적으로 자바스크립트를 공부할 때 [MDN](https://developer.mozilla.org)에서 참고하는 게 좋다!
  ### html에서 javascript를 포함하는 방식(async vs defer)
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