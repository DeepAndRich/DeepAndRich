<template>
	<div>
		<h1>상세페이지</h1>
		<div v-if="getArticleCheck">
			{{ article.title }}
			{{ article.content }}
		</div>
		<div v-else>로딩중</div>
		<div>
			댓글자리
			<div>
				<input type="text" name="comment" v-model="inputComment" />
				<button @click="saveComment">댓글 저장</button>
			</div>
			<div v-for="item in article.comment_set" :key="item.id">
				<Comment :item="item" />
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
import Comment from '@/components/Community/CommentComponent.vue';
const URL = 'http://127.0.0.1:8000/articles/';

export default {
	name: 'CommunityDetailView',
	components: {
		Comment,
	},
	data() {
		return {
			article: [],
			comments: [],
			inputComment: '',
			userToken: localStorage.getItem('token'),
		};
	},
	created() {
		this.getArticle();
		this.getComments();
	},
	computed: {
		getArticleCheck() {
			if (this.article.length === 0) {
				return false;
			} else {
				return true;
			}
		},
	},
	methods: {
		getArticle() {
			axios
				.get(URL + this.$route.params.id + '/')
				.then(res => {
					console.log(res);
					this.article = res.data;
				})
				.catch(err => {
					console.log(err);
				});
		},
		getComments() {
			axios
				.get(URL + this.$route.params.id + '/comments/')
				.then(res => {
					console.log(res);
					this.comments = res.data;
				})
				.catch(err => {
					console.log(err);
				});
		},
		saveComment() {
			axios
				.post(URL + this.$route.params.id + '/comments/', {
					headers: {
						Authorization: `Token ${this.userToken}`,
					},
					content: this.inputComment,
				})
				.then(res => {
					console.log(res);
					this.inputComment = '';
					// this.getComments();
					this.getArticle();
				})
				.catch(err => {
					console.log(err);
				});
		},
	},
};
</script>

<style></style>
