<template>
	<div class="recommendQuestions">
		<swiper class="swiper" :options="swiperOption">
			<swiper-slide>
				<h3 class="h-12">주식투자를 하고 있다</h3>
				<label>
					<input type="radio" value="1" v-model="question1" />
					전혀 아니다
				</label>
				<label>
					<input type="radio" value="2" v-model="question1" />
					조금 아니다
				</label>
				<label>
					<input type="radio" value="3" v-model="question1" />
					보통이다
				</label>
				<label>
					<input type="radio" value="4" v-model="question1" />
					조금 그렇다
				</label>
				<label>
					<input type="radio" value="5" v-model="question1" />
					매우 그렇다
				</label>
			</swiper-slide>
			<swiper-slide>
				<h3>당장 큰 돈이 들어갈 일이 있다.</h3>
				<label>
					<input type="radio" value="1" v-model="question2" />
					전혀 아니다
				</label>
				<label>
					<input type="radio" value="2" v-model="question2" />
					조금 아니다
				</label>
				<label>
					<input type="radio" value="3" v-model="question2" />
					보통이다
				</label>
				<label>
					<input type="radio" value="4" v-model="question2" />
					조금 그렇다
				</label>
				<label>
					<input type="radio" value="5" v-model="question2" />
					매우 그렇다
				</label>
			</swiper-slide>
			<swiper-slide>
				<h3>틀에 박힌 반복되는 일이 나를 힘들게 한다.</h3>
				<label>
					<input type="radio" value="1" v-model="question3" />
					전혀 아니다
				</label>
				<label>
					<input type="radio" value="2" v-model="question3" />
					조금 아니다
				</label>
				<label>
					<input type="radio" value="3" v-model="question3" />
					보통이다
				</label>
				<label>
					<input type="radio" value="4" v-model="question3" />
					조금 그렇다
				</label>
				<label>
					<input type="radio" value="5" v-model="question3" />
					매우 그렇다
				</label>
			</swiper-slide>
			<swiper-slide>
				<h3>뚜렷한 취미가 있다.</h3>
				<label>
					<input type="radio" value="1" v-model="question4" />
					전혀 아니다
				</label>
				<label>
					<input type="radio" value="2" v-model="question4" />
					조금 아니다
				</label>
				<label>
					<input type="radio" value="3" v-model="question4" />
					보통이다
				</label>
				<label>
					<input type="radio" value="4" v-model="question4" />
					조금 그렇다
				</label>
				<label>
					<input type="radio" value="5" v-model="question4" />
					매우 그렇다
				</label>
			</swiper-slide>
			<swiper-slide>
				<h3>여행은 포기 못해.</h3>
				<label>
					<input type="radio" value="1" v-model="question5" />
					전혀 아니다
				</label>
				<label>
					<input type="radio" value="2" v-model="question5" />
					조금 아니다
				</label>
				<label>
					<input type="radio" value="3" v-model="question5" />
					보통이다
				</label>
				<label>
					<input type="radio" value="4" v-model="question5" />
					조금 그렇다
				</label>
				<label>
					<input type="radio" value="5" v-model="question5" />
					매우 그렇다
				</label>

				<div>
					<button
						class="w-64 h-12 rounded-lg text-white text-xl mt-8 bg-themeBlue"
						@click="saveAnswers"
					>
						결과 확인하기
					</button>
				</div>
			</swiper-slide>

			<div class="swiper-pagination" slot="pagination"></div>
			<div class="swiper-button-prev" slot="button-prev"></div>
			<div class="swiper-button-next" slot="button-next"></div>
		</swiper>
	</div>
</template>

<script>
import axios from 'axios';
const URL = 'http://127.0.0.1:8000/dj-rest-auth/user/';
import { Swiper, SwiperSlide } from 'vue-awesome-swiper';
import 'swiper/css/swiper.css';

