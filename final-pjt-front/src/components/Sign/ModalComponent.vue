<template>
	<div>
		<div v-if="getShowModal" class="modal" @click.self="closeModal">
			<div class="modal-content">
				<slot> </slot>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	props: {
		modalState: Boolean,
	},
	data() {
		return {
			showModal: this.modalState,
		};
	},
	computed: {
		getShowModal() {
			return this.modalState;
		},
	},
	methods: {
		closeModal() {
			this.showModal = false;
			document.removeEventListener('keydown', this.handleEscapeKey);
			this.$store.commit('showLogin', false);
			this.$store.commit('showSignUp', false);
		},
		handleEscapeKey(event) {
			if (event.key === 'Escape') {
				this.closeModal();
			}
		},
	},
};
</script>

<style>
.modal {
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	background-color: rgba(0, 0, 0, 0.7);
	display: flex;
	justify-content: center;
	align-items: center;
	z-index: 10000;
}

/* .modal-content {
	width: 375px;
	height: 375px;
	padding: 10px;
	background-color: #fff;
	border-radius: 5px;
} */
</style>
