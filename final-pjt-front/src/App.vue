<template>
	<div id="app">
		<NavBar />
		<ModalComponent :modalState="showLogin">
			<LoginComponent />
		</ModalComponent>
		<ModalComponent :modalState="showSignUp">
			<SignUpComponent />
		</ModalComponent>

		<router-view />
	</div>
</template>

<script>
import axios from 'axios';
import NavBar from './components/Navbar/NavBar.vue';
import ModalComponent from './components/Sign/ModalComponent.vue';
import LoginComponent from './components/Sign/LoginComponent.vue';
import SignUpComponent from './components/Sign/SignUpComponent.vue';

export default {
	components: {
		NavBar,
		ModalComponent,
		LoginComponent,
		SignUpComponent,
	},
	computed: {
		showLogin() {
			return this.$store.state.showLoginState;
		},
		showSignUp() {
			return this.$store.state.showSignUpState;
		},
	},
	created() {
		if (Object.keys(this.$store.state.mainDeposit).length == 0) {
			axios
				.get('http://127.0.0.1:8000/savings/save-saving-products/')
				.then(res => console.log(res))
				.catch(err => console.log(err));
			axios
				.get('http://127.0.0.1:8000/deposits/save-deposit-products/')
				.then(res => console.log(res))
				.catch(err => console.log(err));
			axios
				.get('http://127.0.0.1:8000/exchange/save-exchange-rate/')
				.then(res => {
					console.log(res);
				})
				.catch(err => console.log(err));
			console.log('확인');
		}
		const user = localStorage.getItem('user');
		this.$store.commit('setUser', user);
		if (Object.keys(this.$store.state.mainDeposit).length == 0) {
			const savings = {};
			const deposits = {};
			for (let i = 0; i < 4; i++) {
				let month = 0;
				if (i == 0) {
					month = 6;
				} else if (i == 1) {
					month = 12;
				} else if (i == 2) {
					month = 24;
				} else {
					month = 36;
				}
				axios
					.get(`http://127.0.0.1:8000/savings/saving-products/${month}/`)
					.then(res => {
						console.log(res);
						console.log(month);
						console.log(this.$store.state.MainSavings);
						savings[month] = res.data;
						console.log(savings);
					})
					.catch(err => {
						console.log(err);
					});
				axios
					.get(`http://127.0.0.1:8000/deposits/deposit-products/${month}/`)
					.then(res => {
						deposits[month] = res.data;
						console.log(deposits);
					})
					.catch(err => {
						console.log(err);
					});
			}
			this.$store.commit('saveMainSavings', savings);
			this.$store.commit('saveMainDeposit', deposits);
		}
	},
};
</script>

<style>
#app {
	/* font-family: Avenir, Helvetica, Arial, sans-serif; */
	font-family: LINESeedKR-Bd;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
}

nav {
	padding: 30px;
}

nav a {
	font-weight: bold;
	color: #2c3e50;
}

nav a.router-link-exact-active {
	color: #ffe14e;
}
</style>
