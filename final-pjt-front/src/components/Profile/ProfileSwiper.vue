<template>
	<swiper class="swiper" :options="swiperOption">
		<swiper-slide><ProfileUserProducts /></swiper-slide>
		<swiper-slide><ProfileUserProducts /></swiper-slide>
		<swiper-slide><ProfileUserProducts /></swiper-slide>
		<swiper-slide><ProfileUserProducts /></swiper-slide>
		<swiper-slide><ProfileUserProducts /></swiper-slide>
		<swiper-slide><ProfileUserProducts /></swiper-slide>
		<swiper-slide><ProfileUserProducts /></swiper-slide>
		<swiper-slide><ProfileUserProducts /></swiper-slide>
		<swiper-slide><ProfileUserProducts /></swiper-slide>
		<swiper-slide><ProfileUserProducts /></swiper-slide>
		<swiper-slide><ProfileUserProducts /></swiper-slide>
		<swiper-slide><ProfileUserProducts /></swiper-slide>
		<div class="swiper-pagination" slot="pagination"></div>
	</swiper>
</template>

<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper';
import 'swiper/css/swiper.css';
import ProfileUserProducts from '@/components/Profile/ProfileUserProducts.vue';

export default {
	name: 'swiper-example-mousewheel-control',
	title: 'Mousewheel control',
	components: {
		Swiper,
		SwiperSlide,
		ProfileUserProducts,
	},
	data() {
		return {
			swiperOption: {
				// direction: 'vertical',
				slidesPerView: 6,
				spaceBetween: 30,
				mousewheel: true,
				pagination: {
					el: '.swiper-pagination',
					clickable: true,
				},
			},
		};
	},
};
</script>

<style scoped></style>
