<template>
	<div>
		<div class="bigbox">
			<!-- <h1>상세페이지</h1> -->
			<div v-if="getArticleCheck">
				<div v-if="!modifyCheck">
					<div class="flex justify-between">
						<h1 class="title text-left">{{ article.title }}</h1>
						<div class="flex items-center justify-center" v-if="isLogined">
							<div
								class="flex items-center justify-center"
								v-if="!getUserCheck"
							>
								<button
									class="border-2 border-rose-300 bg-rose-300 hover:bg-rose-400 rounded-lg w-32 h-8"
									v-if="getLikeUsers"
									@click="likeArticle"
								>
									좋아요!
								</button>
								<button
									class="border-2 border-rose-300 bg-rose-300 hover:bg-rose-400 rounded-lg w-32 h-8"
									v-else
									@click="likeArticle"
								>
									좋아요 취소
								</button>
							</div>
						</div>
					</div>
					<div
						class="text-left flex justify-around items-center h-12 border-b-2 border-black"
					>
						<div>작성자 : {{ article.author_nickname }}</div>
						<div>좋아요수: {{ article.like_users.length }}</div>
						<div>작성시간: {{ formatDate(article.created_at) }}</div>
					</div>
					<br />
					<div class="content pd-2 text-left">
						{{ article.content }}
					</div>
					<br />
				</div>
				<div v-else>
					<div class="w-full h-12 border-b-2 border-black">
						<span class="text-lg mr-4">제목:</span>
						<input
							v-model="article.title"
							class="border-2 w-10/12 h-8 pl-4"
							type="text"
							name="title"
							maxlength="10"
						/>
					</div>
					<div class="w-full">
						<div class="text-left pl-4 text-lg my-4">내용</div>
						<textarea
							class="bd-black border-2 p-4"
							name="contents"
							cols="72"
							rows="20"
							v-model="article.content"
							placeholder="내용을 작성하세요"
						></textarea>
					</div>
				</div>

				<div class="flex justify-between">
					<div>
						<button
							class="w-24 h-8 mb-2 border-2 border-red-200 rounded-lg"
							@click="goToCommunity"
						>
							돌아가기
						</button>
					</div>
					<div v-if="getUserCheck">
						<button
							class="w-24 h-8 border-2 border-black rounded-lg mx-4"
							@click="modifyToggle"
						>
							<span v-if="!modifyCheck">수정</span>
							<span v-else>수정취소</span>
						</button>
						<button
							class="w-24 h-8 border-2 border-black rounded-lg"
							v-if="modifyCheck"
							@click="modifyArticle"
						>
							저장
						</button>
						<button
							class="w-24 h-8 border-2 border-black rounded-lg"
							v-else
							@click="deleteArticle"
						>
							삭제
						</button>
					</div>
				</div>
			</div>
			<div v-else>로딩중</div>
			<hr />
			<h3 class="text-left" style="font-size: 24px">Comments</h3>
			<div class="mt-10 pb-10">
				<div class="input">
					<input
						class="p-4 rounded-lg w-10/12"
						type="text"
						name="comment"
						v-model="inputComment"
						placeholder="댓글 작성"
						style="border: 1px solid black; height: 50px"
					/>
					&nbsp;
					<button
						class="border-2 border-black rounded-lg w-24 h-12"
						@click="saveComment"
					>
						저장
					</button>
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
		isLogined() {
			const check = localStorage.getItem('token');
			if (check?.length > 0) {
				return true;
			} else {
				return false;
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
		goToCommunity() {
			this.$router.push('/community');
		},
		formatDate(date) {
			const formattedDate = new Date(date);
			const year = formattedDate.getFullYear();
			const month = ('0' + (formattedDate.getMonth() + 1)).slice(-2);
			const day = ('0' + formattedDate.getDate()).slice(-2);
			return `${year}년 ${month}월 ${day}일`;
		},
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
	/* padding-top: 130px; */
	background-color: #ffffff; /* 원하는 배경색 */
}

.content {
	/* border: 0.5px solid black; */
	/* padding-top: 1rem; */
	height: 300px;
}

/* .input {
	padding-bottom: 20px;
} */

.comment-container {
	padding-top: 2rem;
	text-align: left;

	/* margin-bottom: 20px; */
}
</style>
