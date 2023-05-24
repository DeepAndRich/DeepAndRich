<template>
	<swiper class="swiper" :options="swiperOption">
		<swiper-slide v-for="item in items" :key="item.id"
			><ProfileUserProducts :item="item"
		/></swiper-slide>
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
	props: {
		items: Array,
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

<style scoped>
.swiper {
	width: 100%;
}
</style>
