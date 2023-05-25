<template>
	<div class="profileView flex flex-wrap">
		{{ user.personal_type }}
		<button @click="check">asdfsf</button>
		<div class="w-5/12 flex items-center flex-wrap p-7 text-left">
			<div class="profileImage w-40 h-40 mb-4"></div>
			<div class="w-full">{{ user.nickname }}</div>
			<div class="w-full">{{ user.email }}</div>
			<div class="w-full">{{ user.region }}</div>
			<div class="w-full">{{ user.age }}세</div>
			<div>{{ user.personal_type }}</div>
		</div>
		<div class="w-7/12 p-7">
			<div>
				Lorem ipsum dolor sit amet, consectetur adipisicing elit. Magnam, ut?
				Aspernatur ex, odio expedita molestias dicta ratione velit. Ipsam
				necessitatibus praesentium consequuntur corporis quae quas maiores iste
				id saepe eum?
			</div>
		</div>
		<ProfileSwiper :items="products" />
		<div>
			<ModifyProfileVue />
		</div>
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
			products: [],
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
	methods: {
		check() {
			console.log(this.user, '???');
		},
		getUserProducts() {
			axios
				.get(URL + this.user.pk + '/myproduct/')
				.then(res => {
					console.log(res);
					this.products = res.data;
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
