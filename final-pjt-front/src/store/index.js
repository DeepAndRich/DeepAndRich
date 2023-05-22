import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		showLoginState: false,
		showSignUpState: false,
	},
	getters: {
		getShowLogin(state) {
			return state.showLoginState;
		},
	},
	mutations: {
		showLogin(state, payload) {
			state.showLoginState = payload;
		},
		showSignUp(state, payload) {
			state.showSignUpState = payload;
		},
	},
	actions: {},
	modules: {},
});
