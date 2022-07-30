<template>
  <div>
    <select name="" id="" v-model="selectedCity"> <!-- v-model은 사용자가 값을 변경할 수 있는 유형의 tag에만 사용 가능 -->
      <option value=""></option>
      <option value="02">서울</option>
      <option value="051">부산</option>
      <option value="064">제주</option>
    </select>
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      selectedCity: '02'
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {}
}
</script>
