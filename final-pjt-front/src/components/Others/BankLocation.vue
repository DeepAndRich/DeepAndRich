<template>
	<div class="bankLoca flex flex-shrink">
		<div class="flex items-center flex-wrap justify-center w-64 flex-shrink">
			<LocationSelect v-model="selectedLocation" />
			<div>
				<select v-model="selectedBank">
					<option value="">은행 선택</option>
					<option v-for="bank in banks" :value="bank" :key="bank">
						{{ bank }}
					</option>
				</select>
			</div>
			<div class="w-56 flex flex-grow-0" @click="searchBank">
				<SignButton buttonName="검색" />
			</div>
		</div>
		<div id="map"></div>
	</div>
</template>

<script>
import LocationSelect from '../LocationSelect.vue';

import SignButton from '../Sign/SignButtonComponent.vue';
import BANK_LIST from '@/assets/json/banks.json';
const KAKAO_API_KEY = 'ff4a60a02a968cbe4a7c906d776763c8';

export default {
	name: 'KakaoMap',
	components: {
		LocationSelect,
		SignButton,
	},
	data() {
		return {
			selectedLocation: '',
			selectedBank: '',
			map: null,
			markers: [],
			infowindow: null,
			ps: null,
			bankList: BANK_LIST,
		};
	},
	computed: {
		banks() {
			return BANK_LIST.banks;
		},
	},
	mounted() {
		if (window.kakao && window.kakao.maps) {
			this.initMap();
		} else {
			const script = document.createElement('script');
			/* global kakao */
			script.onload = () => kakao.maps.load(this.initMap);
			script.src =
				'//dapi.kakao.com/v2/maps/sdk.js?autoload=false&libraries=services&appkey=' +
				KAKAO_API_KEY;
			document.head.appendChild(script);
		}
	},
	methods: {
		check() {
			console.log(this.selectedLocation, this.selectedBank);
		},
		initMap() {
			const container = document.getElementById('map');
			const options = {
				center: new kakao.maps.LatLng(33.450701, 126.570667),
				level: 3,
			};

			//지도 객체를 등록합니다.
			//지도 객체는 반응형 관리 대상이 아니므로 initMap에서 선언합니다.
			this.map = new kakao.maps.Map(container, options);
		},
		searchBank() {
			this.markers.forEach(marker => marker.setMap(null));
			this.markers = [];
			const ps = new kakao.maps.services.Places();
			ps.keywordSearch(
				`${this.selectedLocation} ${this.selectedBank}`,
				this.placeSearchCB,
			);
			this.ps = ps;
		},
		placeSearchCB(data, status) {
			if (status === kakao.maps.services.Status.OK) {
				// 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
				// LatLngBounds 객체에 좌표를 추가합니다
				const bounds = new kakao.maps.LatLngBounds();

				for (var i = 0; i < data.length; i++) {
					this.displayMarker(data[i]);
					bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
				}
				// console.log(bounds);

				// 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
				this.map.setBounds(bounds);
			}
		},
		displayMarker(place) {
			console.log(place.place_name, 'durl');
			// 마커를 생성하고 지도에 표시합니다
			const iwContent = `<div style="padding:5px;">${place.place_name}</div>`;
			const infowindow = new kakao.maps.InfoWindow({
				zIndex: 1,
				content: iwContent,
			});

			const marker = new kakao.maps.Marker({
				map: this.map,
				position: new kakao.maps.LatLng(place.y, place.x),
				clickable: true,
			});
			// 마커에 클릭이벤트를 등록합니다
			kakao.maps.event.addListener(marker, 'click', function () {
				// 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
				infowindow.setContent(
					'<div style="padding:5px;font-size:12px;">' +
						place.place_name +
						'</div>',
				);
				infowindow.open(this.map, marker);
			});
			this.markers.push(marker);
		},
	},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.bankLoca {
	width: 1250px;
	height: 650px;
}
#map {
	width: 650px;
	height: 550px;
}

.button-group {
	margin: 10px 0px;
}

button {
	margin: 0 3px;
}
select {
	border: 1px solid black;
	border-radius: 5px;
}
</style>
