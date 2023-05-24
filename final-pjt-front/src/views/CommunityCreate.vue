<template>
	<div class="communityCreate bg-green-200 mx-auto p-5">
		<div class="w-full">
			title :
			<input
				v-model="title"
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
				name="contents"
				cols="70"
				rows="20"
				v-model="content"
			></textarea>
		</div>
		<div>
			<button @click="createArticle">저장</button>
			<button @click="returnCommunity">돌아가기</button>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
const URL = 'http://127.0.0.1:8000/articles/';
export default {
	name: 'CommunityCreate',
	data() {
		return {
			title: '',
			content: '',
			userToken: localStorage.getItem('token'),
		};
	},
	methods: {
		// check() {
		// 	console.log(this.title, this.content);
		// },
		// {
		// 			headers: {
		// 				Authorization: `Token ${this.userToken}`,
		// 			},
		// 			title,
		// 			content,
		// 		}

		createArticle() {
			const title = this.title;
			const content = this.content;
			if (title.length === 0 || content.length === 0) {
				return;
			}
			const body = { title, content };
			console.log(body, this.userToken, '저장?');
			axios
				.post(
					URL,
					{
						title,
						content,
					},
					{
						headers: {
							Authorization: `Token ${this.userToken}`,
						},
					},
				)
				.then(res => {
					console.log(res);
					this.returnCommunity();
				})
				.catch(err => {
					console.log(err);
					console.log('why');
				});
		},
		returnCommunity() {
			this.$router.push('/community');
		},
	},
};
</script>

<style>
.communityCreate {
	width: 1000px;
	height: 700px;
}
</style>
