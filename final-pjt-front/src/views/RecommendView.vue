<template>
	<div class="recommendContainer bg-green-200">
		<h1>추천알고리즘</h1>
		<div>
			<button @click="toggleComponent">유형검사</button>
			<button @click="toggleComponent">추천상품</button>
		</div>
		<RecommendItem v-if="selectedQuestion" />
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
			user: this.$store.getters.getUser,
			selectedQuestion: false,
		};
	},
	created() {
		if (this.user.personal_type == null) {
			this.selectedQuestion = false;
		} else {
			this.selectedQuestion = true;
		}
	},
	methods: {
		toggleComponent() {
			this.selectedQuestion = !this.selectedQuestion;
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
