<template>
	<div>
		<button class="signBtn bg-themeBlue my-3.5 font-medium tracking-widest">
			{{ buttonName }}
		</button>
	</div>
</template>

<script>
export default {
	name: 'SignButtonComponent',
	props: {
		buttonName: String,
	},
};
</script>

<style>
.signBtn {
	width: 350px;
	height: 44px;
	border-radius: 5px;
	color: #fff;
	font-size: 20px;
}
</style>
