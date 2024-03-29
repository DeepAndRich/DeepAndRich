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
		profile: false,
		modifyProfile: false,
		havingProducts: [],
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
		getProfileCheck(state) {
			return state.profile;
		},
		getHavingProducts(state) {
			return state.havingProducts;
		},
		getModifyProfile(state) {
			return state.modifyProfile;
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
		setProfile(state, payload) {
			state.profile = payload;
		},
		setHavingProducts(state, payload) {
			state.havingProducts = payload;
		},
		setModifyProfile(state, payload) {
			state.modifyProfile = payload;
		},
	},
	actions: {},
	modules: {},
});
