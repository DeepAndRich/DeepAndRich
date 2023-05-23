<template>
	<nav class="pagination">
		<ul class="flex">
			<!-- <li :class="{ disabled: currentPage === 1 }">
				<button
					@click="goToPage(currentPage - 1)"
					:disabled="currentPage === 1"
				>
					Previous
				</button>
			</li> -->
			<li
				v-for="page in totalPages"
				:key="page"
				:class="{ active: page === currentPage }"
			>
				<button @click="goToPage(page)">{{ page }}</button>
			</li>
			<!-- <li :class="{ disabled: currentPage === totalPages }">
				<button
					@click="goToPage(currentPage + 1)"
					:disabled="currentPage === totalPages"
				>
					Next
				</button>
			</li> -->
		</ul>
	</nav>
</template>

<script>
export default {
	name: 'PaginationComponent',
	props: {
		currentPage: {
			type: Number,
			required: true,
		},
		totalPages: {
			type: Number,
			required: true,
		},
	},
	methods: {
		goToPage(page) {
			if (page >= 1 && page <= this.totalPages) {
				this.$emit('page-changed', page);
			}
		},
	},
};
</script>

<style scoped>
.pagination {
	display: flex;
	justify-content: center;
	margin-top: 1rem;
}

.pagination ul {
	list-style: none;
}

.pagination li {
	margin: 0 0.25rem;
}

.pagination button {
	display: inline-block;
	font-size: 20px;
	padding: 0.5rem 1rem;
	font-style: italic;
	/* border: 1px solid #ddd;
	border-radius: 4px; */
	/* background-color: #fff; */
	color: #fff;
	cursor: pointer;
	text-shadow: 0px 0px 4px rgba(255, 255, 255, 0.75);
}

.pagination li.disabled button {
	cursor: not-allowed;
	opacity: 0.5;
}

.pagination li.active button {
	text-decoration: underline;
}
</style>
