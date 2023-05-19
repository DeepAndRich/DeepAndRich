<template>
	<div>
		<select v-model="selectedProvince" @change="onProvinceChange">
			<option value="">시/도 선택</option>
			<option v-for="province in provinces" :value="province" :key="province">
				{{ province }}
			</option>
		</select>
		<select v-model="selectedDistrict">
			<option value="">구/군 선택</option>
			<option v-for="district in districts" :value="district" :key="district">
				{{ district }}
			</option>
		</select>
	</div>
</template>

<script>
import locations from '@/assets/json/location.json';
export default {
	name: 'LocationSelect',
	data() {
		return {
			data: locations.data,
		};
	},
	computed: {
		selectedProvince: {
			get() {
				return this.value.selectedProvince;
			},
			set(newValue) {
				this.$emit('input', { ...this.value, selectedProvince: newValue });
			},
		},
		selectedDistrict: {
			get() {
				return this.value.selectedDistrict;
			},
			set(newValue) {
				this.$emit('input', { ...this.value, selectedDistrict: newValue });
			},
		},
		provinces() {
			return this.data.map(item => Object.keys(item)[0]);
		},
		districts() {
			const selectedProvinceData = this.data.find(
				item => Object.keys(item)[0] === this.selectedProvince,
			);
			return selectedProvinceData
				? selectedProvinceData[this.selectedProvince]
				: [];
		},
	},
	methods: {
		onProvinceChange() {
			this.selectedDistrict = ''; // Reset selected district when province changes
		},
	},
};
</script>

<style></style>
