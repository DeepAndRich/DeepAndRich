import Vue from 'vue';
import VueRouter from 'vue-router';
import MainView from '../views/MainView.vue';
import OthersView from '@/views/OthersView';

Vue.use(VueRouter);

const routes = [
	{
		path: '/',
		name: 'mainpage',
		component: MainView,
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
