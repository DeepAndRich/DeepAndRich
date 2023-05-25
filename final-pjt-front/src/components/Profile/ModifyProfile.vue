<template>
	<div class="signUp z-50">
		<img src="@/assets/img/logo.png" alt="" />
		<div class="loginTitle align-middle flex items-center justify-center">
			<p>회원정보수정</p>
		</div>
		<div>
			<!-- <SignItem v-model="userId" placeHolder="아이디" />
			<SignItem v-model="password1" placeHolder="비밀번호" type="password" /> -->
			<!-- <SignItem
				v-model="password2"
				placeHolder="비밀번호 확인"
				type="password"
			/>
			<div class="float-right">
				<p v-if="samePassword === 0">비밀번호를 입력해 주세요.</p>
				<p v-else-if="samePassword === 1">비밀번호가 일치하지 않습니다.</p>
				<p v-else>비밀번호가 일치합니다.</p>
			</div> -->

			<!-- <SignItem v-model="userName" placeHolder="이름" /> -->
			<SignItem v-model="userNickName" placeHolder="닉네임" />
			<SignItem
				v-model="userAge"
				placeHolder="나이"
				type="number"
				min="0"
				max="100"
			/>
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

			<div @click="modifyProfile">
				<SignButton buttonName="수정" />
			</div>
			<button @click="check">확인</button>
		</div>
	</div>
</template>

<script>
import SignButton from '@/components/Sign/SignButtonComponent.vue';
import SignItem from '@/components/Sign/SignItemComponent.vue';
import axios from 'axios';
import LocationSelect from '@/components/LocationSelect.vue';

const URL = 'http://127.0.0.1:8000/dj-rest-auth/user/';

export default {
	name: 'ModifyProfile',
	components: {
		SignItem,
		SignButton,
		LocationSelect,
	},
	data() {
		return {
			user: JSON.parse(this.$store.getters.getUser),
			userId: '',
			password1: '',
			password2: '',
			userName: '',
			userNickName: '',
			userAge: '',
			userRegion: '',
			userAssets: '',
			userToken: localStorage.getItem('token'),
		};
	},
	created() {
		this.userName = this.user.realname;
		this.userNickName = this.user.nickname;
		this.userAge = Number(this.user.age);
		this.userRegion = this.user.region;
		this.userAssets = this.user.asset;
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
		check() {
			console.log(this.user);
		},
		modifyProfile() {
			// const userId = this.userId;
			// const password1 = this.password1;
			// const password2 = this.password2;
			const userName = this.userName;
			const userNickName = this.userNickName;
			const userAge = this.userAge;
			const userRegion = this.userRegion;
			const userAssets = this.userAssets;
			console.log('회원가입 요청');
			axios
				.put(
					URL,
					{
						// username: userId,
						// password1,
						// password2,
						age: userAge,
						realname: userName,
						nickname: userNickName,
						region: userRegion,
						asset: userAssets,
					},
					{
						headers: {
							Authorization: `Token ${this.userToken}`,
						},
					},
				)
				.then(res => {
					console.log(res);
					this.$router.go(0);
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
