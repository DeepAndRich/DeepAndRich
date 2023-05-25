<template>
	<div
		class="flex items-center justify-around w-full h-12 hover:underline cursor-pointer"
		@click="goToDetail"
	>
		<div class="w-2/12 h-8">{{ index }}</div>
		<div class="w-5/12 cursor-pointer">
			{{ item.title }}
		</div>
		<div class="w-2/12">{{ item.author_nickname }}</div>
		<div class="w-2/12">{{ formatDate(item.created_at) }}</div>
		<div class="w-1/12">{{ item.like_users.length }}</div>
	</div>
</template>

<script>
// const URL = 'http://127.0.0.1:8000/articles/';

export default {
	name: 'CommunityList',
	props: {
		item: {
			type: Object,
			default: () => {
				return {
					id: '글번호',
					title: '제목',
					author: '작성자',
					created_at: '작성일',
					like_users: '좋아요',
				};
			},
		},
		index: Number,
	},
	methods: {
		formatDate(date) {
			const formattedDate = new Date(date);
			const year = formattedDate.getFullYear();
			const month = ('0' + (formattedDate.getMonth() + 1)).slice(-2);
			const day = ('0' + formattedDate.getDate()).slice(-2);
			return `${year}년 ${month}월 ${day}일`;
		},
		goToDetail() {
			console.log('??');
			this.$router.push(`community/${this.item.id}/`);
		},
	},
};
</script>

<style></style>
