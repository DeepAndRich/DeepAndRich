<template>
	<div class="w-32 h-40 flex items-center flex-wrap justify-center">
		<div>
			<img class="h-20 w-20" src="@/assets/img/banks/신한.png" alt="" />
		</div>
		<div>
			<p>제주은행</p>
			<p>다드림예금</p>
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
			bankName: BANKLIST.bankList,
		};
	},
};
</script>

<style></style>
