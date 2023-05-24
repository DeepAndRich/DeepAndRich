<template>
	<div
		class="billBoardTitle w-full rounded-lg h-16 text-center bg-black flex items-center justify-center"
	>
		<span class="w-1/12">순위</span>
		<span class="w-2/12">세전이자</span>
		<span class="w-2/12">세후이자</span>
		<span class="w-2/12 pr-16">금융기관</span>
		<span class="w-3/12 pr-16">상품명</span>
		<!-- <span class="w-1/12"></span> -->
	</div>
</template>

<script>
export default {
	name: 'BillboardTitle',
	props: {
		month: String,
	},
	computed: {
		selectedMonth() {
			if (this.month < 2) {
				console.log(this.month);
				const dummy = Number(this.month) * 6 + 6;
				return dummy;
			} else if (this.month == 2) {
				return 24;
			} else {
				return 36;
			}
		},
	},
};
</script>

<style scope>
.billBoardTitle span {
	margin: 0 2rem 0 2rem;
	color: #38bdf8;
	font-size: 25px;
	text-shadow: 0 0 4px rgba(255, 255, 255, 0.5);
}
</style>
