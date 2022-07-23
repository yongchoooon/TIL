# API
- Application Programming Interface
- Front-End와 Back-End를 잇는 개념
- Front-End가 Back-End에 요청(request)을 할 때 갖춰야 하는 사용 규칙을 의미함.
- Open API : Back-End의 주소와 사용 규칙을 공개한 것을 의미함.
  - 공공데이터포털, 네이버, 카카오 등 많음.

## API 가이드
- API 가이드에 따라 Front-End가 Back-End에 요청(request)을 하면 Back-End가 Front-End에 응답(response)을 해주는 방식.
- 요청(request)
  - 주소 (ex) https://dapi.kakao.com/v3/search/book)
  - 전송방식 (GET or POST)
    - GET : 주소창에 모든 정보를 담아 정보를 전달하는 방식
    - POST : 주소창이 아니라 내부적으로 정보를 담아 전달하는 방식
  - 보낼 것
    - ex)
    - query 검색어(필수)
    - sort 정렬 방식 (선택)
    - target 검색 대상 (선택)
- 응답 (response)
  - 형식 (ex) JSON)
  - 응답 의미 설명
    - ex)
    - title 도서 제목
    - contents 도서 소개 
    - ...
- :bulb: **JSON**
  - JSON : JavaScript Object Notation
  - 정보 전송에 많이 사용되는 방식으로, python의 dict type과 유사한 형식을 갖춤.
  ```Javascript
  {
    name : "홍길동";,
    age : 25,
    sex : "male",
    family : {father : "홍판서", mother : "춘섬"},
    hoppy : ["농구", "도술"]
  }
  ```

