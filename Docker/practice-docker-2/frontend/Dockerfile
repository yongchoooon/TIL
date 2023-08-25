FROM node:12.18.4

RUN npm install -g http-server 

WORKDIR /home/node/app

CMD ["http-server", "-p", "8081", "./public"]

# 이미지 생성 명령어 (현 파일과 같은 디렉토리에서)
# docker build -t {이미지명} .

# 컨테이너 생성 & 실행 명령어
# docker run --name {컨테이너명} -v $(pwd):/home/node/app -p 8080:8080 {이미지명}