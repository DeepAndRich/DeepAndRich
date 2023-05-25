<template>
	<div>
		<ul class="h-max text-left">
			<div class="modal" v-if="showDetail" @click.self="closeDetail">
				<BillboardDetail
					:item="selectedItem"
					:finance="finance"
					@product-modified="closeDetail"
				/>
			</div>
			<RecommendListItem
				v-for="(item, idx) in items"
				:key="item.id"
				:item="item"
				:ranking="idx + 1 + (currentPage - 1) * 10"
				@click="openDetail(item)"
			/>
		</ul>
	</div>
</template>

<script>
import BillboardDetail from '@/components/Finance/BillboardDetail.vue';
import RecommendListItem from './RecommendListItem.vue';

export default {
	name: 'RecommendItemList',
	components: {
		RecommendListItem,
		BillboardDetail,
	},
	props: {
		items: {
			type: Array,
			required: true,
		},
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
	methods: {
		openDetail(item) {
			this.selectedItem = item;
			this.showDetail = true;
			console.log('체크');
		},
		closeDetail() {
			this.showDetail = false;
		},
	},
};
</script>

<style></style>
