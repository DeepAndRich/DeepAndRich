<template>
	<div class="recommendedItemContainer">
		<!-- 추천
		<button @click="setRecommendProducts">와와아</button> -->
		<div>
			<img class="mx-auto" :src="getUserType" alt="" />
			<p class="text-xl my-2">당신은 {{ getComment.name }}입니다</p>
			<p class="text-lg">{{ getComment.content }}</p>
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
			style: {
				freestyle: {
					name: '자유형',
					content:
						'자유형은 자유롭게 어떤 방식으로든 헤엄칠 수 있습니다. 자유로운 당신에게 다음과 같은 상품을 추천합니다.',
				},

				backstroke: {
					name: '배영',
					content:
						'마치 물에 누워 떠다니듯이 여유를 즐길 줄 아는 당신에게 다음과 같은 상품을 추천합니다.',
				},

				breaststroke: {
					name: '평영',
					content:
						'빠르지 않아도 확실하게 원하는 방향으로 가고싶은 당신에게 다음과 같은 상품을 추천합니다.',
				},

				butterfly: {
					name: '접영',
					content:
						'압도적인 추진력을 가지고 가장 빠른 속도를 낼 수 있는 당신에게 다음과 같은 상품을 추천합니다.',
				},
			},
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
		getComment() {
			return this.style[this.userType];
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

<style>
.recommendedItemContainer {
	width: 1000px;
	margin: 0 auto;
}
</style>
