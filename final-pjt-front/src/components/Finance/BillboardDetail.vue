<template>
	<div class="billBoardDetail text-xl p-4 mx-auto">
		<div>은행: {{ item.fin_prdt_cd.kor_co_nm }}</div>
		<div>상품명: {{ item.fin_prdt_cd.fin_prdt_nm }}</div>
		<div>단리</div>
		<div>우대금리: {{ item.intr_rate2 }}</div>
		<div>금리: {{ item.intr_rate }}</div>
		<div>{{ item.rsrv_type_nm }}</div>
		<div v-if="checkUser">
			<button
				v-if="!productCheck"
				@click="check"
				class="border-2 rounded border-black"
			>
				상품 가입
			</button>
			<button v-else @click="check" class="border-2 rounded border-black">
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
			HavingProducts: '',
			productCheck: false,
		};
	},
	created() {
		this.getProducts();
	},
	computed: {
		checkUser() {
			return this.user;
		},
	},
	methods: {
		check() {
			console.log(this.HavingProducts, '???');
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
		async getProducts() {
			await axios
				.get(BASE_URL + this.user.pk + '/myproduct/')
				.then(res => {
					// console.log(res);
					this.HavingProducts = res.data;
					this.checkProducts();
				})
				.catch(err => {
					console.log(err);
				});
		},
		checkProducts() {
			console.log(this.HavingProducts, '설마');
			this.HavingProducts.forEach(item => {
				if (item.fin_prdt_nm == this.item.fin_prdt_nm) {
					console.log(item, '??');
					this.productCheck = true;
				}
			});
		},
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
</style>
