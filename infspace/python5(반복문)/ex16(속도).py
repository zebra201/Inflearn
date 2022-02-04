
# from operator import eq
# speed = ""
# speed_now = 0

# while True:
#     speed = str(input("1.증속, 2.감속, 3.중지 중 하나를 입력하세요 : "))
#     if eq(speed, "1"):
#         speed_now += 10
#     elif eq(speed, "2"):
#         speed_now += -10
#     elif eq(speed, "3"):
#         print("운전이 종료되었습니다. 현재속도는 " + str(speed_now) + "입니다")

# 플래그 변수
run = True # 불리언 타입(객체)이 됨
speed = 0
keyCode = 0

while run :
    print("----------------------------")
    print("1.증속  |  2.감속  |  3.중지")
    print("----------------------------")
    
    # 증속일 경우
    keyCode = int(input("선택 : "))
    if keyCode == 1:
        speed += 10
        print("현재 속도는 : ", speed)
    # 감속일 경우
    elif keyCode == 2:
        speed -= 10
        # 속도가 음수 값으로 나오게 되면
        if speed < 0:
            print("속도는 음수일 수 없습니다. 뒤로 갈까요?")
            speed = 0
        else:
            print("현재 속도는 : ", speed)
    # 중지일 경우 플래그 변수를 False 로 설정해주므로, 무한 루프를 탈출하는 코드
    elif keyCode == 3:
        run = False
        print("현재 속도는 : ", speed)
    # 사용자가 잘못 입력했을 경우
    else :
        print("잘못된 입력값입니다.")
print("프로그램 종료")    
