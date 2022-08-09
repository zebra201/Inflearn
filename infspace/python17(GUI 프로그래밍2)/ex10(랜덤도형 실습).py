# 랜덤하게 사각형을 윈도우창에 나타내기 실습

import random
from tkinter import *
from tkinter import colorchooser


window = Tk()
canvas = Canvas(window, width = 600, height = 500, bg = "white")
canvas.pack()

# 8개의 색상을 리스트로 생성
color = ["red", "orange", "black", "yellow","blue", "violet", "green","purple"]

def draw_rect():
    # canvas.delete(ALL)
    x = random.randint(0, 600)
    y = random.randint(0, 500)
    w = random.randrange(100)
    h = random.randrange(100)
    
    # random.choice() 함수는 매개변수로 들어간 시퀀스 자료형의
    # 인덱스를 무작위로 랜덤하게 생성해준다.
    # canvas.create_rectangle(x, y, w, h, fill = random.choice(color))
    
    # 퀴즈 : colorchooser 를 이용하여 사각형의 색상을 사용자로부터
    # 입력받아서 배경색으로 지정하는 부분의 코드를 작성해보시오.
    color = colorchooser.askcolor()
    canvas.create_rectangle(x, y, w, h, fill = color[1])
    
def delete_rect():
    canvas.delete(ALL)

# for i in range(10):
#     draw_rect()

button = Button(window, text = "사각형 그리기", width=20, height=5, command = draw_rect)
button.pack(side = LEFT)

button1 = Button(window, text = "모두 지우기", width=20, height=5, command = delete_rect)
button1.pack(side = LEFT)


window.mainloop()