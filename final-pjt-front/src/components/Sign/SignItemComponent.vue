<template>
	<div>
		<input
			class="signItem my-2.5"
			v-if="!this.$slots.default"
			:type="type"
			:placeholder="placeHolder"
			:value="value"
			@input="$emit('input', $event.target.value)"
		/>
		<slot></slot>
	</div>
</template>

<script>
export default {
	name: 'SignItemComponent',
	props: {
		placeHolder: String,
		type: {
			type: String,
			default: 'text',
		},
		value: String,
	},
	data() {
		return {};
	},
};
</script>

<style>
.signItem {
	width: 355px;
	height: 44px;
	border-radius: 5px;
	/* background: rgba(217, 217, 217, 0.4); */
	border: 0.5px solid #38bdf8;
	border-radius: 5px;
	padding-left: 0.5rem;
	padding-right: 1rem;
}
.signItem:focus {
	outline: none;
	border-color: #38bdf8;
	box-shadow: 0 0 5px #38bdf8;
}
</style>
