<template>
	<div>
		<ul class="h-max">
			<BillboardItem
				v-for="(item, idx) in paginatedItems"
				:key="item.id"
				:item="item"
				:tax="selectedTax"
				:payment="payments"
				:ranking="idx + 1 + (currentPage - 1) * 10"
			/>
		</ul>
		<Pagination
			:currentPage="currentPage"
			:totalPages="totalPages"
			@page-changed="handlePageChange"
		/>
	</div>
</template>

<script>
import BillboardItem from './BillboardItem.vue';
import Pagination from '@/components/Finance/PaginationComponent.vue';

export default {
	name: 'BillboardList',
	components: {
		BillboardItem,
		Pagination,
	},
	props: {
		items: {
			type: Array,
			required: true,
		},
		selectedTax: String,
		payments: String,
	},
	data() {
		return {
			currentPage: 1,
			itemsPerPage: 10, // 페이지당 아이템 수
			ranking: 0,
		};
	},
	computed: {
		totalItems() {
			return this.items.length;
		},
		totalPages() {
			return Math.ceil(this.totalItems / this.itemsPerPage);
		},
		paginatedItems() {
			const startIndex = (this.currentPage - 1) * this.itemsPerPage;
			const endIndex = startIndex + this.itemsPerPage;
			return this.items.slice(startIndex, endIndex);
		},
	},
	methods: {
		handlePageChange(page) {
			this.currentPage = page;
		},
	},
};
</script>

<style></style>
