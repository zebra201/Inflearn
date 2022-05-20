# counter 모듈 : 시퀀스 자료형의 데이터 값의 개수를 딕셔너리 형태로 반환하는 자료구조이다.
# Counter()에는 값 = 개수형태로 입력이 가능
# 또한 산술/집합 연산이 가능 (단, 음수 값은 출력하지 않는다.)

from collections import Counter

text = "A press release is the quickest and easiest way to get free publicity.".lower().split()
print(Counter(text))