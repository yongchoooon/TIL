<template>
  <div>
    <input type="text" v-bind:value="userId" readonly />
    <!-- readonly 속성의 input text에는 양방향 데이터바인딩이 필요 없으니까 v-bind:value=""로 해서 단방향만 가능하도록 -->
    <input type="text" :value="userId" readonly />
    <!-- v-bind 는 생략 가능 -->
    <br>
    <img :src="imgSrc" alt="" style="width:100px;height:auto;" />
    <!-- img 태그의 src 속성에도 :를 붙여서 데이터바인딩 가능 -->
    <br>
    <input type="search" name="" id="" v-model="txt1" />
    <button :disabled="txt1 === ''">조회</button>
    <!-- disabled와 같이 true/false로 되는 속성도 조건문을 입력해서 토글 가능 -->
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      userId: 'i dont know',
      imgSrc: 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png',
      txt1: ''
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {}
}
</script>
