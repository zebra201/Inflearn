# counter 모듈 : 시퀀스 자료형의 데이터 값의 개수를 딕셔너리 형태로 반환하는 자료구조이다.
# Counter()에는 값 = 개수형태로 입력이 가능
# 또한 산술/집합 연산이 가능 (단, 음수 값은 출력하지 않는다.)

from collections import Counter
from itertools import repeat, chain

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
count = Counter(A=3, b=1, c=5, a=3)
print(count)
# elements() 는 Counter 로 주어진 값의 요소에 해당하는 값을 풀어서 반환을 한다.
# 요소는 무작위적으로 반환하며 요소의 수가 1보다 작을 경우에는
# elements 메서드는 출력하지 않는다. 대소문자를 구별하며 sorted() 정렬이 되어진다.

print(sorted(count.elements()))

# print(list(repeat([1,2,3],3)))
# print(list(chain.from_iterable((repeat(number,3) for number in [1,2,3]))))
print("-" * 50)

a = "가"
b = "나"
# 값 = 개수 형태로 Counter() 객체를 만들 때는 문자열은 매개변수로 쓸 수가 없다.
# 문자열 자체를 맵개변수로 넣어주는 것은 아래와 같이 가능하다.
count = Counter("가나다라가나다라")
print(count)
print(sorted(count.elements()))

print("-" * 50)
# 아래 문자열은 소문자로 다 바뀌고 단어별로 만들어진 리스트가 반환되어진다.
text = "abcdefg abcdefg repeat count! you can do it nice to meet you. A Count" + "telephone!!!!"
text = text.lower().split()
print(text)
print(Counter(text))

print("-" * 50)
count = Counter({"가":4, "나":3})
print(count)
print(count.elements())
# 리스트, 시퀀스 타입으로 element 메서드가 열거해준다.
print(list(count.elements()))