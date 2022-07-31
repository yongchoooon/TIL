<template>
  <v-calendar />
  <v-date-picker v-model="date" />
</template>
<script>
import { ref } from 'vue'

export default {
  components: {},
  data() {
    return {
      date : ref(new Date())
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {}
}
</script>
