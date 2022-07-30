<template>
  <div>
    <div :class="{ 'text-red': hasError , active: isActive }">클래스 바인딩</div>
    <!-- class명에 - 이 들어가면 ''로 반드시 묶어줘야 하는데 안 들어가면 안 묶어줘도 됨 -->
    <!-- 적용되는 class에 따라 켜고 끄고 할 수 있음 -->
    <div :class="class2">클래스 바인딩2</div>
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      isActive: false,
      hasError: false,
      class2: ['active', 'text-red']
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {}
}
</script>
<style scoped>
  .active {
    background-color: greenyellow;
    font-weight: bold;
  }
  .text-red {
    color: red;
  }
</style>
