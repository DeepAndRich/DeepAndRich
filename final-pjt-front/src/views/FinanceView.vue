<template>
	<div class="financeBackGround w-11/12 h-screen">
		<button @click="click">데이터 받아오기</button>
		<div
			class="bg-white w-8/12 h-10 drop-shadow-md rounded-md mx-auto flex justify-center items-center"
		>
			<select
				class="mx-2 border-2 border-black rounded-lg h-8"
				v-model="selectedFinance"
			>
				<option value="정기예금">정기예금</option>
				<option value="정기적금">정기적금</option>
			</select>
			<select
				class="mx-2 h-8 border-2 border-black rounded-lg"
				v-model="selectedMonth"
			>
				<option value="6">6개월</option>
				<option value="12">12개월</option>
				<option value="24">24개월</option>
				<option value="36">36개월</option>
			</select>
			<select
				class="mx-2 h-8 border-2 border-black rounded-lg"
				v-model="selectedTax"
			>
				<option value="15.4">일반과세 15.4%</option>
				<option value="9.5">세금우대 9.5%</option>
			</select>
			<input
				class="h-8 border-2 border-black rounded-lg"
				type="text"
				v-model="inputMoney"
				id="inputMoney"
			/>
			<label
				class="h-8 border-2 border-black rounded-lg text-right"
				for="inputMoney"
				>원</label
			>
		</div>
		<div
			class="billBoard bg-black rounded-lg mt-10 p-3"
			v-if="selectedProducts"
		>
			<BillboardTitle :month="selectedMonth" />
			<BillboardList
				:items="selectedProducts"
				:selectedTax="selectedTax"
				:payments="inputMoney"
				:finance="selectedFinance"
			/>
		</div>
		<div v-else>로딩중~</div>
	</div>
</template>

<script>
import BillboardList from '@/components/Finance/BillboardList.vue';
import BillboardTitle from '@/components/Finance/BillboardTitle.vue';
export default {
	name: 'FinanceView',
	components: {
		BillboardList,
		BillboardTitle,
	},
	data() {
		return {
			selectedFinance: '정기예금',
			selectedMonth: '6',
			selectedTax: '15.4',
			inputMoney: '100000',
		};
	},
	computed: {
		selectedProducts() {
			if (this.selectedFinance !== '정기예금') {
				return this.$store.getters.getMainSavings(this.selectedMonth);
			} else {
				return this.$store.getters.getMainDeposit(this.selectedMonth);
			}
		},
	},
	methods: {
		click() {
			console.log(this.selectedProducts);
		},
	},
};
</script>

<style>
.financeBackGround {
	margin: 0 auto;
	/* width: 1278px; */
	/* height: 980px; */
	background-image: linear-gradient(
			rgba(255, 255, 255, 0.3),
			rgba(255, 255, 255, 0.3)
		),
		url('@/assets/img/financeBackground.png');
	background-repeat: no-repeat;
	background-size: cover;
	background-position: center;
	z-index: -2;
}
.billBoard {
	width: 1200px;
	height: 700px;
	margin: 0 auto 0 auto;
	filter: drop-shadow(-4px 4px 4px rgba(0, 0, 0, 0.5));
}
</style>
