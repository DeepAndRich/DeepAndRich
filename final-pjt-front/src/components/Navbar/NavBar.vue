<template>
	<div class="py-11 px-14 w-full h-36 mx-auto bg-white z-30">
		<nav
			class="text-xl flex box-content p-0 flex-wrap items-center justify-between"
		>
			<div class="flex items-center">
				<router-link to="/" class="w-80 mr-2"
					><img class="w-80" src="@/assets/img/logo.png" alt=""
				/></router-link>
				<div v-for="item in navList" :key="item.title">
					<NavBarLink :item="item" />
				</div>
			</div>
			<div class="flex items-center">
				<div v-if="!isLogined">
					<button class="mx-2 font-bold" @click="loginClick">로그인</button>
					<button
						class="mx-2 w-40 h-10 font-bold bg-themeyellow rounded-lg"
						@click="signUpClick"
					>
						회원가입
					</button>
				</div>
				<div v-else>
					<button class="mx-2 font-bold" @click="logoutClick">로그아웃</button>
					<button
						v-if="!isInProfileCheck"
						class="mx-2 w-40 h-10 font-bold bg-themeyellow rounded-lg"
						@click="goToProfile"
					>
						프로필 페이지
					</button>
					<button
						v-else
						class="mx-2 w-40 h-10 font-bold bg-themeyellow rounded-lg"
					>
						유저 정보 수정
					</button>
				</div>
			</div>
		</nav>
	</div>
</template>

<script>
import NavBarLink from '@/components/Navbar/NavBarLink.vue';
export default {
	name: 'NavBar',
	components: {
		NavBarLink,
	},
	data() {
		return {
			navList: [
				{
					URL: '/finance',
					title: '예 적금 비교',
				},
				{
					URL: '/algorithm',
					title: '추천 알고리즘',
				},
				{
					URL: '/community',
					title: '커뮤니티',
				},
				{
					URL: '/banks',
					title: '은행',
				},
				{
					URL: '/exchange',
					title: '환율',
				},
			],
		};
	},
	methods: {
		loginClick() {
			// console.log(this.$store.state.showLoginState);
			this.$store.commit('showLogin', true);
			console.log('로그인 클릭');
		},
		signUpClick() {
			this.$store.commit('showSignUp', true);
			console.log('회원가입 클릭');
		},
		logoutClick() {
			localStorage.removeItem('token');
			localStorage.removeItem('user');
			console.log('로그아웃');
			this.$router.go(0);
		},
		goToProfile() {
			this.$router.push('/profile');
		},
	},
	computed: {
		isLogined() {
			const token = localStorage.getItem('token');
			return token !== null;
		},
		isInProfileCheck() {
			return this.$store.getters.getProfileCheck;
		},
	},
};
</script>

<style></style>
