<template>
	<div class="exchange flex mx-auto flex-wrap">
		<div class="w-6/12">
			<h1>여기 환율 계산기 넣기</h1>
			<button @click="check">확인용</button>
			<div>
				<select v-model="selectedCountry" name="" id="">
					<option v-for="item in countryList" :key="item.key" :value="item">
						{{ item }}
					</option>
				</select>
			</div>
			<div>
				원화 : <input v-model="inputMoney" type="number" name="" id="" />
			</div>
			<div>환전 : {{ calculatedMoney }}</div>
		</div>
		<div class="w-6/12">
			<h1>여기 환율 계산기 넣기</h1>
			<button @click="check">확인용</button>
			<div>
				<select v-model="selectedCountry" name="" id="">
					<option v-for="item in countryList" :key="item.key" :value="item">
						{{ item }}
					</option>
				</select>
			</div>
			<div>
				원화 : <input v-model="inputMoney" type="number" name="" id="" />
			</div>
			<div>환전 : {{ calculatedMoney }}</div>
		</div>
		<div class="w-full">
			<h1>여기 환율 정보 넣기</h1>
			<div class="flex border-b-2 border-black">
				<div class="w-4/12">화폐코드</div>
				<div class="w-4/12">국가</div>
				<div class="w-4/12">환전비율(1,000원당)</div>
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
			inputMoney: 1000,
			outputMoney: 0,
		};
	},
	created() {
		this.getExchangeInfo();
	},
	computed: {
		calculatedMoney() {
			try {
				const selectedInfo = this.exchangeInfo.find(
					item => item.cur_nm === this.selectedCountry,
				);
				console.log(selectedInfo);
				const selectedExchange = selectedInfo.deal_bas_r.replaceAll(',', '');
				let divideMoney = 1000;
				if (
					this.selectedCountry == '일본 엔' ||
					this.selectedCountry == '인도네시아 루피아'
				) {
					divideMoney = 100;
				}
				console.log(parseFloat(selectedExchange));
				return parseInt(
					(this.inputMoney * parseFloat(selectedExchange)) / divideMoney,
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
	width: 1100px;
}
</style>
