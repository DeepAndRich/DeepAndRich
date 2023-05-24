<template>
	<div>
		<ul class="h-max text-left">
			<div class="modal" v-if="showDetail" @click.self="closeDetail">
				<BillboardDetail :item="selectedItem" :finance="finance" />
			</div>
			<BillboardItem
				v-for="(item, idx) in paginatedItems"
				:key="item.id"
				:item="item"
				:tax="selectedTax"
				:payment="payments"
				:ranking="idx + 1 + (currentPage - 1) * 10"
				@click="openDetail(item)"
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
import BillboardDetail from './BillboardDetail.vue';

export default {
	name: 'BillboardList',
	components: {
		BillboardItem,
		Pagination,
		BillboardDetail,
	},
	props: {
		items: {
			type: Array,
			required: true,
		},
		selectedTax: String,
		payments: String,
		finance: String,
	},
	data() {
		return {
			currentPage: 1,
			itemsPerPage: 8, // 페이지당 아이템 수
			ranking: 0,
			showDetail: false,
			selectedItem: null,
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
		openDetail(item) {
			this.selectedItem = item;
			this.showDetail = true;
			console.log('체크');
		},
		closeDetail() {
			this.showDetail = false;
		},
		check() {
			console.log('??');
		},
	},
};
</script>

<style></style>
