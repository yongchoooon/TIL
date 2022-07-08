# 1. Github
```bash
Git으로 관리하는 프로젝트의 원격 저장소
```

# 2. 원격 저장소 사용하기
1. Github에서 로컬 PC의 폴더명과 같은 이름의 Repository 생성
2. `git remote add origin (원격 저장소 주소)`
    - 로컬의 Git 저장소에 원격 저장소로의 연결 추가
    - 원격 저장소의 이름이 흔히 `remote` 사용. 다른 것으로 수정 가능
3. `git branch -M main`
    - Github 권장 : 기본 브랜치명을 `main`으로
4. `git push -u origin main`
    - 로컬 저장소의 커밋 내역을 원격으로 `push`(업로드)
        - `-u` 또는 `--set-upstream` : 현재 브랜치와 명시된 원격 브랜치 기본 연결
    - `git remote`를 입력하면 원격 저장소의 내용 확인 가능

# 3. Github에서 프로젝트 다운받기
1. `Download ZIP` : 파일들만 다운받음, Git 관리내역 제외
2. `git clone` : 프로젝트의 파일들 뿐만 아니라 Git의 관리내역까지 로컬 PC로 복사
    - 터미널이나 Git Bash에서 대상 폴더로 이동 후
    - `git clone (원격 저장소 주소)`

# 4. Push와 Pull
## 1) 원격으로 커밋 밀어올리기(push)
- `git push` 명령어로 push
    - 이미 `git push -u origin main`으로 대상 원격 브랜치가 지정되었기 때문에 `git push`만으로도 가능
- Github 페이지에서 확인