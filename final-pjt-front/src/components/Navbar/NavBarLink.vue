<template>
	<router-link :to="item.URL" class="mx-2">{{ item.title }}</router-link>
</template>

<script>
export default {
	name: 'NavBarLink',
	props: {
		item: Object,
	},
};
</script>

<style></style>
