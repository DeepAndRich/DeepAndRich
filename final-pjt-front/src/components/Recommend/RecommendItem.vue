<template>
	<div>
		<!-- 추천
		<button @click="setRecommendProducts">와와아</button> -->
		<div>
			<img class="mx-auto" :src="getUserType" alt="" />
			<!-- {{ recommendProducts }} -->
		</div>
		<div
			class="recommendBoard bg-black rounded-lg mt-10 p-3"
			v-if="recommendProducts"
		>
			<RecommendListTitle />
			<RecommendItemList :items="getRecommendedProducts" />
		</div>
	</div>
</template>

<script>
import axios from 'axios';

import RecommendListTitle from './RecommendListTitle.vue';
import RecommendItemList from './RecommendItemList.vue';

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
	components: {
		RecommendListTitle,
		RecommendItemList,
	},
	computed: {
		getUserType() {
			console.log(this.userType);
			// return this.userType;

			return require(`@/assets/img/${this.userType}.gif`);
		},
		getRecommendedProducts() {
			if (this.recommendProducts.length == 0) {
				this.setRecommendProducts();
			}
			return this.recommendProducts;
		},
	},
	// created() {
	// 	this.setRecommendProducts;
	// },
	methods: {
		getImagePath() {
			console.log(`@/assets/img/${this.userType}.gif`);
			return require(`@/assets/img/${this.userType}.gif`);
		},
		async setRecommendProducts() {
			await axios
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
