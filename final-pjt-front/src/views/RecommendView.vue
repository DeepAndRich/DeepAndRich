<template>
	<div class="recommendContainer">
		<h1 class="text-3xl">MY유형검사</h1>
		<div class="my-4">
			<button
				class="w-24 h-8 border-2 rounded-lg mx-4 text-white bg-themeBlue hover:bg-sky-300"
				@click="toggleComponent"
			>
				유형검사
			</button>
			<button
				class="w-24 h-8 border-2 rounded-lg mx-4 text-white bg-themeBlue hover:bg-sky-300"
				@click="toggleComponent"
			>
				추천상품
			</button>
		</div>
		<RecommendItem
			v-if="getSelectedQuestion"
			@save-type="setSelectedQuestion"
		/>
		<RecommendQuestion v-else />
	</div>
</template>

<script>
import RecommendItem from '@/components/Recommend/RecommendItem.vue';
import RecommendQuestion from '@/components/Recommend/RecommendQuestion.vue';
export default {
	name: 'RecommendView',
	components: {
		RecommendItem,
		RecommendQuestion,
	},
	data() {
		return {
			user: JSON.parse(this.$store.getters.getUser),
			selectedQuestion: false,
		};
	},
	created() {
		console.log(this.user);
		if (this.user.personal_type == null) {
			this.selectedQuestion = false;
		} else {
			this.selectedQuestion = true;
		}
	},
	computed: {
		getSelectedQuestion() {
			console.log(this.selectedQuestion, '확인');
			return this.selectedQuestion;
		},
	},
	methods: {
		toggleComponent() {
			if (this.user.personal_type == null) {
				this.selectedQuestion = false;
				alert('유형 검사를 마치신 후 이용하실 수 있습니다.');
			} else {
				this.selectedQuestion = !this.selectedQuestion;
			}
		},
		setSelectedQuestion() {
			this.selectedQuestion = true;
			this.$router.go(0);
		},
	},
};
</script>

<style>
.recommendContainer {
	margin: 0 auto;
	width: 1200px;
	height: 650px;
}
</style>
