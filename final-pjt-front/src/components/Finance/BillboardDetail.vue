<template>
	<div class="billBoardDetail text-xl p-4 mx-auto items-center flex flex-wrap">
		<div class="w-full text-center">상품 상세 정보</div>
		<div class="w-3/12">은행:</div>
		<div class="w-9/12">{{ item.fin_prdt_cd.kor_co_nm }}</div>
		<div class="w-3/12">상품명:</div>
		<div class="w-9/12">{{ item.fin_prdt_cd.fin_prdt_nm }}</div>
		<div class="w-3/12">우대금리:</div>
		<div class="w-9/12">{{ item.intr_rate2 }}</div>
		<div class="w-3/12">금리:</div>
		<div class="w-9/12">{{ item.intr_rate }}</div>
		<div class="w-3/12">이자:</div>
		<div class="w-9/12">{{ item.intr_rate_type_nm }}</div>
		<div class="w-3/12">만기</div>
		<div class="w-9/12">{{ item.save_trm }}개월</div>

		<div v-if="checkUser" class="w-full flex items-center justify-center">
			<button
				v-if="checkProducts"
				@click="check"
				class="subscribeProduct hover:bg-sky-300"
			>
				상품 가입
			</button>
			<button v-else @click="check" class="subscribeProduct hover:bg-sky-300">
				가입 취소
			</button>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
const BASE_URL = 'http://127.0.0.1:8000/accounts/';
const DEPOSIT_URL = 'save-deposit-myproduct/';
const SAVING_URL = 'save-saving-myproduct/';

export default {
	name: 'BillboardDetail',
	components: {},
	props: {
		item: Object,
		finance: String,
	},
	data() {
		return {
			user: JSON.parse(this.$store.getters.getUser),
			userToken: localStorage.getItem('token'),
			financeKind: '',
			URL: '',
			HavingProducts: this.$store.getters.getHavingProducts,
			productCheck: false,
		};
	},
	computed: {
		checkUser() {
			console.log(this.item);
			return this.user;
		},
		checkProducts() {
			let dummy = false;
			this.HavingProducts.forEach(item => {
				if (item.fin_prdt_nm == this.item.fin_prdt_cd.fin_prdt_nm) {
					dummy = true;
				}
			});
			return dummy;
		},
	},
	methods: {
		check() {
			if (this.finance == '정기예금') {
				this.URL = BASE_URL + DEPOSIT_URL + this.item.fin_prdt_cd.id + '/';
			} else {
				this.URL = BASE_URL + SAVING_URL + this.item.fin_prdt_cd.id + '/';
			}
			axios
				.post(this.URL, null, {
					headers: {
						Authorization: `Token ${this.userToken}`,
					},
				})
				.then(res => {
					console.log(res);
					this.getProducts();
					this.$emit('product-modified');
				})
				.catch(err => {
					console.log(err);
				});
		},
		getProducts() {
			axios
				.get(BASE_URL + this.user.pk + '/myproduct/')
				.then(res => {
					console.log(res);
					this.$store.commit('setHavingProducts', res.data);
				})
				.catch(err => {
					console.log(err);
				});
		},
		// checkProducts() {
		// 	console.log(this.HavingProducts, '설마');
		// 	this.HavingProducts.forEach(item => {
		// 		if (item.fin_prdt_nm == this.item.fin_prdt_nm) {
		// 			console.log(item, '??');
		// 			this.productCheck = true;
		// 		}
		// 	});
		// 	console.log(this.productCheck, '???');
		// },
	},
};
</script>

<style>
.billBoardDetail {
	position: fixed;
	left: 50%;
	top: 50%;
	transform: translate(-50%, -50%);

	width: 400px;
	height: 500px;
	border: 1.5px solid black;
	border-radius: 10px;
	backdrop-filter: (0, 0, 4px, #fff);
	background-color: #fff;
	z-index: 2000;
}
.subscribeProduct {
	width: 350px;
	height: 44px;
	border-radius: 5px;
	color: #fff;
	font-size: 20px;
	background-color: #38bdf8;
}
</style>
