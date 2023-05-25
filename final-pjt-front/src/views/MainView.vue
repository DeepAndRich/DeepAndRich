<template>
	<div class="mainPage mx-auto">
		<div class="mainContainer flex">
			<div class="w-3/12 flex justify-center">
				<TestComponentVue name="정기예금 순위" :list="getDepositArray" />
			</div>
			<div class="w-3/12 flex justify-center">
				<TestComponentVue name="정기적금 순위" :list="getSavingArray" />
			</div>
			<div class="w-3/12 flex justify-center">
				<!-- <TestComponentVue /> -->
			</div>
			<div class="w-3/12 flex justify-center">
				<!-- <TestComponentVue /> -->
			</div>
		</div>
		<!-- {{ getDepositArray }} -->
		<div class="mainBtmContainer">
			<button>추천알고르즘으로 가기</button>
		</div>
	</div>
</template>

<script>
import TestComponentVue from '@/components/Main/TestComponent.vue';
import axios from 'axios';

export default {
	name: 'MainView',
	components: {
		TestComponentVue,
	},
	data() {
		return {
			depositArray: [],
			savingArray: [],
			articlesArray: [],
		};
	},
	created() {
		axios
			.get(`http://127.0.0.1:8000/savings/saving-products/12/`)
			.then(res => {
				console.log(res);
				// console.log(month);
				console.log(this.$store.state.MainSavings);
				this.savingArray = res.data;
			})
			.catch(err => {
				console.log(err);
			});
		axios
			.get(`http://127.0.0.1:8000/deposits/deposit-products/12/`)
			.then(res => {
				this.depositArray = res.data;
			})
			.catch(err => {
				console.log(err);
			});
	},
	computed: {
		getDepositArray() {
			console.log(this.depositArray, '??');
			return this.depositArray.slice(0, 7);
		},
		getSavingArray() {
			return this.savingArray.slice(0, 7);
		},
	},
	methods: {},
};
</script>

<style>
.mainPage {
	width: 1250px;
	height: 1000px;
	background-image: linear-gradient(
			rgba(255, 255, 255, 0.3),
			rgba(255, 255, 255, 0.3)
		),
		url('@/assets/img/mainBackground.png');
	background-repeat: no-repeat;
	background-size: cover;
	background-position: top;
	z-index: -2;
}
.mainContainer {
	margin: 0 auto;
	width: 1250px;
	height: 650px;
}
.mainBtmContainer {
	margin: 0 auto;
	width: 1200px;
	height: 350px;
	background-color: #fff;
	box-shadow: -8px 8px 4px rgba(0, 0, 0, 0.25);
	border-radius: 28px;
}
</style>
