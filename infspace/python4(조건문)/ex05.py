# 사용자에게 명령어를 입력받아서 터틀그래픽을 제어해 보자.
# 즉, 사용자가 "left"을 입력을 하면, "right"를 입력했다면 오른쪽으로
# 회전하는 프로그램 만들기

import turtle

# 펜의 기능을 t라는 변수에 저장함.
t = turtle.Pen()

# 반복문을 무한루프 돌려서 if 구문을 이용하여 방향을 제어하는 코드
# 통상적으로 while 은 무한루프를 돌 때 사용.(끝날때까지 계속 실행)
# 무한루프를 프로그래밍 했다면 반드시 *루프를 탈출하는 코드*가 반드시 필요.
while True:     # True 일때 계속 돈다
    direction = input("왼쪽=left, 오른쪽=right, 종료=quit 입력 :")
    # break 는 무한루프를 나가는 키워드이다.
    if direction == 'quit':
        print("종료되었습니다.")
        break
    # 사용자가 left를 입력했을때,
    if direction == 'left':
        print("Left 입력")
        t.left(60)
        t.forward(50)
    # 사용자가 right를 입력했을때,
    if direction == 'right':
        print("Right 입력")
        t.right(60)
        t.forward(50)
# 터틀 그래픽 창이 클릭이 되어야 화면이 사라지게 하는 함수이다.
turtle.exitonclick()