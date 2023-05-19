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
	color: #42b983;
}
</style>
