# 1byte(8bit) -> 1Kbyte(1024byte) -> 1Mbyte(1024Kbyte) -> 1G(1024Mbyte) -> 1T(1024Gbyte) -> 1P(1024Tbyte)
# 파이썬에서 리스트는 넓게 보면 시퀀스 자료형에 속한다.
# 시퀀스 요소들은 순서를 가지고 있고, 인덱스를 사용하여 참조할 수 있다.

# 인덱싱이란 리스트에서 하나의 요소를 인덱스 연산자를 통하여 참조(접근)하는 것을 의미한다. 항상 0부터 시작

from re import L


myList = [0,1,2,3,4,5,6,7]
print(myList[3:6])
# [3, 4, 5]

squares = [0,1,4,9,16,25,36,49]
print(squares[3:6])

# 문자열과 다르게 리스트는 변경이 가능하다.

# 시퀀스 자료형 : 순서를 가지는 요소들로 구성된 자료형을 의미한다.
# 문자열, 바이트 시퀀스, 바이트 배열, 리스트, 튜플, range() 객체가 존재한다.
# 시퀀스 자료형의 특징
# 1. 요소들이 순서를 가지고 있다.
# 2. 인덱스를 이요하여 요소들을 참조할 수 있다.

# 문자열에 대한 참조
words = "Nice To Meet You!"
print(words[0], words[5], words[-1])

li = ["사과", "바나나", "복숭아", "토마토"]
# 아래 출력코드는 없는 인덱슬르 참조하므로 에러 발생
# IndexError: list index out of range
# print(li[0], li[5], li[-1])
print(li[0], li[2], li[-1])

# 시퀀스의 길이를 구하는 코드
print("words의 길이 : ", len(words))
print("li의 길이 : ", len(li))

# 시퀀스에서 가능한 연산과 함수
li1 = [1, 2]
print("li1의 주소값 : ", id(li1))
li2 = [3, 4, 5]
print("li2의 주소값 : ", id(li2))
# 시퀀스 자료형은 + 연산이 가능하다.
li3 = li1 + li2
print("li3의 주소값 : ", id(li3))
print(li3)

# *연산자는 시퀀스 자료형에서 해당하는 값을 반복시켜서 요소의 수가 증가가 됨.
print(["안녕", "Hi"] * 3)

# in 연산자는 시퀀스 자료형에 해당하는 값이 있다면 True 를 반환.
print(10 in [10, 2, 3])
# not in 연산자는 시퀀스 자료형에 해당하는 값이 있다면 False 를 반환.
print(10 not in [10, 2, 3])

# 시퀀스 자료형의 최대값
print(max([1,7,-5,15]))
# 시퀀스 자료형의 최소값
print(min([1,7,-5,15]))
# 문자열 리스트에서 max, min 함수는 의미가 없다.
# print(max(["안녕", "Hi", "가나다라"]))

# 반복문의 시퀀스 자료형이 올 수가 있다.
for i in [1,2,3,4,5]:
    print(i)   
for i in "일이삼":
    print(i)

