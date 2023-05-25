<template>
	<div
		class="square-box cursor-pointer"
		:class="{ expanded: isExpanded }"
		@mouseenter="expandBox"
		@mouseleave="shrinkBox"
	>
		<div v-if="!isExpanded" class="placeholder">{{ name }}</div>
		<div name="flip-list" tag="div" class="list-container">
			<div
				v-for="(item, index) in list"
				:key="index"
				class="list-item p-2"
				:class="{ flipped: isFlipped(index) }"
			>
				<span class="text-left" :class="{ 'list-item-content': !isExpanded }">
					{{ item.fin_prdt_cd.fin_prdt_nm }}</span
				>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	props: {
		name: String,
		list: { type: Array },
	},
	data() {
		return {
			isExpanded: false,
			currentIndex: -1,
		};
	},
	methods: {
		expandBox() {
			this.isExpanded = true;
			this.startFlipping();
		},
		shrinkBox() {
			this.isExpanded = false;
			this.stopFlipping();
		},
		isFlipped(index) {
			return this.isExpanded && index <= this.currentIndex;
		},
		startFlipping() {
			this.currentIndex = 0;
			this.interval = setInterval(() => {
				if (this.currentIndex < this.list.length - 1) {
					this.currentIndex++;
				} else {
					this.stopFlipping();
				}
			}, 500);
		},
		stopFlipping() {
			clearInterval(this.interval);
		},
	},
};
</script>

<style>
.square-box {
	position: absolute;
	margin-top: 4.5rem;
	width: 220px;
	height: 110px;
	background-color: #000;
	border-radius: 8px;
	transition: height 0.5s;
	display: flex;
	/* justify-content: center; */
	/* align-items: center; */
	box-shadow: 0px 0px 4px rgba(255, 255, 255, 0.75);
}

.square-box.expanded {
	height: 15rem !important;
}

.placeholder {
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
	font-size: 24px;
	color: #fde047;
	text-shadow: 0px 0px 4px rgba(255, 255, 255, 0.75);
}

.list-container {
	height: 100%;
	display: flex;
	flex-direction: column;
	justify-content: flex-start;
	/* justify-content: center; */
	/* align-items: center; */
	text-shadow: 0px 0px 4px rgba(255, 255, 255, 0.75);
	text-align: left;
	/* align-items: center; */
}

.list-item {
	width: 100%;
	height: 4rem !important;
	/* text-align: center; */
	color: #000;
	opacity: 0;
	/* background-color: #000; */
	text-align: left !important;
	transition: transform 0.5s;
	transform: rotateX(-180deg);
	list-style-type: none; /* ::marker 제거 */
	margin: 0;
	padding: 0;
	font-size: 20px !important;
}

.list-item-content {
	display: none; /* 초기에 숨겨진 상태로 설정 */
}

.list-item.flipped {
	transform: rotateX(0deg);
	opacity: 1;
	/* color: white; */
	color: #fde047;
	text-shadow: 0px 0px 4px rgba(255, 255, 255, 0.75);
}

/* Flip 애니메이션 설정 */
.flip-list-move {
	transition: transform 0.5s;
	backface-visibility: hidden;
}

.flip-list-enter-active {
	animation: flip-list-enter 0.5s;
}

.flip-list-leave-active {
	animation: flip-list-leave 0.5s;
}

@keyframes flip-list-enter {
	from {
		transform: rotateX(-180deg);
	}
	to {
		transform: rotateX(0deg);
	}
}

@keyframes flip-list-leave {
	from {
		transform: rotateX(0deg);
	}
	to {
		transform: rotateX(-180deg);
	}
}
</style>
