import Vue from 'vue';
import VueRouter from 'vue-router';
import store from '@/store/index';
import MainView from '../views/MainView.vue';
import ProfileView from '@/views/ProfileView';
import FinanceView from '@/views/FinanceView';
import CommunityView from '@/views/CommunityView';
import CommunityCreate from '@/views/CommunityCreate';
import CommunityDetail from '@/views/CommunityDetailView';
import BanksView from '@/views/BanksView';
import ExchangeView from '@/views/ExchangeView';

Vue.use(VueRouter);

const routes = [
	{
		path: '/',
		name: 'mainpage',
		component: MainView,
	},
	{
		path: '/profile',
		name: 'profile',
		component: ProfileView,
		meta: { requiresAuth: true },
	},
	{
		path: '/finance',
		name: 'finance',
		component: FinanceView,
	},
	{
		path: '/community',
		name: 'community',
		component: CommunityView,
	},
	{
		path: '/community/create',
		name: 'community-create',
		component: CommunityCreate,
	},
	{
		path: '/community/:id',
		name: 'community-detail',
		component: CommunityDetail,
	},
	{
		path: '/banks',
		name: 'bankspage',
		component: BanksView,
	},
	{
		path: '/exchange',
		name: 'exchange',
		component: ExchangeView,
	},
];

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes,
});

// navigation guard 추가
router.beforeEach((to, from, next) => {
	if (to.matched.some(record => record.meta.requiresAuth)) {
		// requiresAuth 메타 필드가 true로 설정된 경로인지 확인
		// 로그인 여부를 확인하는 로직을 추가하여 적절히 처리
		const isLoggedIn = checkUserLogin(); // 로그인 여부 확인 함수 호출

		if (isLoggedIn) {
			next(); // 로그인 되어 있으면 다음으로 진행
		} else {
			store.commit('showLogin', true);
		}
	} else {
		next(); // requiresAuth가 필요하지 않은 경로는 그냥 진행
	}
});

function checkUserLogin() {
	if (store.user) {
		return false;
	} else {
		return true;
	}
}

export default router;
