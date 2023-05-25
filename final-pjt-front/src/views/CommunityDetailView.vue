<template>
	<div>
		<div class="bigbox">
			<!-- <h1>상세페이지</h1> -->
			<div v-if="getArticleCheck">
				<div v-if="!modifyCheck">
					<div class="flex justify-between">
						<h1 class="title text-left">{{ article.title }}</h1>
						<div class="text-right" v-if="!getUserCheck">
							<button v-if="getLikeUsers" @click="likeArticle">좋아요!</button>
							<button v-else @click="likeArticle">좋아요 취소</button>
						</div>
					</div>
					<div class="text-left">{{ article.author_nickname }}</div>
					<br />
					<div class="content text-left">
						{{ article.content }}
					</div>
					<br />
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
					<button v-else @click="deleteArticle" style="border: 1px solid black">
						삭제
					</button>
				</div>
			</div>
			<div v-else>로딩중</div>
			<hr />
			<h3 class="text-left" style="font-size: 24px">댓글</h3>
			<div class="mt-10 pb-10">
				<div class="input">
					<input
						type="text"
						name="comment"
						v-model="inputComment"
						style="border: 1px solid black; width: 90%; height: 50px"
					/>
					&nbsp;
					<button @click="saveComment">저장</button>
				</div>
				<div
					v-for="item in article.comment_set"
					:key="item.id"
					class="comment-container"
				>
					<Comment
						:item="item"
						@comment-deleted="getArticle"
						@comment-modified="getArticle"
					/>
				</div>
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
			user: this.$store.getters.getUser,
			isChecked: false,
			likeUsers: [],
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
			console.log(this.user, '???');
			if (this.article?.author_nickname == JSON.parse(this.user)?.nickname) {
				return true;
			}
			return false;
		},
		getLikeUsers() {
			if (this.likeUsers.includes(JSON.parse(this.user)?.pk)) {
				return false;
			} else {
				return true;
			}
		},
	},
	methods: {
		userCheck() {
			if (this.article.author == JSON.parse(this.user)?.pk) {
				return true;
			} else {
				return false;
			}
		},
		likeArticle() {
			axios
				.post(URL + this.article.id + '/likes/', null, {
					headers: {
						Authorization: `Token ${this.userToken}`,
					},
				})
				.then(res => {
					console.log(res);
					this.getArticle();
				})
				.catch(err => {
					console.log(err);
				});
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
					this.likeUsers = res.data.like_users;
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
				.post(
					URL + this.$route.params.id + '/comments/',
					{
						content: this.inputComment,
					},
					{
						headers: {
							Authorization: `Token ${this.userToken}`,
						},
					},
				)
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

<style>
.title {
	font-size: 35px;
	margin-left: 10;
	margin-top: 10;
}

.bigbox {
	margin: 0 auto;
	width: 700px;
	padding: 8px;
	padding-top: 130px;
	background-color: #ffffff; /* 원하는 배경색 */
}

.content {
	/* border: 0.5px solid black; */
	padding-top: 30px;
	height: 300px;
}

.input {
	padding-bottom: 20px;
}

.comment-container {
	padding-top: 50px;
	text-align: left;

	margin-bottom: 20px; /* 원하는 간격 크기로 조절하세요 */
}
</style>
