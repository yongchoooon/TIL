<template>
  <div>
    <div>
      <select name="" id="">
        <option value=""></option>
        <option :value="city.code" v-for="city in cities" :key="city.code">
          {{city.title}}
          </option>
        <!-- key에는 항상 유일한 값이 와야 함 -->
      </select>
    </div>
    <div>
      <table>
        <thead>
          <tr>
            <th>제품번호</th>
            <th>제품명</th>
            <th>가격</th>
            <th>주문수량</th>
            <th>합계</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="drink in drinkList" :key="drink.drinkID">
          <!-- 내가 가진 데이터에 key로 쓸만한 게 없다면-->
          <!-- v-for에 반복되는 걸 ()로 감싸고 (drink, index) 로 하면 자동으로 unique한 숫자 차례로 생성되고 key를 index로 하면 됨-->
            <td>{{ drink.drinkID }}</td>
            <td>{{ drink.drinkName }}</td>
            <td>{{ drink.price }}</td>
            <td><input type="number" v-model="drink.qty"></td>
            <td>{{ drink.price * drink.qty }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      cities: [
        { title: '서울', code: '02' },
        { title: '부산', code: '051' },
        { title: '제주', code: '064' }
      ],
      drinkList: [
        {
          drinkID: '1',
          drinkName: '코카콜라',
          price: 700,
          qty: 1
        },
        {
          drinkID: '2',
          drinkName: '오렌지주스',
          price: 1200,
          qty: 1
        },
        {
          drinkID: '3',
          drinkName: '커피',
          price: 500,
          qty: 1
        },
        {
          drinkID: '4',
          drinkName: '물',
          price: 700,
          qty: 1
        },
        {
          drinkID: '5',
          drinkName: '보리차',
          price: 1200,
          qty: 1
        }
      ]
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {}
}
</script>
