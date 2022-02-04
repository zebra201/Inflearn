# 두 개의 정수를 입력받아서 두 수 중에서 더 큰 수를 찾아서
# 리턴하는 함수를 만들어보자.

# 함수의 목록이 정의되어 있는 모듈을 import할 때는
# 항상 개발코드의 상단에 위치해 있어야 한다.
from calc import *

# x,y 가 매개변수라면, 결과로 나온 값 10,20 등은 인수라고 한다.


num1 = int(input("첫 번째 값을 입력하세요 : "))
num2 = int(input("두 번째 값을 입력하세요 : "))
value = get_max(num1,num2)
print("입력된 두 값 : ", num1,",", num2)
print("큰 값 :", get_max(num1,num2))
print("큰 값 :", value)


# 두 개의 정수를 입력받아서 두 수 중에서 더 작은 수를 찾아서
# 리턴하는 함수를 만들어보자.



num1 = int(input("첫 번째 값을 입력하세요 : "))
num2 = int(input("두 번째 값을 입력하세요 : "))
value = get_min(num1,num2)
print("입력된 두 값 : ", num1,",", num2)
print("작은 값 :", get_min(num1,num2))
print("작은 값 :", value)


# 거듭제곱을 구하는 코드
num1 = int(input("거듭제곱 대상 숫자 : "))
num2 = int(input("거듭제곱 횟수 숫자 : "))
value = power(num1,num2)
print("입력된 두 값 : ", num1,",", num2)
print("거듭제곱의 값 :", power(num1,num2))
print("거듭제곱의 값 :", value)