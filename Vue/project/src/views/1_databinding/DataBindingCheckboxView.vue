<template>
  <div>
    <div>
      <input type="checkbox" id="html" value="HTML" v-model="favoriteLang" />
      <label for="html">HTML</label>
    </div>
    <div>
      <input type="checkbox" id="css" value="CSS" v-model="favoriteLang" />
      <label for="css">CSS</label>
    </div>
    <div>
      <input type="checkbox" id="js" value="JavaScript" v-model="favoriteLang" />
      <label for="js">JavaScript</label>
    </div>
    <div>
      선택한 지역 : {{ favoriteLang }}
    </div>
    <!-- checkbox는 사용자가 value를 바꿀 수 있는게 check했는지 아닌지 밖에 없기 때문에 그것만 양방향 데이터바인딩이 가능 -->
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      favoriteLang: ['JavaScript']
      // checkbox는 여러개를 선택할 수 있기 때문에 반드시 배열로 선언해야한다
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {}
}
</script>
