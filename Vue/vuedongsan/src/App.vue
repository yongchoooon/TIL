<template>

  <div class="black-bg" v-if="modalIO == true">
    <div class="white-bg">
      <h4>상세 페이지임</h4>
      <p>상세 페이지 내용임</p>
      <button @click="modalIO = false">상세 페이지 닫기</button>
    </div>
  </div>

  <div class="menu">
    <a v-for="a in menus" :key="a"> {{ a }}</a><br>
  </div>

  <img alt="Vue logo" src="./assets/logo.png">

  <!-- <div v-for="(room, i) in 3" :key="room">
    <h4>{{ products[i] }}</h4>
    <p>{{ 50 * (i+1)}} 만원</p>
  </div>  -->
  <!-- 반복문 연습과제 -->

  <p>-------</p>
  
  <!-- 모달창, 탭, 햄버거메뉴, 서브메뉴, 툴팁, 이미지슬라이드 등 모든 건 미리 만들어놓고 숨겨놨다가 이벤트 발생시 보이도록 하는 것-->

  <div>
    <img src="./assets/room0.jpg" alt="room0" class="room-img">
    <h4 @click="modalIO = true">{{ products[0] }}</h4>
    <p>50 만원</p>
    <button v-on:click="increase(0)">허위매물 신고</button> <span>신고 수 : {{ reports[0] }}</span>
    <!-- 여기서 v-on: 대신 @로 써도 됨-->
    <!-- click 이외에도 mouseover 등 이벤트 종류가 많음--> 
    <!-- "" 안에 함수명을 넣을 수도 있음 함수는 밑에서 만들어야 함-->
  </div>
  <div>
    <img src="./assets/room1.jpg" alt="room1" class="room-img">
    <h4>{{ products[1] }}</h4>
    <p>60 만원</p>
    <button v-on:click="increase(1)">허위매물 신고</button> <span>신고 수 : {{ reports[1] }}</span>
  </div>
  <div>
    <img src="./assets/room2.jpg" alt="room2" class="room-img">
    <h4>{{ products[2] }}</h4>
    <p>70 만원</p>
    <button v-on:click="increase(2)">허위매물 신고</button> <span>신고 수 : {{ reports[2] }}</span>
  </div>


  <p>--------------------------------------------------------------</p>

  <div v-for="i in 5" :key="i">
    <img :src="onerooms[i].image" class="room-img">
    <h4>{{onerooms[i].title}}</h4>
    <p>{{onerooms[i].price}}원</p>
    <p>{{onerooms[i].content}}</p>
  </div>
</template>

<script>
import data from './assets/oneroom.js';

export default {
  name: 'App',
  data(){
    return {
      onerooms : data,
      modalIO : false,
      reports : [0, 0, 0],
      menus : ['Home', 'Shop', 'About'],
      products : ['역삼동', '천호동', '마포구'],      
    }
  },

  methods : {
    increase(i) {
      this.reports[i] += 1;
    }

  },
  components: {

  }
}
</script>

<style>
body {
  margin: 0;
}
div {
  box-sizing: border-box;
}
.black-bg {
  width: 100%;
  height: 100%;
  background : rgba(0,0,0,0.5);
  position: fixed;
  padding: 20px;
}
.white-bg {
  width: 100%;
  background: white;
  border-radius: 8px;
  padding: 20px;
}

.room-img {
  width: 100%;
  margin-top: 40px;
}
.menu {
  background: blue;
  padding: 15px;
  border-radius: 5px;
}
.menu a {
  color: white;
  padding: 10px;
}

#apple {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
