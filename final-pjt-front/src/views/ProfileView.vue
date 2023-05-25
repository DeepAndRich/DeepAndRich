<template>
	<div class="profileView flex flex-wrap">
		<div class="modal" v-if="getModifyProfile" @click.self="closeDetail">
			<ModifyProfileVue @profile-modified="updateProfile" />
		</div>
		<div class="w-3/12 flex items-center flex-wrap p-7 text-left">
			<div class="profileImage w-40 h-40 mb-4"></div>
			<div class="w-full">{{ user.nickname }}</div>
			<div class="w-full">{{ user.email }}</div>
			<div class="w-full">{{ user.region }}</div>
			<div class="w-full">{{ user.age }}세</div>
			<div>{{ user.personal_type }}</div>
		</div>
		<div class="w-9/12 p-7">
			<div>안녕하세요</div>
			<div v-if="getUserType">
				<img :src="getUserType" alt="" />
			</div>
			<div v-else>아직 유형이 없습니다.</div>
		</div>
		<ProfileSwiper :items="products" />
	</div>
</template>

<script>
import ProfileSwiper from '@/components/Profile/ProfileSwiper.vue';
import axios from 'axios';
import ModifyProfileVue from '@/components/Profile/ModifyProfile.vue';

const URL = 'http://127.0.0.1:8000/accounts/';

export default {
	name: 'ProfileView',
	components: {
		ProfileSwiper,
		ModifyProfileVue,
	},
	data() {
		return {
			user: JSON.parse(localStorage.getItem('user')),
			userToken: localStorage.getItem('token'),
			products: [],
			userType: 'freestyle',
			showDetail: this.$store.getters.getModifyProfile,
		};
	},
	beforeCreate() {
		this.$store.commit('setProfile', true);
	},
	destroyed() {
		this.$store.commit('setProfile', false);
	},
	created() {
		this.getUserProducts();
	},
	computed: {
		getModifyProfile() {
			return this.$store.getters.getModifyProfile;
		},
		getUserType() {
			console.log(this.userType);
			if (this.userType == null) {
				return false;
			}
			// return this.userType;

			return require(`@/assets/img/${this.userType}.gif`);
		},
	},
	methods: {
		check() {
			console.log(this.user, '???');
		},
		checkModal() {},
		async getUserProducts() {
			await axios
				.get(URL + this.user.pk + '/myproduct/')
				.then(res => {
					console.log(res);
					this.products = res.data;
					this.userType = this.user.personal_type;
				})
				.catch(err => {
					console.log(err);
				});
		},
		openDetail() {
			this.showDetail = true;
			console.log('체크');
		},
		closeDetail() {
			this.$store.commit('setModifyProfile', false);
			this.showDetail = false;
		},
		updateProfile() {
			axios
				.get('http://127.0.0.1:8000/dj-rest-auth/user/', {
					headers: {
						Authorization: `Token ${this.userToken}`,
					},
				})
				.then(res => {
					const user = res.data;
					localStorage.removeItem('user');
					localStorage.setItem('user', JSON.stringify(user));
					this.$store.commit('setUser', user);
					this.$store.commit('setModifyProfile', false);
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
.profileView {
	margin: 0 auto 0 auto;
	width: 850px;
	/* height: 550px; */
}
.profileImage {
	background-image: url('@/assets/img/example.jpeg');
	background-position: center;
	background-size: cover;
	border-radius: 100%;
}
</style>
