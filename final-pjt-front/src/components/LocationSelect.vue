<template>
	<div>
		<select class="mx-2" v-model="selectedProvince" @change="onProvinceChange">
			<option value="">시/도 선택</option>
			<option v-for="province in provinces" :value="province" :key="province">
				{{ province }}
			</option>
		</select>
		<select
			class="mx-2"
			v-model="selectedDistrict"
			@change="$emit('input', selectedResult)"
		>
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
			selectedProvince: '',
			selectedDistrict: '',
		};
	},
	props: ['value'],
	computed: {
		selectedResult() {
			const result = `${this.selectedProvince} ${this.selectedDistrict}`;
			return result;
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
