# counter 모듈 : 시퀀스 자료형의 데이터 값의 개수를 딕셔너리 형태로 반환하는 자료구조이다.
# Counter()에는 값 = 개수형태로 입력이 가능
# 또한 산술/집합 연산이 가능 (단, 음수 값은 출력하지 않는다.)

from collections import Counter

text1 = "A press release is the quickest and easiest way to get free publicity.".lower().split()
print(Counter(text1))
print("-" * 50)

# 문자열을 가지고 리스트를 생성함
text = list("high school")
print(text)
print(type(text))
# Counter 객체를 만드는데 인자값으로 리스트형을 주었따.
count = Counter(text)
print(type(count))
print(count)
# 시퀀스 자료형에서 어떤 특수문자의 개수를 알고 싶을 때 사용하면 된다.
print(count["h"])
print("-" * 50)

# Counter() 객체를 만들 때, 값=개수 와 같은 형태로 입력도 가능하다
count = Counter(b=2, c=5, a=3)
print(count)
print(sorted(count.elements()))