<template>
	<div class="communityCreate mx-auto">
		<div class="w-full h-12 border-b-2 border-black">
			<span class="text-lg mr-4">제목:</span>
			<input
				v-model="title"
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
				v-model="content"
				placeholder="내용을 작성하세요"
			></textarea>
		</div>
		<div class="flex justify-end">
			<button
				class="w-24 h-8 border-2 border-black rounded-lg mx-4"
				@click="createArticle"
			>
				저장
			</button>
			<button
				class="w-24 h-8 border-2 border-black rounded-lg"
				@click="returnCommunity"
			>
				돌아가기
			</button>
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
	width: 700px;
	height: 700px;
}
</style>
