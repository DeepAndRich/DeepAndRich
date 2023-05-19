import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import './assets/css/tailwindcss.css';
import '@/assets/css/tailwindcss.css';
import '@/assets/css/font.css';

Vue.config.productionTip = false;

new Vue({
	router,
	store,
	render: h => h(App),
}).$mount('#app');
