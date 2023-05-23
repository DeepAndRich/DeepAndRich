<template>
	<div class="community p-8 bg-green-200 text-lg">
		<div class="flex items-center justify-between">
			<div class="w-2/12">게시판</div>
			<div class="w-2/12">
				<button>검색</button>
				<button>글쓰기</button>
			</div>
		</div>
		<div class="border-solid border-b-2 border-black">
			<CommunityList />
		</div>
		<CommunityList />
		<CommunityList />
		<CommunityList />
		<CommunityList />
		<CommunityList />
		<CommunityList />
	</div>
</template>

<script>
import CommunityList from '@/components/Community/CommunityList.vue';

export default {
	name: 'CommunityView',
	components: {
		CommunityList,
	},
	data() {
		return {
			tableHeader: {
				title: '제목',
				author: '작성자',
				created_at: '작성일',
			},
		};
	},
};
</script>

<style>
.community {
	margin: 0 auto;
	width: 1200px;
	height: 800px;
	/* background-color: #000; */
}
</style>
