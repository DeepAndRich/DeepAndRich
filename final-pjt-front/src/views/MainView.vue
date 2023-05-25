<template>
	<div class="mainPage mx-auto">
		<div class="mainContainer flex">
			<div class="w-3/12 flex justify-center">
				<TestComponentVue
					name="정기예금 순위"
					:list="getDepositArray"
					@click-check="goToFinance"
				/>
			</div>
			<div class="w-3/12 flex justify-center">
				<TestComponentVue
					name="정기적금 순위"
					:list="getSavingArray"
					@click-check="goToFinance"
				/>
			</div>
			<div class="w-3/12 flex justify-center">
				<MainArticle :list="getArticles" @click-check="goToArticle" />
			</div>
			<div class="w-3/12 flex justify-center">
				<div class="gotobox cursor-pointer">
					<div class="placeholder" @click="goToRecommend">검사하러 가기</div>
				</div>
			</div>
		</div>
		<!-- {{ getDepositArray }} -->
		<div class="mainBtmContainer">
			<div class="p-4 py-12" style="font-size: 30px">
				<h2>나에게 어울리는 스타일은?</h2>
			</div>
			<div class="flex flex-wrap px-3">
				<div class="image-container w-3/12">
					<span>어떤 방식이든 자유롭게 자유형</span>
					<img src="@/assets/img/freestyle.gif/" />
				</div>
				<div class="image-container w-3/12">
					<span>느리지만 확실하게, 원하는 용도로 자유롭게</span>
					<img src="@/assets/img/breststroke.gif/" />
				</div>
				<div class="image-container w-3/12">
					<span>유유자적 돈 버는 게 제일 쉬웠어요...</span>
					<img src="@/assets/img/backstroke.gif/" />
				</div>
				<div class="image-container w-3/12">
					<span>압도적인 추진력! 저 먼저 갑니다</span>
					<img src="@/assets/img/butterfly.gif/" />
				</div>
			</div>
			<div>
				<button
					class="bg-themeBlue w-48 h-12 text-lg text-white rounded-lg mt-16"
					@click="goToRecommend"
				>
					확인하러 가기
				</button>
			</div>
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
		goToArticle() {
			this.$router.push('/community');
		},
		goToFinance() {
			this.$router.push('/finance');
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
	height: 470px;
}
.mainBtmContainer {
	margin: 0 auto;
	width: 1200px;
	height: 500px;
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
