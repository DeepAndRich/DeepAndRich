<template>
	<div class="community p-8 text-lg">
		<!-- bg-green-200 -->
		<div class="flex items-center justify-between">
			<!-- <div class="w-2/12">게시판</div> -->
			<div></div>
			<div class="w-2/12 flex justify-end items-center">
				<button
					class="w-24 h-8 mx-4 border-2 border-black rounded-lg"
					@click="goToCreateArticle"
				>
					글쓰기
				</button>
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
		<div style="min-height: 600px" v-if="getArticlesCheck">
			<CommunityList
				v-for="(item, index) in paginatedItems"
				:item="item"
				:index="index + 1"
				:key="item.id"
			/>
		</div>
		<div v-else style="min-height: 600px">글이 없습니다.</div>
		<Pagination
			:currentPage="currentPage"
			:totalPages="totalPages"
			@page-changed="handlePageChange"
		/>

		<!-- <button @click="getArticles">safasdfsf</button> -->
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
				updated_at: '수정',
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
		async getArticles() {
			await axios
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
