<template>
	<div>
		<h1>하이</h1>
		<LocationSelectVue />
	</div>
</template>

<script>
import LocationSelectVue from '@/components/LocationSelect.vue';

export default {
	name: 'MainView',
	components: {
		LocationSelectVue,
	},
};
</script>

<style></style>
