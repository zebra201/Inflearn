# 터틀 그래픽을 활용하여 별 모양을 그려보는 프로그램을
# for 문을 이용하여 작성하시오.

import turtle
t = turtle.Pen()

for i in range(5):
    t.forward(150)
    t.right(144) 
# 터틀 종료 방지
turtle.exitonclick()