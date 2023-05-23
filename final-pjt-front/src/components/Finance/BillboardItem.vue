<template>
	<li
		@click="handleItemClick"
		class="billBoardItem h-14 my-2.5 flex items-center justify-center"
	>
		<p class="w-1/12 ranking text-center">{{ ranking }}</p>
		<p class="w-2/12 text-center">{{ calculatedInterest }}원</p>
		<p class="w-2/12 text-center">{{ calculateTax }}원</p>
		<p class="w-3/12">{{ item.fin_prdt_cd.kor_co_nm }}</p>
		<p class="w-3/12">{{ item.fin_prdt_cd.fin_prdt_nm }}</p>
	</li>
</template>

<script>
export default {
	name: 'BillboardItem',
	props: {
		item: Object,
		payment: String,
		tax: String,
		ranking: Number,
	},
	data() {
		return {
			payments: Number(this.payment),
		};
	},
	computed: {
		calculatedAmounts() {
			// console.log(this.ranking);
			const interest = (this.payments * this.item.intr_rate) / 100;
			return interest;
		},
		calculatedInterest() {
			return this.formatAmount(this.payments + this.calculatedAmounts);
		},
		calculateTax() {
			const tax = parseFloat(this.tax);
			const caculatedInter =
				this.calculatedAmounts - (this.calculatedAmounts * tax) / 100;
			return this.formatAmount(Math.round(this.payments + caculatedInter));
		},
	},
	methods: {
		formatAmount(amount) {
			return amount.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
		},
		handleItemClick() {
			// 클릭 이벤트 처리 로직
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
