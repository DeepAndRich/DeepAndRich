<template>
	<div class="bankContainer">
		<BankLocation />
	</div>
</template>

<script>
import BankLocation from '@/components/Others/BankLocation.vue';

export default {
	name: 'BanksView',
	components: {
		BankLocation,
	},
};
</script>

<style>
.bankContainer {
	width: 1200px;
	height: 700px;
	margin: 0 auto;
}
</style>
