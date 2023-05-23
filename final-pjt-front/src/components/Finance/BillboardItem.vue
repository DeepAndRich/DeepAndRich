<template>
	<li class="billBoardItem h-10 my-2.5 flex items-center justify-center">
		<p class="ranking">{{ ranking }}</p>
		<p>금리:{{ item.intr_rate }}</p>
		<p>{{ item.save_trm }}개월</p>
		<p>{{ calculatedInterest }}원</p>
		<p>{{ calculateTax }}원</p>
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
	},
};
</script>

<style scope>
.ranking {
	color: #f97316 !important;
}
.billBoardItem p {
	font-size: 25px;
	color: #fde047;
	text-shadow: 0px 0px 4px rgba(255, 255, 255, 0.75);
	margin: 0 2rem 0 2rem;
}
</style>
