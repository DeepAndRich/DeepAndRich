<template>
	<div class="billBoardDetail text-xl flex flex-wrap p-4">
		<BillboardDetailItem />
		<BillboardDetailItem />
		<BillboardDetailItem />
		<BillboardDetailItem />
		<BillboardDetailItem />
	</div>
</template>

<script>
import BillboardDetailItem from './BillboardDetailItem.vue';

export default {
	name: 'BillboardItemDetail',
	components: {
		BillboardDetailItem,
	},
	props: {
		item: Object,
	},
};
</script>

<style>
.billBoardDetail {
	width: 400px;
	height: 500px;
	border: 1.5px solid black;
	border-radius: 10px;
	backdrop-filter: (0, 0, 4px, #fff);
}
</style>
