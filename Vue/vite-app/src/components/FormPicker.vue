<template>
  <DatePicker
    v-model="date"
    color="red"
    title-position="left"
   />
  <p>
    Date : {{ date.toJSON() }}
  </p>
  <v-date-picker v-model="date" />
</template>

<script setup>
import { ref } from 'vue'
import { DatePicker } from 'v-calendar'
import 'v-calendar/dist/style.css'

const date = ref(new Date())
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
