<template>
	<div class="login z-50">
		<img src="@/assets/img/logo.png" alt="" />
		<div class="loginTitle align-middle flex items-center justify-center">
			<p>로그인</p>
		</div>
		<div>
			<SignItem v-model="userId" placeHolder="아이디" />
			<SignItem v-model="password" placeHolder="비밀번호" type="password" />
			<p v-if="loginCheck" class="loginCheckText">
				아이디 또는 비밀번호를 확인해 주세요
			</p>
			<div @click="loginClick" @keyup.enter="loginClick">
				<SignButton buttonName="로 그 인" />
			</div>
			<div class="mt-2">
				<span class="mr-2">계정이 없으신가요?</span>
				<span
					class="text-themeBlue underline ml-2 cursor-pointer"
					@click="showSignUp"
					>회원가입</span
				>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
import SignButton from './SignButtonComponent.vue';
import SignItem from './SignItemComponent.vue';

const URL = 'http://127.0.0.1:8000/dj-rest-auth/login/';

export default {
	name: 'LoginComponent',
	components: {
		SignItem,
		SignButton,
	},
	data() {
		return {
			userId: '',
			password: '',
			loginChecked: false,
		};
	},
	computed: {
		loginCheck() {
			return this.loginChecked;
		},
	},
	methods: {
		loginClick() {
			const userId = this.userId;
			const password = this.password;
			axios
				.post(URL, {
					username: userId,
					password: password,
				})
				.then(res => {
					console.log(res);
					localStorage.setItem('token', res.data.key);
					this.$store.commit('setToken', res.data.key);
					this.$store.commit('showLogin', false);
					this.$router.go(0);
				})
				.catch(err => {
					console.log(err);
					this.loginChecked = true;
				});
		},
		showSignUp() {
			console.log('로그인에서 회원가입 버튼 클릭');
			this.$store.commit('showLogin', false);
			this.$store.commit('showSignUp', true);
		},
	},
};
</script>

<style>
.login {
	width: 375px;
	height: 385px;
	padding: 10px;
	background-color: #fff;
	border-radius: 5px;
}
.login .loginTitle {
	width: 220px;
	height: 58px;
	text-align: center;
	margin: 0 auto 0 auto;
	font-size: 20px;
	font-weight: 600;
}
.loginCheckText {
	color: red;
	font-size: 0.8rem;
	font-weight: 700;
}
</style>
