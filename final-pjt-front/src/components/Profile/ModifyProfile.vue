<template>
	<div class="modifyProfile z-50">
		<img src="@/assets/img/logo.png" alt="" />
		<div class="loginTitle align-middle flex items-center justify-center">
			<p>회원정보수정</p>
		</div>
		<div>
			<SignItem v-model="userName" placeHolder="이름" />
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
			userAge: 0,
			userRegion: '',
			userAssets: 0,
			userToken: localStorage.getItem('token'),
		};
	},
	created() {
		this.userName = this.user.realname;
		this.userNickName = this.user.nickname;
		this.userAge = String(this.user.age);
		this.userRegion = this.user.region;
		this.userAssets = String(this.user.asset);
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
			const userName = this.userName;
			const userNickName = this.userNickName;
			const userAge = this.userAge;
			const userRegion = this.userRegion;
			const userAssets = this.userAssets;
			console.log('프로필 수정 요청');
			axios
				.put(
					URL,
					{
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
					this.$emit('profile-modified');
				})
				.catch(err => {
					console.log(err);
					alert('이미 존재하는 닉네임입니다.');
				});
		},
	},
};
</script>

<style>
.modifyProfile {
	width: 375px;
	height: 530px;
	padding: 10px;
	background-color: #fff;
	border-radius: 5px;
}
.modifyProfile .loginTitle {
	width: 220px;
	height: 58px;
	text-align: center;
	margin: 0 auto 0 auto;
	font-size: 20px;
	font-weight: 600;
}
</style>
