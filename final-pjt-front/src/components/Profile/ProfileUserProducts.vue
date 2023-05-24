<template>
	<div class="w-32 h-44 flex items-center flex-wrap justify-center">
		<div>
			<img
				class="h-20 w-20"
				:src="require(`@/assets/img/banks/${bankName}.png`)"
				alt=""
			/>
		</div>
		<div class="h-24 p-2">
			<p>{{ bankName }}</p>
			<p>{{ productName }}</p>
		</div>
	</div>
</template>

<script>
import BANKLIST from '@/assets/json/banklist.json';
export default {
	name: 'ProfileUserProducts',
	props: {
		item: Object,
	},
	data() {
		return {
			bankName: BANKLIST.bankList[this.item.kor_co_nm].name,
			productName: this.item.fin_prdt_nm,
		};
	},
};
</script>

<style></style>
