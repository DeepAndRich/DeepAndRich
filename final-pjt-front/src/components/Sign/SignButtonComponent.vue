<template>
	<div>
		<button
			class="signBtn my-3.5 font-medium tracking-widest hover:bg-sky-500 focus:outline-none focus:ring focus:ring-themeBlue"
		>
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
	background-color: #38bdf8;
}
</style>
