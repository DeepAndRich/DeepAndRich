<template>
	<div class="profileView flex flex-wrap">
		<div class="w-5/12 flex items-center flex-wrap p-7 text-left">
			<div class="profileImage w-40 h-40 mb-4"></div>
			<div class="w-full">베토디베이컨빼주세요</div>
			<div class="w-full">rlatmddn94@gmail.com</div>
			<div class="w-full">제주특별자치도 제주시</div>
		</div>
		<div class="w-7/12 flex flex-wrap justify-center items-center p-7">
			<div>
				Lorem ipsum dolor sit amet, consectetur adipisicing elit. Magnam, ut?
				Aspernatur ex, odio expedita molestias dicta ratione velit. Ipsam
				necessitatibus praesentium consequuntur corporis quae quas maiores iste
				id saepe eum?
			</div>
		</div>
		<div class="w-full flex justify-around"></div>
		<ProfileSwiper />
	</div>
</template>

<script>
import ProfileSwiper from '@/components/Profile/ProfileSwiper.vue';

export default {
	name: 'ProfileView',
	components: {
		ProfileSwiper,
	},
};
</script>

<style>
.profileView {
	margin: 0 auto 0 auto;
	width: 900px;
	height: 550px;
}
.profileImage {
	background-image: url('@/assets/img/example.jpeg');
	background-position: center;
	background-size: cover;
	border-radius: 100%;
}
</style>
