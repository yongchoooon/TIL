# 1.  Git 최초 설정
- Git 전역으로 사용자 이름과 이메일 주소를 설정
- Github 계정과는 별개
    - `git config --global user.name "(본인 이름)"`
    - `git config --global user.email "(본인 이메일)"`
- 이후에 아래의 명령어들로 확인
    - `git config --global user.name`
    - `git config --global user.email`

- 기본 브랜치명 변경
    - `git config --global init.defaultBranch main`

# 2. 프로젝트 생성 & Git 관리 시작
- 적당한 위치에 원하는 이름으로 폴더를 생성하고 VS Code로 열람
- 해당 폴더에서 아래 명령어 입력
    - `git init` : 맨 처음에 git을 사용하기 위해서 초기화를 해 주겠다는 뜻
- 폴더에 숨김모드로 `.git` 폴더 생성 확인
    - 이 폴더를 지우면 Git 관리 내역이 삭제되니 조심
- 현재 폴더의 상황을 확인하기 위해서는 아래 명령어 입력
    - `git status` : 파일의 추가, 변경, 삭제 모든 내역을 확인할 수 있음

# 3. Git에게 맡기지 않을 것들
- 포함할 필요가 없거나 보안상 포함하지 말아야 할 때
    - `.gitignore`파일을 사용해서 배제할 요소들 지정 가능
- gitignore 작성법은 필요할 때마다 찾아서 보자!

# 4. 프로젝트의 변경사항들을 타임캡슐(버전)에 담기
- 추적하지 않는(untracked)파일 : Git의 관리에 들어간 적 없는 파일
    - `git status`를 통해 확인 가능
        
- 파일을 캡슐에 담기(스테이징)
    - `git add (filename)`
    - `git add .` : 모든 파일 담기

# 5. 타임캡슐 묻기 (commit)
- 아래 명령어로 commit
    - `git commit`
- Vim 입력 모드로 진입
    - 입력 시작 : `i`
    - 입력 종료 : `esc`
    - 저장 없이 종료 : `:q`
    - 저장 없이 강제 종료 : `:q!`
    - 저장하고 종료 : `:wq`
- commit message 입력한 뒤 저장하고 종료해야 commit이 완료됨
- 아래의 명령어를 통해서도 commit 가능 (자주 사용됨)
    - `git commit -m "(commit message)"`
- 아래 명령어로 확인
    - `git log`
- :star: tip : add와 commit을 한꺼번에
    - `git commit -am "(메세지)"`
    - 단, 새로 추가된(untracked) 파일이 없을 때에만 한정 

# 6. 하던 작업을 임시로 저장해두고 싶을 때
- `git stash` : 아직 마무리하지 않은 작업을 스택에 잠시 저장할 수 있도록 함. 이를 통해 아직 완료하지 않은 일을 commit하지 않고 나중에 다시 꺼내와 마무리할 수 있다. (`git stash save`로도 가능)
1. `stash`란 아래에 해당하는 파일들을 **보관해두는 장소**이다.
    - Modified이면서 Tracked 상태인 파일
        - Tracked : 과거에 이미 commit하여 스냅샷에 넣어진 관리 대상 상태의 파일
        - Tracked 상태인 파일을 수정한 경우
    - Staged 상태의 파일
        - `git add` 명령을 실행한 경우

2. stash 목록 확인하기
    - `git stash list`

3. stash 적용하기 (했던 작업을 다시 가져오기)
    - `git stash apply`
    - `git stash apple (stash 이름)`
    - :bulb: 이 경우 staged 상태였던 파일을 자동으로 staged 상태로 만들어주지는 않는다. 그래서 아래와 같이 index 옵션을 주어야 staged 상태까지 복원한다.
        - `git stash apply --index`
        
4. stash 제거하기 
    - `git stash drop`
    - `git stash drop (stash 이름)`
    - :bulb: 만약 적용과 동시에 스택에서 stash를 제거하고 싶으면
        - `git stash pop`

5. stash 되돌리기
    - `git stash show -p` or `git apply -R`
    - `git stash show -p (stash 이름)` or `git apply -R`