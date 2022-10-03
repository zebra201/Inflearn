# 내장함수와 람다식을 이용한 예제
# 1. map() 와 람다식
list1 = [1,2,3,4,5]
f = lambda x : x * 2        # 리스트의 각각의 요소에 2를 곱하여 리턴해준다.
result = map(f, list1)
print(list(result))
print("-"*50)

# 2. filter() 와 람다식
list2 = [1,2,3,4,5,6]
# filter() : 어떠한 조건이 참이면 그 조건만 반환해줌
result = filter(lambda x : x % 2 == 0, list2)
print(list(result))
print("-"*50)

# 람다식은 정렬할 때 기준이 되는 키를 지칭할 때도 많이 사용한다.
data = [(1,100),(1,300),(1,200),(2,200)]
print(sorted(data, key=lambda data : data[0]))
print("-"*50)

# 3. reduce(func, seq) : func() 함수를 seq(시퀀스)에
# 연속적으로 적용하여 단일 값을 반환한다.
# reduce()와 람다식을 이용한 예제
import functools
result = functools.reduce(lambda x, y : x * y, [1,2,3,4])
print(result)