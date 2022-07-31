<template>
  <div>
    <select name="" id="" @change="changeCity" v-model="selectedCity">
      <!-- 여기서 @change="changeCity($event)" 로 해서 이벤트를 파라미터로 보낼 수도 있음. 함수 정의할 때도 파라미터 정의 필요-->
      <option value="">==도시선택==</option>
      <option :value="city.cityCode" :key="city.cityCode" v-for="city in cityList">
        {{ city.title }}
      </option>
    </select>
    <select name="" id="">
      <option :value="dong.dongCode" :key="dong.dongCode" v-for="dong in selectedDongList">
        {{ dong.dongTitle }}
      </option>
    </select>
    <!-- <select name="" id="">
      <option :value="dong.dongCode" :key="dong.dongCode" v-for="dong in dongList.filter(dong => dong.cityCode === selectedCity)">
        {{ dong.dongTitle }}
      </option>
    </select> -->
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      selectedCity: '',
      cityList: [
        { cityCode: '02', title: '서울' },
        { cityCode: '051', title: '부산' },
        { cityCode: '064', title: '제주' }
      ],
      dongList: [
        { cityCode: '02', dongCode: '1', dongTitle: '서울1동' },
        { cityCode: '02', dongCode: '2', dongTitle: '서울2동' },
        { cityCode: '02', dongCode: '3', dongTitle: '서울3동' },
        { cityCode: '02', dongCode: '4', dongTitle: '서울4동' },
        { cityCode: '051', dongCode: '1', dongTitle: '부산1동' },
        { cityCode: '051', dongCode: '2', dongTitle: '부산2동' },
        { cityCode: '051', dongCode: '3', dongTitle: '부산3동' },
        { cityCode: '064', dongCode: '1', dongTitle: '제주1동' },
        { cityCode: '064', dongCode: '2', dongTitle: '제주2동' }
      ],
      selectedDongList: []
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {
    changeCity() {
      this.selectedDongList = this.dongList.filter(dong => dong.cityCode === this.selectedCity)
    }
  }
}
</script>
