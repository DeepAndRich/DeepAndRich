<template>
	<div>
		<h3>질문 1: 주식투자를 하고 있다</h3>
		<label>
			<input type="radio" value="1" v-model="question1" />
			1점
		</label>
		<label>
			<input type="radio" value="2" v-model="question1" />
			2점
		</label>
		<label>
			<input type="radio" value="3" v-model="question1" />
			3점
		</label>
		<label>
			<input type="radio" value="4" v-model="question1" />
			4점
		</label>
		<label>
			<input type="radio" value="5" v-model="question1" />
			5점
		</label>

		<!-- 나머지 질문들에 대한 라디오 버튼도 동일한 방식으로 작성 -->

		<!-- 예시로 질문 2 추가 -->
		<h3>질문 2: 당장 큰 돈이 들어갈 일이 있다.</h3>
		<label>
			<input type="radio" value="1" v-model="question2" />
			1점
		</label>
		<label>
			<input type="radio" value="2" v-model="question2" />
			2점
		</label>
		<label>
			<input type="radio" value="3" v-model="question2" />
			3점
		</label>
		<label>
			<input type="radio" value="4" v-model="question2" />
			4점
		</label>
		<label>
			<input type="radio" value="5" v-model="question2" />
			5점
		</label>

		<h3>질문 3: 틀에 박힌 반복되는 일이 나를 힘들게 한다.</h3>
		<label>
			<input type="radio" value="1" v-model="question3" />
			1점
		</label>
		<label>
			<input type="radio" value="2" v-model="question3" />
			2점
		</label>
		<label>
			<input type="radio" value="3" v-model="question3" />
			3점
		</label>
		<label>
			<input type="radio" value="4" v-model="question3" />
			4점
		</label>
		<label>
			<input type="radio" value="5" v-model="question3" />
			5점
		</label>

		<h3>질문 4: 뚜렷한 취미가 있다.</h3>
		<label>
			<input type="radio" value="1" v-model="question4" />
			1점
		</label>
		<label>
			<input type="radio" value="2" v-model="question4" />
			2점
		</label>
		<label>
			<input type="radio" value="3" v-model="question4" />
			3점
		</label>
		<label>
			<input type="radio" value="4" v-model="question4" />
			4점
		</label>
		<label>
			<input type="radio" value="5" v-model="question4" />
			5점
		</label>

		<h3>질문 5: 여행은 포기 못해.</h3>
		<label>
			<input type="radio" value="1" v-model="question5" />
			1점
		</label>
		<label>
			<input type="radio" value="2" v-model="question5" />
			2점
		</label>
		<label>
			<input type="radio" value="3" v-model="question5" />
			3점
		</label>
		<label>
			<input type="radio" value="4" v-model="question5" />
			4점
		</label>
		<label>
			<input type="radio" value="5" v-model="question5" />
			5점
		</label>

		<!-- 나머지 질문들도 동일한 방식으로 작성 -->

		<!-- 저장 버튼 -->
		<button @click="saveAnswers">저장</button>
	</div>
</template>

<script>
import axios from 'axios';
const URL = 'http://127.0.0.1:8000/dj-rest-auth/user/';

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
			// 나머지 질문들에 대한 변수도 동일한 방식으로 선언
		};
	},
	methods: {
		saveAnswers() {
			// 답변 저장하는 로직을 여기에 작성하면 됩니다.
			console.log('질문 1의 답변:', this.question1);
			console.log('질문 2의 답변:', this.question2);

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
			axios
				.put(
					URL,
					{
						age: this.user.age,
						asset: this.user.asset,
						nickname: this.user.nickname,
						region: this.user.region,
						personal_type: this.answer,
						realname: '와!',
					},
					{
						headers: {
							Authorization: `Token ${this.userToken}`,
						},
					},
				)
				.then(res => {
					console.log(res);
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
