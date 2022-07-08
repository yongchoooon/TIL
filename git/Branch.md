# 1. Branch (분기된 가지, 다른 차원)
- 프로젝트를 하나 이상의 모습으로 관리해야 할 때
    - 예) 실배포용, 테스트 서버용, 새로운 시도용
- 여러 작업들이 각각 독립되어 진행될 때
    - 예) 신기능 1, 신기능 2, 코드 개선, 긴급수정
    - 각각의 차원에서 작업한 뒤 확정된 것을 메인 차원에 통합
```bash
이 모든 것을 하나의 프로젝트 폴더에서 진행될 수 있도록 함
```

# 2. 명령어
- Branch 생성
    - `git branch (이름)`
- Branch 목록 확인
    - `git branch`
- Branch 이동
    - `git switch (이름)`
- Branch 생성과 동시에 이동하기
    - `git switch -c (이름)`
- Branch 삭제
    - `git branch -d (이름)`
- Branch 이름 변경
    - `git branch -m (기존 브랜치명) (새 브랜치명)`

# 3. 각각의 브랜치에서 서로 다른 작업해보기
- main 브랜치에서 작업한 후 변경사항을 add & commit 하고 나서
- 새로운 브랜치 git_test로 switch하고 다른 작업을 진행한 후 변경사항을 add & commit하면
- 이는 즉 다른 각각의 branch에서 진행된 것이므로 branch를 switch할 때마다 파일의 내용이 바뀌어서 나타나게 됨.
- 각기 다른 branch 상에서 파일을 생성하거나 삭제했을 경우에도 진행상황이 해당 branch에서만 국한되게 기록됨
- `git log`를 통해 각기 다른 branch에서의 변경사항을 확인할 수 있고, 소스트리에서도 직관적으로 확인 가능
- git bash에서 시각적으로 확인하는 방법
    - `git log --all --decorate --oneline --graph`

# 4. Branch를 합치는 2가지 방법
## 1) Merge
<img src="./pics/branch_merge.JPG" title="branch_merge">

- 병합의 개념
- 초록색 Branch와 파란색 Branch의 두 가지를 하나로 이어 붙이는 것.
- Merge 이전의 branch들의 History가 다 남음.
1. git_test 브랜치를 main 브랜치로 merge
2. **main 브랜치에서** 아래 명령어를 입력
    - `git merge git_test`
    - :bulb: `merge`는 `reset`으로 되돌리기 가능
        - `merge`도 하나의 커밋이기 때문에 이전으로 `merge`하기 이전 해당 브랜치의 마지막 시점으로 되돌리기 가능
3. 병합된 브랜치는 삭제
    - `git branch -d git_test`
## 2) Rebase
<img src="./pics/branch_rebase.JPG" title="branch_rebase">

- Branch의 마디(commit)들을 대상 Branch로 옮겨붙이는 것.
- History가 깔끔하게 한 줄로 정리됨.
1. git_test2 브랜치를 main 브랜치로 rebase
2. **git_test2 브랜치에서** 아래 명령어를 입력
    - :bangbang: `merge` 때와는 반대
    - `git rebase main`
3. main 브랜치로 이동 후 아래 명령어로 git_test2 시점으로 `fast-forward`
    - `git merge git_test2`

# 5. 충돌 해결하기
## 브랜치 간 충돌
- 파일과 같은 위치에 다른 내용이 입력된 상황
## 1) `merge` 충돌 해결
- main 브랜치에서 `git merge conflict_1`을 입력하여 conflict_1 브랜치와 병합을 시도하면 충돌이 발생
    - 이 경우 VS code에서 여러 브랜치 중 하나의 브랜치의 내용을 선택할 수도 있고, 모두 선택할 수도 있음
    - 당장 충돌이 해결이 어려운 경우 아래 명령어로 `merge` 중단 가능
        - `git merge --abort`
    - 해결 가능 시 충돌 부분을 수정한 뒤 `git add .`, `git commit`으로 병합 완료
- conflict_1 브랜치 삭제
    
## 2) `rebase` 충돌 해결
- conflict_2 브랜치에서 `git rebase main`을 입력하여 main 브랜치와 병합을 시도하면 충돌이 발생
    - 이 경우에도 마찬가지로 브랜치들의 변경사항 중 선택하면 됨
    - 당장 충돌이 해결이 어려운 경우 아래 명령어로 `merge` 중단 가능
        - `git merge --abort`
    - 해결 가능 시 : 충돌 부분을 수정한 후 `git add .`, 아래 명령어로 계속
        - `git rebase --continue`
        - 충돌이 모두 해결될 때 까지 반복
    - main 브랜치에서 `git merge conflict_2`로 마무리
- conflict_2 브랜치 삭제