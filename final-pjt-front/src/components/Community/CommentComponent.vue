<template>
	<div>
		<div v-if="!modifyCheck">
			{{ item.content }}
			<div>작성자: {{ item.author_nickname }}</div>
		</div>
		<div v-else>
			<input v-model="content" type="text" />
		</div>
		<div v-if="userCheck">
			<button @click="modifyToggle">
				<span v-if="!modifyCheck">수정</span>
				<span v-else>수정취소</span>
			</button>
			<button v-if="modifyCheck" @click="modifyComment">저장</button>
			<button v-else @click="deleteComment">삭제</button>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
const URL = 'http://127.0.0.1:8000/articles/comments/';

export default {
	name: 'CommentComponent',
	props: {
		item: Object,
	},
	data() {
		return {
			articleId: this.$route.params.id,
			modifyCheck: false,
			content: this.item.content,
			userToken: localStorage.getItem('token'),
			user: this.$store.getters.getUser,
		};
	},
	computed: {
		checkModify() {
			return this.modifyCheck;
		},
		userCheck() {
			if (JSON.parse(this.user)?.pk == this.item?.author_id) {
				console.log('확인');
				return true;
			} else {
				return false;
			}
		},
	},
	methods: {
		deleteComment() {
			axios
				.delete(URL + this.item.id + '/')
				.then(res => {
					console.log(res);
					this.$emit('comment-deleted');
				})
				.catch(err => {
					console.log(err);
				});
		},
		modifyToggle() {
			this.modifyCheck = !this.modifyCheck;
		},
		modifyComment() {
			axios
				.put(URL + this.item.id + '/', {
					headers: {
						Authorization: `Token ${this.userToken}`,
					},
					content: this.content,
				})
				.then(res => {
					console.log(res);
					this.modifyCheck = false;
					this.$emit('comment-modified');
				})
				.catch(err => {
					console.log(err);
				});
		},
	},
};
</script>

<style></style>
