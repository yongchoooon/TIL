<template>
  <div>
    <div>
      <input type="radio" id="html" value="HTML" v-model="favoriteLang" />
      <label for="html">HTML</label>
    </div>
    <div>
      <input type="radio" id="css" value="CSS" v-model="favoriteLang" />
      <label for="css">CSS</label>
    </div>
    <div>
      <input type="radio" id="js" value="JavaScript" v-model="favoriteLang" />
      <label for="js">JavaScript</label>
    </div>
    <div>
      선택한 지역 : {{ favoriteLang }}
    </div>
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      favoriteLang: 'JavaScript'
      // radio는 하나만 선택할 수 있기 때문에 문자열 형태로 선언해야 한다
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {}
}
</script>
