from math import *

# 파이썬에서의 자료형(Data-Type)
# int 형을 출력해봄
print(type(18))

# float 형을 출력해봄
print(type(10.7779))

# str형을 출력해봄
print(type("안녕하세요."))

# 반지름이 r 인 구의 부피는 4/3 * pi * r**3 공식
# 반지름이 5인 부피를 계산하는 프로그램

r = 5.0
# volume = (4.0/3.0) * pi * ( r ** 3.0)
volume = (4.0/3.0) * pi * pow(r,3)   # math 를 import 했다면 pow 사용
print("구의 부피 : ", volume)

# print(pi)

# **문자열 + float 은 타입이 일치가 안되어 문자열을 생설할 수 없음.**
# print("구의 부피 : " + volume)
# 해결하기 위한 방안은 문자열 즉, 숫자로 변환이 되지 않는 문자열에다가
# int 함수를 사용해서는 안된다. 또한 + 연산이 이루어지지 않음을 알 수 있다.
# 타입을 일치하게 만들기 위해 volume 을 str()을 이용하여 문자열로 변환하면 가능해진다.
print("구의 부피 : " + str(volume))


# 구의 겉넓이를 구해보자
# volume = (4.0*pi) * (r ** 2.0)
r = 5.0
outer_area = 4.0 * pi * (r ** 2.0)
print("구의 겉넓이 : ", outer_area)
