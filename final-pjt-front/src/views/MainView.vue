<template>
	<div class="mainPage mx-auto">
		<div class="mainContainer flex">
			<div class="w-3/12 flex justify-center">
				<TestComponentVue />
			</div>
			<div class="w-3/12 flex justify-center">
				<TestComponentVue />
			</div>
			<div class="w-3/12 flex justify-center">
				<TestComponentVue />
			</div>
			<div class="w-3/12 flex justify-center">
				<TestComponentVue />
			</div>
		</div>
		<div class="mainBtmContainer">
			<button>추천알고르즘으로 가기</button>
		</div>
	</div>
</template>

<script>
import TestComponentVue from '@/components/Main/TestComponent.vue';

export default {
	name: 'MainView',
	components: {
		TestComponentVue,
	},
};
</script>

<style>
.mainPage {
	width: 1250px;
	height: 1000px;
	background-image: linear-gradient(
			rgba(255, 255, 255, 0.3),
			rgba(255, 255, 255, 0.3)
		),
		url('@/assets/img/mainBackground.png');
	background-repeat: no-repeat;
	background-size: cover;
	background-position: top;
	z-index: -2;
}
.mainContainer {
	margin: 0 auto;
	width: 1250px;
	height: 650px;
}
.mainBtmContainer {
	margin: 0 auto;
	width: 1200px;
	height: 350px;
	background-color: #fff;
	box-shadow: -8px 8px 4px rgba(0, 0, 0, 0.25);
	border-radius: 28px;
}
</style>
