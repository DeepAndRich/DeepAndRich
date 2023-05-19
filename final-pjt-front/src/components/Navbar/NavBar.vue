<template>
	<div class="py-11 px-14 w-full h-36 mx-auto z-30">
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
				<button class="mx-2 font-bold" @click="loginClick">로그인</button>
				<button
					class="mx-2 w-40 h-10 font-bold bg-themeyellow rounded-lg"
					@click="signUpClick"
				>
					회원가입
				</button>
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
					URL: '/bank',
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
	},
};
</script>

<style></style>
