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

## 2) 원격의 커밋 당겨오기(pull)
- Github 페이지에서 파일 변경 이후
- `git pull` 명령어로 pull
- 로컬에서 파일과 로그 확인

## 3) Pull 해야할 내용이 있는데 Push 해야할 경우
- 공동 작업자가 이미 Push한 내용이 Github에 저장되어 있고
- 본인이 그 내용을 Pull 해야하는 데, 
- 본인의 로컬 PC에서 작업한 사항도 Push 해야할 경우
1. `git push`를 해보면, 원격 저장소에 먼저 적용된 최신 버전이 있으므로 적용이 불가함.
    - pull을 먼저 해서 원격의 버전을 받아온 다음 push를 해야 함
2. Pull하는 2가지 방법
    1. merge 방식 : `git pull --no-rebase`
    2. rebase 방식 : `git pull -rebase`
3. Push 하기

## 4) 로컬의 내역 강제 Push
- 강제로 Push할 경우 원격 저장소에 Push 되어있는 공동 작업자의 작업 내용이 날아갈 수도 있으므로 협의된 상황이 아니라면 협업 시에는 유의해야 함.
- `git push --force`

# 5. 원격의 브랜치 다루기
## 1) 로컬에서 브랜치 만들어 원격에 Push 해보기
1. 로컬에서 from-local 이라는 이름의 브랜치를 생성하고 `git push`를 하면
    - 원격의 브랜치 명시 및 기본설정을 요구하는 메세지가 나옴.
2. 그래서 `git push -u origin from-local`을 해줘야 함.
3. Github에서 브랜치 목록을 확인
4. 로컬에서 브랜치 목록을 확인
    - `git branch --all` or `git branch -a` : 로컬의 브랜치와 원격 저장소의 브랜치 목록 모두 확인 가능

## 2) 원격의 브랜치 로컬로 받아오기
1. Github의 main 브랜치에서 분기해서 from-remote라는 브랜치를 생성
    - 이 상태에서 `git branch -a`를 입력해도 업데이트가 되지 않음
2. `git fetch` 입력
    - `git branch -a`로 확인
3. `git switch -t origin/from-remote` : 로컬에 같은 이름의 브랜치를 생성하여 연결하고 switch
    - 여기서 `-t`는 원격의 브랜치를 로컬로 복사한 이후에 앞으로도 계속 로컬의 from-remote 브랜치는 원격의 from-remote 브랜치와 연결하겠다는 의미

## 3) 원격의 브랜치 삭제
- `git push (원격 이름) --delete (원격의 브랜치명)`
    - 위의 예시로 보면 `git push origin --delete from-remote`
    - `git branch -a`로 확인