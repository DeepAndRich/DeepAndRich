import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
	state: {
		showLoginState: false,
		showSignUpState: false,
		mainDeposit: [],
		mainSavings: [],
	},
	getters: {
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
		showLogin(state, payload) {
			state.showLoginState = payload;
		},
		showSignUp(state, payload) {
			state.showSignUpState = payload;
		},
		saveMainDeposit(state, payload) {
			state.mainDeposit.push(payload);
		},
		saveMainSavings(state, payload) {
			state.mainSavings.push(payload);
		},
	},
	actions: {},
	modules: {},
});
