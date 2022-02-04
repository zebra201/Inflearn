# 숫자 추측게임을 만들기(반복문 이용)

from random import *
# 1~100까지 임의의 수(난수)를 발생시키는 코드
randnum = randint(1, 100)
print("발생한 난수는", randnum)

user_num = int(input("숫자를 맞추어 보세요. (1~100) : "))
cnt = 0     # 몇 번만에 맞추었는가?
while True: 
    if randnum == user_num:
        cnt += 1
        print("정답입니다! 게임을 종료합니다. 시도횟수 : ", cnt)
        break
    elif randnum > user_num:
        print("랜덤 숫자가 입력값보다 큽니다.")
        cnt += 1        # 파이썬에서는 ++,-- 이런 증감 연산자는 없다. 대신 복합대입연산자를 사용.\
        print("시도횟수 :", cnt)
    else:
        print("랜덤 숫자가 입력값보다 작습니다.")
        cnt += 1
        print("시도횟수 :", cnt)
    user_num = int(input("다시 입력해주세요 : "))