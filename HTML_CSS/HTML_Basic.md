# HTML : HyperText Markup Language

## 1. 기본문법
- Tag : HTML 요소(element)라고도 부르며, HTML 문서를 구성하는 기본 단위
    - ex) `<strong>`, `</strong>`, `<p>`, `</p>`, `<br>` 등
- 속성(attribute) : HTML 요소 유형의 수정자(modifier)이다. 태그의 동작을 제어하기 위해 여는 태그 안에 사용되는 특수 용어이다.
    - ex) `<a href=""></a>` 에서 `href`

## 2. 태그의 중첩과 목록
- `<ul>` : 순서가 없는 리스트 만들기 (unordered list)
- `<ol>` : 숫자로 된 리스트 만들기 (ordered list)
- `<li>` : 리스트 만들기 (list)

## 3. 문서의 구조
- `<html>` : 문서의 범위를 설정 (`<head>`와 `<body>`를 감싸는 태그)
- `<head>` : 문서의 정보를 설정
- `<body>` : 문서의 구조를 설정
- `<!DOCTYPE html>`(Document type declaration) : 자신이 작성한 HTML 코드가 어떤 방식으로 작성되었는지를 알려주는 태그. HTML5로 접어들면서 방식이 단일화되었기 때문에 그냥 HTML 코드를 작성할 때 맨 처음에 쓰면 됨.

## 5. Tag
- `<p>` : paragraph. 단락. 기본적으로 `<p></p>` 다음에는 한 줄을 띄움
- `<br>` : a forced linebreak. 줄바꿈. `<p>`와는 다르게 다음에 한 줄을 띄우지 않음. 더 띄우고 싶으면 `<br>`을 두 번 쓰면 됨.
- `<img>` : 이미지 삽입.
    - `alt` 속성 : alternative text의 약자. 이미지가 깨졌거나 사용할 수 없을 때 표시되는 텍스트.
- `<table>` : 표. border 속성으로 경계선 표시 가능. 꾸미는 건 CSS로.
    - `<th>` : table header
    - `<tr>` : table row
    - `<td>` : table data
    - `<thead>`, `<tbody>`, `<tfoot>` : table row들의 위치를 명시
    - `rowspan="2"` : 행 2개만큼을 병합 (병합되는 행에는 `<td></td>`를 지워줌)
    - `colspan="3"` : 열 3개만큼을 병합 (병합되는 열에는 `<td></td>`를 지워줌)

## 6. Form

