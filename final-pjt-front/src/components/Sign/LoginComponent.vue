<template>
	<div class="login z-50">
		<img src="@/assets/img/logo.png" alt="" />
		<div class="loginTitle align-middle flex items-center justify-center">
			<p>로그인</p>
		</div>
		<div>
			<SignItem v-model="userId" placeHolder="아이디" />
			<SignItem v-model="password" placeHolder="비밀번호" type="password" />
			<SignButton buttonName="로 그 인" />
			<div class="mt-2">
				<span class="mr-2">계정이 없으신가요?</span>
				<span class="text-themeBlue underline ml-2">회원가입</span>
			</div>
		</div>
	</div>
</template>

<script>
import SignButton from './SignButtonComponent.vue';
import SignItem from './SignItemComponent.vue';

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
		};
	},
};
</script>

<style>
.login {
	width: 375px;
	height: 375px;
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
</style>
