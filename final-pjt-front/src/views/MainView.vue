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
				<MainArticle :list="getArticles" />
			</div>
			<div class="w-3/12 flex justify-center">
				<div class="gotobox cursor-pointer">
					<div class="placeholder" @click="goToRecommend">검사하러 가기</div>
				</div>
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
import MainArticle from '@/components/Main/MainArticleComponent.vue';

export default {
	name: 'MainView',
	components: {
		TestComponentVue,
		MainArticle,
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
		axios
			.get('http://127.0.0.1:8000/articles/')
			.then(res => {
				console.log(res, '제발');
				this.articlesArray = res.data
					.sort((a, b) => {
						if (a.like_users.length >= b.like_users.length) {
							return -1;
						} else {
							return 1;
						}
					})
					.slice(0, 7);
				console.log(this.articlesArray);
			})
			.catch(err => {
				console.log(err);
			});
	},
	computed: {
		getDepositArray() {
			console.log(this.depositArray, '??');
			return this.depositArray.slice(0, 5);
		},
		getSavingArray() {
			return this.savingArray.slice(0, 5);
		},
		getArticles() {
			return this.articlesArray;
		},
	},
	methods: {
		goToRecommend() {
			this.$router.push('/recommend');
		},
	},
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
.gotobox {
	position: absolute;
	margin-top: 4.5rem;
	width: 220px;
	height: 110px;
	background-color: #000;
	border-radius: 8px;
	transition: height 0.5s;
	display: flex;
	justify-content: center;
	align-items: center;
	box-shadow: 0px 0px 4px rgba(255, 255, 255, 0.75);
}
</style>
