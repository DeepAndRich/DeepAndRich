<template>
	<div class="signUp z-50">
		<img src="@/assets/img/logo.png" alt="" />
		<div class="loginTitle align-middle flex items-center justify-center">
			<p>회원가입</p>
		</div>
		<div>
			<SignItem v-model="userId" placeHolder="아이디" />
			<SignItem v-model="password1" placeHolder="비밀번호" type="password" />
			<SignItem
				v-model="password2"
				placeHolder="비밀번호 확인"
				type="password"
			/>
			<div class="float-right">
				<p v-if="samePassword === 0">비밀번호를 입력해 주세요.</p>
				<p v-else-if="samePassword === 1">비밀번호가 일치하지 않습니다.</p>
				<p v-else>비밀번호가 일치합니다.</p>
			</div>

			<SignItem v-model="userName" placeHolder="이름" />
			<SignItem v-model="userNickName" placeHolder="닉네임" />
			<SignItem v-model="userAge" placeHolder="나이" type="number" />
			<div class="signItem flex items-center justify-around my-2.5">
				<span>지역</span>
				<LocationSelect v-model="userRegion" />
			</div>
			<SignItem v-model="userAssets" placeHolder="현금자산">
				<select v-model="userAssets" class="signItem my-2.5 px-2">
					<option value="">보유하신 현금자산을 선택해주세요</option>
					<option value="1000">1,000만원 이하</option>
					<option value="5000">1,000만원 이상 5,000만원 이하</option>
					<option value="10000">5,000만원 이상 1억 이하</option>
					<option value="20000">1억이상</option>
				</select>
			</SignItem>

			<div @click="signUp">
				<SignButton buttonName="회 원 가 입" />
			</div>
		</div>
	</div>
</template>

<script>
import SignButton from './SignButtonComponent.vue';
import SignItem from './SignItemComponent.vue';
import axios from 'axios';
import LocationSelect from '../LocationSelect.vue';

const URL = 'http://127.0.0.1:8000/dj-rest-auth/registration/';

export default {
	name: 'SignUpComponent',
	components: {
		SignItem,
		SignButton,
		LocationSelect,
	},
	data() {
		return {
			userId: '',
			password1: '',
			password2: '',
			userName: '',
			userNickName: '',
			userAge: '',
			userRegion: '',
			userAssets: '',
		};
	},
	computed: {
		samePassword() {
			if (this.password1.length === 0) {
				return 0;
			} else if (this.password1 !== this.password2) {
				return 1;
			} else {
				return 2;
			}
		},
	},
	methods: {
		signUp() {
			const userId = this.userId;
			const password1 = this.password1;
			const password2 = this.password2;
			const userName = this.userName;
			const userNickName = this.userNickName;
			const userAge = this.userAge;
			const userRegion = this.userRegion;
			const userAssets = this.userAssets;
			console.log('클릭');
			console.log({
				userId,
				userName,
			});
			axios
				.post(URL, {
					username: userId,
					password1,
					password2,
					age: userAge,
					realname: userName,
					nickname: userNickName,
					region: userRegion,
					asset: userAssets,
				})
				.then(res => {
					console.log(res);
				})
				.catch(err => {
					console.log(err);
				});
		},
	},
};
</script>

<style>
.signUp {
	width: 375px;
	height: 730px;
	padding: 10px;
	background-color: #fff;
	border-radius: 5px;
}
.signUp .loginTitle {
	width: 220px;
	height: 58px;
	text-align: center;
	margin: 0 auto 0 auto;
	font-size: 20px;
	font-weight: 600;
}
</style>
