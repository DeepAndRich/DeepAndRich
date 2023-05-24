import Vue from 'vue';
import VueRouter from 'vue-router';
import MainView from '../views/MainView.vue';
import ProfileView from '@/views/ProfileView';
import FinanceView from '@/views/FinanceView';
import CommunityView from '@/views/CommunityView';
import CommunityCreate from '@/views/CommunityCreate';
import CommunityDetail from '@/views/CommunityDetailView';
import OthersView from '@/views/OthersView';

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
		path: '/others',
		name: 'otherpage',
		component: OthersView,
	},
];

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes,
});

export default router;
