<template>
	<div>
		추천
		<button @click="getRecommendProducts">와와아</button>
		<div>
			<img class="mx-auto" :src="getUserType" alt="" />
			{{ recommendProducts }}
		</div>
	</div>
</template>

<script>
import axios from 'axios';
const TYPE_URL = 'http://127.0.0.1:8000/dj-rest-auth/user/';
const SAVING_URL = 'http://127.0.0.1:8000/savings/';
const DEPOSIT_URL = 'http://127.0.0.1:8000/deposits/';

export default {
	name: 'RecommendItem',
	data() {
		return {
			recommendProducts: [],
			userType: 'freestyle',
			userToken: localStorage.getItem('token'),
		};
	},
	computed: {
		getUserType() {
			console.log(this.userType);
			// return this.userType;

			return require(`@/assets/img/${this.userType}.gif`);
		},
	},
	methods: {
		getImagePath() {
			console.log(`@/assets/img/${this.userType}.gif`);
			// 동적 이미지 경로를 반환하는 메소드
			// return require(`@/assets/img/${this.userType}.gif`);
			// this.getRecommendProducts();
			return require(`@/assets/img/${this.userType}.gif`);
		},
		getRecommendProducts() {
			axios
				.get(TYPE_URL, {
					headers: {
						Authorization: `Token ${this.userToken}`,
					},
				})
				.then(res => {
					console.log(res);
					this.userType = res.data.personal_type;
					if (this.userType == 'freestyle' || this.userType == 'breaststroke') {
						axios
							.get(SAVING_URL + this.userType + '/')
							.then(res => {
								console.log(res);
								this.recommendProducts = res.data;
							})
							.catch(err => {
								console.log(err);
							});
					} else {
						axios
							.get(DEPOSIT_URL + this.userType + '/')
							.then(res => {
								console.log(res);
								this.recommendProducts = res.data;
							})
							.catch(err => {
								console.log(err);
							});
					}
				})
				.catch(err => {
					console.log(err);
				});
		},
	},
};
</script>

<style></style>
