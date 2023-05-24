<template>
	<div class="community p-8 bg-green-200 text-lg">
		<div class="flex items-center justify-between">
			<div class="w-2/12">게시판</div>
			<div class="w-2/12">
				<button>검색</button>
				<button @click="goToCreateArticle">글쓰기</button>
			</div>
		</div>
		<div class="border-solid border-b-2 border-black">
			<div class="flex items-center justify-around w-full h-12">
				<div class="w-2/12 h-8">글번호</div>
				<div class="w-5/12">제목</div>
				<div class="w-2/12">작성자</div>
				<div class="w-2/12">작성일</div>
				<div class="w-1/12">좋아요</div>
			</div>
		</div>
		<div v-if="getArticlesCheck">
			<CommunityList
				v-for="item in paginatedItems"
				:item="item"
				:key="item.id"
			/>
		</div>
		<div v-else>로딩중</div>
		<Pagination
			:currentPage="currentPage"
			:totalPages="totalPages"
			@page-changed="handlePageChange"
		/>

		<button @click="getArticles">safasdfsf</button>
	</div>
</template>

<script>
import CommunityList from '@/components/Community/CommunityList.vue';
import Pagination from '@/components/Finance/PaginationComponent.vue';

import axios from 'axios';
const URL = 'http://127.0.0.1:8000/articles/';

export default {
	name: 'CommunityView',
	components: {
		CommunityList,
		Pagination,
	},
	data() {
		return {
			articles: [],
			tableHeader: {
				title: '제목',
				author: '작성자',
				created_at: '작성일',
			},
			currentPage: 1,
			itemsPerPage: 10, // 페이지당 아이템 수
		};
	},
	created() {
		this.getArticles();
	},
	computed: {
		getArticlesCheck() {
			if (this.articles.length === 0) {
				return false;
			} else {
				return true;
			}
		},
		totalItems() {
			return this.articles.length;
		},
		totalPages() {
			return Math.ceil(this.totalItems / this.itemsPerPage);
		},
		paginatedItems() {
			const startIndex = (this.currentPage - 1) * this.itemsPerPage;
			const endIndex = startIndex + this.itemsPerPage;
			return this.articles.slice(startIndex, endIndex);
		},
	},
	methods: {
		goToCreateArticle() {
			this.$router.push('/community/create');
		},
		getArticles() {
			axios
				.get(URL)
				.then(res => {
					console.log(res);
					this.articles = res.data;
				})
				.catch(err => {
					console.log(err);
				});
		},
		handlePageChange(page) {
			this.currentPage = page;
		},
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
