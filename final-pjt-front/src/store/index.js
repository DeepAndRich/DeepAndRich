import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		userToken: null,
		user: null,
		showLoginState: false,
		showSignUpState: false,
		mainDeposit: {},
		mainSavings: {},
	},
	getters: {
		getUser(state) {
			return state.user;
		},
		getShowLogin(state) {
			return state.showLoginState;
		},
		getMainDeposit(state) {
			return function (index) {
				return state.mainDeposit[index];
			};
		},
		getMainSavings(state) {
			return function (index) {
				return state.mainSavings[index];
			};
		},
	},
	mutations: {
		setToken(state, payload) {
			state.userToken = payload;
		},
		setUser(state, payload) {
			state.user = payload;
		},
		showLogin(state, payload) {
			state.showLoginState = payload;
		},
		showSignUp(state, payload) {
			state.showSignUpState = payload;
		},
		saveMainDeposit(state, payload) {
			// Vue.set(state.mainDeposit, month, payload);
			state.mainDeposit = payload;
		},
		saveMainSavings(state, payload) {
			state.mainSavings = payload;
			// Vue.set(state.mainSavings, month, payload);
		},
	},
	actions: {},
	modules: {},
});
