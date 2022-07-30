<template>
  <div>
    <input type="text" v-model="userId"/>
    <!-- v-model이 input text에 기본 입력값으로 채워짐, 근데 script에서 가져옴, 양방향 데이터바인딩 가능-->
    <!-- placeholder와는 느낌이 약간 다름 -->
    <button @click="myFunction">클릭</button>
    <button @click="changeData">변경</button>
    <br>
    <input type="text" v-model="num1"/> + <input type="text" v-model="num2"/> = <span>{{ num1 + num2 }}</span>
    <!-- input type text 에 들어가는 value는 무조건 문자열로 들어감.-->
    <br>
    <input type="text" v-model.number="num3"/> + <input type="text" v-model.number="num4"/> = <span>{{ num3 + num4 }}</span>
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      userId: 'i dont know',
      num1: 0,
      num2: 0,
      num3: 0,
      num4: 0
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {
    myFunction() {
      console.log(this.userId)
    },
    changeData() {
      this.userId = 'Jeremy'
    }
  }
}
</script>
