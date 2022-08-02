<template>
  <v-app>
    <v-content>
      <PleaseCal />
    </v-content>
  </v-app>
</template>

<script>
import PleaseCal from './components/PleaseCal.vue'

export default {
  name: 'App',

  components: {
    PleaseCal,
  },

  data: () => ({
    //
  }),
};
</script>
