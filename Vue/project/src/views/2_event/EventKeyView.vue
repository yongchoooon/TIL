<template>
  <div>
    <!-- <input type="search" name="" id="" @keyup="checkEnter($event)" v-model="searchText"> -->
    <input type="search" name="" id="" @keyup.ctrl.enter="doSearch" v-model="searchText">
    <button @click="doSearch">조회</button>
    <button type="sumbit" @click.prevent="doSearch">prevent</button>
  </div>
</template>
<script>
// @keyup 다음에
// .enter .tab .delete .esc .space .up .down .left .right 등 많은 키에 대해서 눌러졌는지 확인 가능
// .ctrl.enter 처럼 두개 눌렀는지도 가능
// .stop : event.stopPropagation()의 역할을 함
// .prevent : event.preventDefault()
export default {
  components: {},
  data() {
    return {
      searchText: ''
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {
    doSearch() {
      console.log(this.searchText)
    },
    checkEnter(event) {
      if (event.keyCode === 13) {
        this.doSearch()
      }
    }
  }
}
</script>
