# 유용한 모듈 사용해보기
# copy 모듈 : 객체를 복사할 때 사용하는 모듈이다.
# 1. 얕은 복사(shallow copy) : 객체의 참조값(주소)만 복사되고 객체는 공유가 되버린다.
# 원본객체에 영향을 끼친다. 완벽한 복사가 아님.
# 2. 깊은 복사(deep copy) : 독립된 객체를 복사해준다.
# 원본 객체에 영향을 미치지 않는다. 완벽한 복사이다.
# ----------------------------------------------

import copy
colors = ["red", "blue", "green"]
clone = copy.deepcopy(colors)   # 깊은 복사가 발생한다.
clone[0] = "빨간색"
print(colors)
print(clone)
print("-"*50)

# random 모듈 사용해보기
# random 모듈 : 난수를 발생할 때 사용하는 모듈이다.
# randint() : 정수 범위의 난수 발생
import random
# 1에서 6사이의 값을 랜덤하게 출려겨해준다.
print("주사위의 눈 :", random.randint(1,6))
# random() -> 0,0 ~ 1.0 미만의 난수를 발생시킨다.
# 범위를 정하고 싶다면 범위의 수를 곱하면 된다.
print("random() : ", random.random()*100)
# randrange(start,stop[,step]) -> start 와 stop 값의 사이의 수를
# 랜덤하게 발생시킨다. stop은 옵션이다
print("randrange(0,101), 0~100 사이 난수 : ", random.randrange(0,101))
print("randrange(0,101), 0~100 사이 3의 배수 난수 : ", random.randrange(0,101,3))
print("-"*50)

# choice() -> 주어진 시퀀스의 항목을 랜덤하게 발생시킨다.
list1 = ["이현호", "김연아", "손연재", "추신수"]
print(random.choice(list1))
print("-"*50)

# shuffle() -> 리스트의 항목을 랜덤하게 섞어주는 함수이다.
list2 = [[x] for x in range(10)]
print("섞기 전 : ", list2)
random.shuffle(list2)
print("섞은 후 : ", list2)
print("-"*50)

# sys 모듈 실습해보기
# sys 모듈은 시스템에 관련된 내용을 파이썬 인터프리터에서
# 다양한 정보를 제공하는 모듈이다
import sys
print("파이썬 설치경로 : ", sys.prefix)
print("파이썬 버전 : ", sys.version)
print("-"*50)

# 타임 모듈
import time
# 1970년 1월 1일 자정이후 지금까지 흐른 시간을 초단위로 출력함
# 프로그램 성능테스트, 단위테스트에 많이 사용된다.
print(time.time())

def fib_num(n):
    a,b = 0,1
    while b < n:
        print(b, end=" ")
        a,b = b, a+b
    print()
    
start = time.time()     # 시작값
fib_num(1000)
end = time.time()
print("fib_num() 실행기간(초) : ", end-start)
print("-"*50)

# asctime() 는 현재 날짜와 시간을 문자열 형태로 표식해준다.
print("현재 날짜 및 시간 : ", time.asctime())
print("-"*50)

# sleep(*) : 프로그램을 일시정지시키는 함수
for i in range(3, 0, -1):
    print(i, end = " ")
    time.sleep(1)      # 1초간 일시정지
print("미사일 발사!")
print("-"*50)

# calender 모듈 사용하기
# 2016.8월 달력 출력해보기
import calendar
cal = calendar.month(2016, 8)
print(cal)