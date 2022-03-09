# 리스트 함축(컴프리헨션)은 포함, 함축, 내포, 축약 등을 의미한다.
# 아주 간결하게 리스트를 생성할 수 있다는 장점
# *튜플은 소괄호()로 만들어진 변경 불가능한 객체
# for문 실행 후 if문 실행한다.

list1 = ["All", "good", "things", "must", "come","to","an","end"]
items = [word[0] for word in list1]
print(items)


# 리스트 함축
# 리스트 함축은 수학에서 집합을 정의하는것과 매우 유사하다.

# 일반적인 코드(리스트 함축을 사용하지 않은 경우)
squares = []
for x in range(1,11):
    squares.append(x ** 2)
print(squares)

# 리스트 함축 개념을 이용하여 위와 똑같은 결과 출력하기
# 위으 일반적인 코드보다 코드가 간결하고 쉽게 리스트를 생성할 수 있다.
# 리스트 함축 문법 : 출력식 반복문
li_squares = [x**2 for x in range(1,11)]
print(li_squares)

# 조건이 붙는 리스트 함축(조건문 if를 사용하겠다)
# 조건식이 참이 되는 것만 리스트 요소로 생성시킨다.
odd_list = [x for x in range(1, 21) if x % 2 == 1]
print("홀수 : ", odd_list)

even_list = [x for x in range(1, 21) if x % 2 == 0]
print("짝수 : ", even_list)

# 반복문 2번을 사용하여 구구단의 값을 출력해보자(for문을 많이 사용한다면 자리구분을 하면 좋다)
gugudan_list = [(i * j) for i in range(2,10)
                        for j in range(1,10) ]
print("구구단의 값 : ", gugudan_list)