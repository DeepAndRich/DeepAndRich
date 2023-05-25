<template>
	<li
		@click="handleItemClick"
		class="billBoardItem h-14 my-2.5 flex items-center justify-center"
	>
		<p class="w-1/12 ranking text-center">{{ ranking }}</p>
		<p class="w-2/12">{{ banklist[item.fin_prdt_cd.kor_co_nm].name }}</p>
		<p class="w-3/12">{{ item.fin_prdt_cd.fin_prdt_nm }}</p>
	</li>
</template>

<script>
import BANK_LIST from '@/assets/json/banklist.json';
export default {
	name: 'RecommendListItem',
	props: {
		item: Object,
		ranking: Number,
	},
	data() {
		return {
			banklist: BANK_LIST.bankList,
		};
	},
	methods: {
		handleItemClick() {
			this.$emit('click', this.item);
		},
	},
};
</script>

<style scope>
.ranking {
	color: #f97316 !important;
}
.billBoardItem p {
	font-size: 24px;
	color: #fde047;
	text-shadow: 0px 0px 4px rgba(255, 255, 255, 0.75);
	margin: 0 2rem 0 2rem;
	cursor: pointer;
}
</style>
