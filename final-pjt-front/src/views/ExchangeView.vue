<template>
	<div class="exchange flex mx-auto flex-wrap justify-center">
		<div class="w-5/12 flex flex-wrap p-8 border-2 border-black rounded-lg m-4">
			<h1 class="w-full">원화 -> {{ selectedCountry2 }}</h1>
			<div class="my-2 w-full">
				<select v-model="selectedCountry" name="" id="">
					<option v-for="item in countryList" :key="item.key" :value="item">
						{{ item }}
					</option>
				</select>
			</div>
			<div class="w-full my-2">
				원화 :
				<input class="pl-2" v-model="inputOther" type="number" name="" id="" />
			</div>
			<div class="w-full my-2">
				환전 : {{ calculatedKRW }} {{ selectedCountry }}
			</div>
		</div>
		<div class="w-5/12 flex flex-wrap p-8 border-2 border-black rounded-lg m-4">
			<h1 class="w-full">{{ selectedCountry }} -> 원화</h1>
			<div class="w-full">
				<select v-model="selectedCountry2" name="" id="">
					<option v-for="item in countryList" :key="item.key" :value="item">
						{{ item }}
					</option>
				</select>
			</div>
			<div class="w-full">
				{{ selectedCountry2 }} :
				<input class="pl-2" v-model="inputMoney" type="number" name="" id="" />
			</div>
			<div class="w-full">환전 : {{ calculatedMoney }} 원</div>
		</div>
		<div class="w-full">
			<span class="text-2xl mt-4">환율 정보</span>
			<div class="flex border-b-2 border-black">
				<div class="w-4/12">화폐코드</div>
				<div class="w-4/12">국가</div>
				<div class="w-4/12">환전비율</div>
			</div>
			<div class="flex" v-for="item in exchangeInfo" :key="item.key">
				<div class="w-4/12">
					{{ item.cur_unit }}
				</div>
				<div class="w-4/12">
					{{ item.cur_nm }}
				</div>
				<div class="w-4/12">
					{{ item.deal_bas_r }}
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
const URL = 'http://127.0.0.1:8000/exchange/view-exchange-rate/';
export default {
	name: 'ExchangeView',
	data() {
		return {
			exchangeInfo: null,
			countryList: [],
			selectedCountry: '미국 달러',
			selectedCountry2: '미국 달러',
			inputMoney: 1000,
			inputOther: 1000,
			outputMoney: 0,
		};
	},
	created() {
		this.getExchangeInfo();
	},
	computed: {
		calculatedKRW() {
			try {
				const selectedInfo = this.exchangeInfo.find(
					item => item.cur_nm === this.selectedCountry,
				);
				console.log(selectedInfo);
				const selectedExchange = selectedInfo.deal_bas_r.replaceAll(',', '');
				let divideMoney = 1;
				if (
					this.selectedCountry == '일본 엔' ||
					this.selectedCountry == '인도네시아 루피아'
				) {
					divideMoney = 10;
				}
				console.log(parseFloat(selectedExchange));
				return (
					(this.inputMoney / parseFloat(selectedExchange)) *
					divideMoney
				).toFixed(2);
			} catch (e) {
				console.log('아직 로딩이 되지 않음');
				return 0;
			}
		},
		calculatedMoney() {
			try {
				const selectedInfo = this.exchangeInfo.find(
					item => item.cur_nm === this.selectedCountry2,
				);
				console.log(selectedInfo);
				const selectedExchange = selectedInfo.deal_bas_r.replaceAll(',', '');
				let divideMoney = 1;
				if (
					this.selectedCountry2 == '일본 옌' ||
					this.selectedCountry2 == '인도네시아 루피아'
				) {
					divideMoney = 100;
				}
				console.log(parseFloat(selectedExchange));
				return parseInt(
					(this.inputOther * parseFloat(selectedExchange)) / divideMoney,
				);
			} catch (e) {
				console.log('아직 로딩이 되지 않음');
				return 0;
			}
		},
	},
	methods: {
		check() {
			console.log(this.exchangeInfo);
		},
		getExchangeInfo() {
			axios
				.get(URL)
				.then(res => {
					console.log(res);
					this.exchangeInfo = res.data;
					this.getCountryList(this.exchangeInfo);
				})
				.catch(err => {
					console.log(err);
				});
		},
		getCountryList(data) {
			const array = data.map(item => item.cur_nm);
			this.countryList = array;
		},
	},
};
</script>

<style>
.exchange {
	width: 900px;
}
.exchange input {
	border: 2px solid black;
	border-radius: 8px;
}
.exchange select {
	border: 2px solid black;
	border-radius: 8px;
}
.exchange h1 {
	font-size: 1.5rem;
}
</style>
