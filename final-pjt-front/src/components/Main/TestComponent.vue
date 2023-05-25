<template>
	<div
		class="square-box"
		:class="{ expanded: isExpanded }"
		@mouseenter="expandBox"
		@mouseleave="shrinkBox"
	>
		<transition-group name="flip-list" tag="div" class="list-container">
			<div
				v-for="(item, index) in list"
				:key="index"
				class="list-item"
				:class="{ flipped: isFlipped(index) }"
			>
				{{ item }}
			</div>
		</transition-group>
	</div>
</template>

<script>
export default {
	data() {
		return {
			isExpanded: false,
			list: [
				'Item 1',
				'Item 2',
				'Item 3',
				'Item 4',
				'Item 5',
				'Item 6',
				'Item 7',
			],
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
	top: 181px;
	width: 220px;
	height: 110px;
	background-color: #fff;
	transition: height 0.5s;
}
.hoverCheck {
	display: none;
}

.square-box.expanded {
	height: 400px;
}

.list-container {
	height: 100%;
	display: flex;
	flex-direction: column;
	justify-content: flex-start;
	align-items: center;
	display: block;
}

.list-item {
	width: 100%;
	height: 50px;
	text-align: center;
	color: #000;
	background-color: #000;
	transition: transform 0.5s;
	transform: rotateX(-180deg);
}

.list-item.flipped {
	transform: rotateX(0deg);
	color: white;
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