export default {
	data() {
		return {
			question1: '',
			question2: '',
			question3: '',
			question4: '',
			question5: '',
			freestyle: 0,
			backstroke: 0,
			breaststroke: 0,
			butterfly: 0,
			answer: '',
			userToken: localStorage.getItem('token'),
			user: JSON.parse(localStorage.getItem('user')),
			swiperOption: {
				pagination: {
					el: '.swiper-pagination',
					type: 'progressbar',
				},
				navigation: {
					nextEl: '.swiper-button-next',
					prevEl: '.swiper-button-prev',
				},
			},
			// 나머지 질문들에 대한 변수도 동일한 방식으로 선언
		};
	},
	components: {
		Swiper,
		SwiperSlide,
	},
	methods: {
		saveAnswers() {
			// 답변 저장하는 로직을 여기에 작성하면 됩니다.
			if (
				this.question1 == '' ||
				this.question2 == '' ||
				this.question3 == '' ||
				this.question4 == '' ||
				this.question5 == ''
			) {
				alert('아직 체크하지 않은 질문이 있습니다.');
				return;
			}

			this.calculateSecond(this.question2);
			this.calculateThird(this.question3);
			this.calculateFourth(this.question4);
			this.calculateFifth(this.question5);
			if (JSON.parse(this.$store.getters.getUser).asset == 1000) {
				this.freestyle += 100;
				this.breaststroke += 100;
			}
			if (
				this.freestyle >=
				Math.max(this.backstroke, this.breaststroke, this.butterfly)
			) {
				this.answer = 'freestyle';
			} else if (
				this.backstroke >=
				Math.max(this.freestyle, this.breaststroke, this.butterfly)
			) {
				this.answer = 'backstroke';
			} else if (
				this.breaststroke >=
				Math.max(this.freestyle, this.backstroke, this.butterfly)
			) {
				this.answer = 'breaststroke';
			} else {
				this.answer = 'butterfly';
			}
			console.log(this.answer, '확인');
			axios
				.put(
					URL,
					{
						age: this.user.age,
						asset: this.user.asset,
						nickname: this.user.nickname,
						region: this.user.region,
						personal_type: this.answer,
						// realname: this.user.realname,
						realname: '천우희',
					},
					{
						headers: {
							Authorization: `Token ${this.userToken}`,
						},
					},
				)
				.then(res => {
					console.log(res);
					console.log(res, 'why');
					this.$emit('save-type');
					axios
						.get('http://127.0.0.1:8000/dj-rest-auth/user/', {
							headers: {
								Authorization: `Token ${this.userToken}`,
							},
						})
						.then(res => {
							const user = res.data;
							localStorage.removeItem('user');
							localStorage.setItem('user', JSON.stringify(user));
							this.$store.commit('setUser', user);
							this.$store.commit('setModifyProfile', false);
							this.$router.go(0);
						})
						.catch(err => {
							console.log(err);
						});
				})
				.catch(err => {
					console.log(err);
				});
		},
		calculateSecond(score) {
			if (score == 1) {
				this.freestyle += 0;
				this.backstroke += 5;
				this.breaststroke += 5;
				this.butterfly += 5;
			} else if (score == 2) {
				this.freestyle += 2;
				this.backstroke += 3;
				this.breaststroke += 3;
				this.butterfly += 3;
			} else if (score == 3) {
				this.freestyle += 3;
				this.backstroke += 2;
				this.breaststroke += 2;
				this.butterfly += 2;
			} else if (score == 4) {
				this.freestyle += 4;
				this.backstroke += 1;
				this.breaststroke += 1;
				this.butterfly += 1;
			} else {
				this.freestyle += 5;
			}
		},
		calculateThird(score) {
			if (score == 1) {
				this.freestyle += 5;
				this.backstroke += 0;
				this.breaststroke += 5;
				this.butterfly += 0;
			} else if (score == 2) {
				this.freestyle += 4;
				this.backstroke += 1;
				this.breaststroke += 4;
				this.butterfly += 1;
			} else if (score == 3) {
				this.freestyle += 2;
				this.backstroke += 2;
				this.breaststroke += 2;
				this.butterfly += 2;
			} else if (score == 4) {
				this.freestyle += 1;
				this.backstroke += 4;
				this.breaststroke += 1;
				this.butterfly += 4;
			} else {
				this.freestyle += 0;
				this.backstroke += 5;
				this.breaststroke += 0;
				this.butterfly += 5;
			}
		},
		calculateFourth(score) {
			if (score == 1) {
				this.freestyle += 0;
				this.backstroke += 5;
				this.breaststroke += 0;
				this.butterfly += 5;
			} else if (score == 2) {
				this.freestyle += 1;
				this.backstroke += 4;
				this.breaststroke += 1;
				this.butterfly += 4;
			} else if (score == 3) {
				this.freestyle += 2;
				this.backstroke += 2;
				this.breaststroke += 2;
				this.butterfly += 2;
			} else if (score == 4) {
				this.freestyle += 4;
				this.backstroke += 1;
				this.breaststroke += 4;
				this.butterfly += 1;
			} else {
				this.freestyle += 5;
				this.backstroke += 0;
				this.breaststroke += 5;
				this.butterfly += 0;
			}
		},
		calculateFifth(score) {
			if (score == 1) {
				this.freestyle += 0;
				this.backstroke += 5;
				this.breaststroke += 0;
				this.butterfly += 3;
			} else if (score == 2) {
				this.freestyle += 1;
				this.backstroke += 4;
				this.breaststroke += 1;
				this.butterfly += 3;
			} else if (score == 3) {
				this.freestyle += 2;
				this.backstroke += 2;
				this.breaststroke += 2;
				this.butterfly += 2;
			} else if (score == 4) {
				this.freestyle += 3;
				this.backstroke += 1;
				this.breaststroke += 4;
				this.butterfly += 1;
			} else {
				this.freestyle += 3;
				this.backstroke += 0;
				this.breaststroke += 5;
				this.butterfly += 0;
			}
		},
	},
};
</script>

<style scoped>
.recommendQuestions {
	margin: 0 auto;
	width: 900px;
}
.recommendQuestions h3 {
	font-size: 2rem;
	margin-bottom: 1rem;
}
.swiper-slide {
	padding: 3rem 1rem 0 1rem;
}
.recommendQuestions label {
	font-size: 1.5rem;
	margin: 0 1rem;
	cursor: pointer;
}
.recommendQuestions input {
	width: 1rem;
}
.recommendQuestions .swiper {
	height: 16rem;
}
</style>
