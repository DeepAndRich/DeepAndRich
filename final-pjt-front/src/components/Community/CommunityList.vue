<template>
	<div class="flex items-center justify-around w-full h-12">
		<div class="w-2/12 h-8">글 번호</div>
		<div class="w-5/12">{{ item.title }}</div>
		<div class="w-2/12">{{ item.author }}</div>
		<div class="w-1/12">{{ item.created_at }}</div>
		<div class="w-1/12">{{ item.like_users }}</div>
	</div>
</template>

<script>
export default {
	name: 'CommunityList',
	props: {
		item: {
			type: Object,
			default: () => {
				return {
					title: '제목',
					author: '작성자',
					created_at: '작성일',
					like_users: '좋아요',
				};
			},
		},
	},
};
</script>

<style></style>
