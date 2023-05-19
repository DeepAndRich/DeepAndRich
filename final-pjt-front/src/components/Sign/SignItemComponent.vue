<template>
	<div>
		<input
			class="signItem my-2.5"
			:type="type"
			:placeholder="placeHolder"
			:value="value"
			@input="$emit('input', $event.target.value)"
		/>
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
	width: 350px;
	height: 44px;
	border-radius: 5px;
	/* background: rgba(217, 217, 217, 0.4); */
	border: 0.5px solid #38bdf8;
	border-radius: 5px;
	padding-left: 0.5rem;
}
/* .signItem::placeholder {
	padding-left: 1rem;
} */
/* .signItem:focus-visible {
	border: 2px solid wheat;
} */
.signItem:focus {
	outline: none;
	border-color: #38bdf8;
	box-shadow: 0 0 5px #38bdf8;
}
</style>
