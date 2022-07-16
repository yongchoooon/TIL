## 5. 서버접속
- Bitnami에서 설치한 MariaDB(MySQL)의 bin 폴더 주소에서 cmd창에 `mysql -uroot -p`를 입력하고 password를 입력하면 MariaDB에 접속 가능
- 여기서 `root`는 사용자 이름
  - `root`는 서버 관리자로, 모든 권한을 가지고 있음. 
- `-p`는 비밀번호 입력을 위한 옵션

## 6. 스키마의 사용
- `CREATE DATABASE opentutorials;` : DATABASE 생성
- `SHOW DATABASES;` : 현재 존재하는 DATABASE 확인
- `USE opentutorials;` : 데이터베이스 사용

## 8.1 테이블의 생성
- column의 데이터 타입을 강제할 수 있다. 
  - [link](https://www.w3schools.com/sql/sql_datatypes.asp)
- `NOT NULL` : 공백 허용하지 않음
- `AUTO_INCREMENT` : 자동으로 숫자가 커짐

## 9. CRUD
- CREATE, READ, UPDATE, DELETE

## 10. INSERT
- `DESC table;` : table의 description을 확인 가능
- `INSERT INTO table(title, description) VALUES('MySQL', 'MySQL is ...');` : table의 columns에 value들을 넣어서 row 삽입
- `SELECT * FROM table;` : table의 모든 행 출력
- `NOW()` : 현재 시각 리턴

## 11. SELECT
- [MySQL SELECT Statement](https://dev.mysql.com/doc/refman/8.0/en/select.html)
- `SELECT col1, co2, col3 FROM table;` : table에서 col1, col2, col3의 모든 row를 출력
- `WHERE` : 조건문 
  - ex) `WHERE author='egoing';`
- `ORDER BY` : 정렬
  - `DESC`, `ASC`
  - ex) `ORDER BY id DESC;`
- `LIMIT` : 출력하는 행의 최대 갯수 제약
  - ex) `SELECT * FROM table LIMIT 2;`

## 12. UPDATE
- [MySQL UPDATE Statement](https://dev.mysql.com/doc/refman/8.0/en/update.html)
- ex) `UPDATE table SET col2='Oracle is ...', col1='Oracle' WHERE id=2;`

## 13. DELETE
- [MySQL DELETE Statement](https://dev.mysql.com/doc/refman/8.0/en/delete.html)
- ex) `DELETE FROM table WHERE id=5;`
- `WHERE`가 중요함. 없이 실행시키면 모든 행이 다 삭제됨.

## 15. 관계형 데이터베이스의 필요성
- 테이블을 여러 개로 나눠서 테이블간의 관계로 데이터베이스를 정의할 수 있음.
  - 장점 : 중복을 제거할 수 있고, 유지보수를 용이하게 할 수 있음.
  - 단점 : 직관적으로 이해하기 어려움.

## 17. JOIN
- ex) `SELECT * FROM topic LEFT JOIN author ON topic.author_id = author.id;`
  - 이렇게 하면 중복되는 column이 있을 수 있음.
  - 그래서 `SELECT *`가 아니라 `SELECT id, title, description,...` 이렇게 하면 됨
  - 근데 이렇게 하면 왼쪽 table과 오른쪽 table에 `id`라는 같은 column을 가지고 있을 수도 있음.
  - 그래서 `topic.id` or `author.id` 이렇게 하면 됨
  - `SELECT topic.id, title, description, name, profile FROM topic LEFT JOIN author ON topic.author_id = author.id;`
    - 이 때 `topic.id`라는 이름을 `topic.id AS topic_id`라는 코드를 통해 이름을 변경해서 출력해줄 수 있음.
