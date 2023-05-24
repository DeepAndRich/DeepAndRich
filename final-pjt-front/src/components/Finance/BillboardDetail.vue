<template>
	<div class="billBoardDetail text-xl p-4 mx-auto">
		<div>은행: {{ item.fin_prdt_cd.kor_co_nm }}</div>
		<div>상품명: {{ item.fin_prdt_cd.fin_prdt_nm }}</div>
		<div>단리</div>
		<div>우대금리: {{ item.intr_rate2 }}</div>
		<div>금리: {{ item.intr_rate }}</div>
		<div>{{ item.rsrv_type_nm }}</div>
		<button @click="check" class="border-2 rounded border-black">
			상품 가입
		</button>

		<BillboardDetailItem />
	</div>
</template>

<script>
import BillboardDetailItem from './BillboardDetailItem.vue';
import axios from 'axios';
const URL = 'http://127.0.0.1:8000/accounts/save_myproduct/';

export default {
	name: 'BillboardDetail',
	components: {
		BillboardDetailItem,
	},
	props: {
		item: Object,
	},
	data() {
		return {
			user: JSON.parse(localStorage.getItem('user')),
			userToken: localStorage.getItem('token'),
		};
	},
	methods: {
		check() {
			console.log(this.user.pk);
			console.log(this.userToken);
			console.log(this.item);
			console.log(this.item.fin_prdt_cd.id);
			axios
				.post(URL + this.item.fin_prdt_cd.id + '/', null, {
					headers: {
						Authorization: `Token ${this.userToken}`,
					},
				})
				.then(res => {
					console.log(res);
				})
				.catch(err => {
					console.log(err);
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
