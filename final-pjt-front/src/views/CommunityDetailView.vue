<template>
	<div>
		<h1>상세페이지</h1>
		<div v-if="getArticleCheck">
			<div v-if="!modifyCheck">
				{{ article.title }} <br />{{ article.content }} <br />
				저자: {{ article.author }}
			</div>
			<div v-else>
				<div class="w-full">
					title :
					<input
						v-model="article.title"
						class="border-2"
						type="text"
						name="title"
						maxlength="10"
					/>
				</div>
				<div class="w-full">
					<div>content</div>
					<textarea
						class="bd-black border-2"
						name="content"
						cols="70"
						rows="20"
						v-model="article.content"
					></textarea>
				</div>
			</div>

			<div v-if="getUserCheck">
				<button @click="modifyToggle">
					<span v-if="!modifyCheck">수정</span>
					<span v-else>수정취소</span>
				</button>
				<button v-if="modifyCheck" @click="modifyArticle">저장</button>
				<button v-else @click="deleteArticle">삭제</button>
			</div>
		</div>
		<div v-else>로딩중</div>
		<hr />
		<div class="mt-10">
			댓글자리
			<div>
				<input type="text" name="comment" v-model="inputComment" />
				<button @click="saveComment">댓글 저장</button>
			</div>
			<div v-for="item in article.comment_set" :key="item.id">
				<Comment
					:item="item"
					@comment-deleted="getArticle"
					@comment-modified="getArticle"
				/>
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
			title: '',
			content: '',
			modifyCheck: false,
			inputComment: '',
			userToken: localStorage.getItem('token'),
			user: localStorage.getItem('user'),
			isChecked: false,
		};
	},
	created() {
		this.getArticle();
	},
	computed: {
		getArticleCheck() {
			if (this.article.length === 0) {
				return false;
			} else {
				return true;
			}
		},
		getUserCheck() {
			return this.isChecked;
		},
	},
	methods: {
		userCheck() {
			if (this.article.author == JSON.parse(this.user).pk) {
				return true;
			} else {
				return false;
			}
		},
		modifyToggle() {
			this.modifyCheck = !this.modifyCheck;
		},
		getArticle() {
			axios
				.get(URL + this.$route.params.id + '/')
				.then(res => {
					console.log(res);
					this.article = res.data;
					this.isChecked = this.userCheck();
				})
				.catch(err => {
					console.log(err);
				});
		},
		deleteArticle() {
			axios
				.delete(URL + this.$route.params.id + '/delete/')
				.then(res => {
					console.log(res);
					this.$router.push('/community');
					// this.$emit('comment-deleted');
				})
				.catch(err => {
					console.log(err);
				});
		},
		modifyArticle() {
			axios
				.put(URL + this.$route.params.id + '/', {
					headers: {
						Authorization: `Token ${this.userToken}`,
					},
					title: this.article.title,
					content: this.article.content,
				})
				.then(res => {
					console.log(res);
					this.modifyCheck = false;
					// this.$emit('comment-modified');
					this.getArticle();
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
