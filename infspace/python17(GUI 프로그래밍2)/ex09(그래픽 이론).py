# 캔버스 위젯 생성 이후 그림그리기 가능.
# Canvas() 생성자를 호출

# from tkinter import *
# window = Tk()
# w = Canvas(window, width = 300, height = 200)
# w.pack()

# window.mainloop()

# 선과 사각형 그리기(canvas.create_rectangle)
# 왼쪽 상단의 좌표는 (0,0) 이다.

# 색상의 경우 영어를 사용하거나, color picker 로 코드를 사용가능하다.
# fill 은 채우기 색상, outline 은 경계선 색상
# tkinter.colorchoose 모듈의 askcolor() 사용가능

# canvas.create_line() : 직선을 그리는 메소드
# canvas.create_rectangle() : 사각형을 그리는 메소드
# canvas.create_arc(10,10,100,150, extent=90) : 사각형에 내접한 원이 그려지고 원중에서 90도만 그려진다
# canvas.create_oval() : 타원은 지정된 사각형 안에 그린다
# canvas.create_polygon() : (10, 10)에서 출발하여 (150, 110)으로 가고 최종적으로 (250,20)에서 종료
# canvas.create_text(100,20, text = "테스트테스트", fill = "blue", font =("고딕",20)) :
    # 텍스트의 중앙 위치를 나타내는 (x,y) 좌표 생상 표시하는 fil, 폰트 매개변수 font
    
# ------------------------------------------------------------------------

# 캔버스 생성하여 직선, 원, 사각형, 다각형 등 실습하기
# 캔버스 위젯은 파이썬에서는 그래픽 기능을 제공하는 것이다.

from tkinter import *

window = Tk()
# window.geometry("700x700")
canvas = Canvas(window, width = 500, height = 500, bg = "white")
canvas.pack()

# 선을 그려본다
# 선에서 fill 은 색상이고, width 는 선의 굵기가 된다.
canvas.create_line(0,0, 500,500, fill = "blue")
canvas.create_line(0,500, 500,0, fill = "red", width = 5)
# 사각형을 그려본다.
# 사각형에서 fill 은 채우기 색상이고, width 는 바깥선의 굵기가 되고
# outline 값은 바깥선의 색상이 된다.
canvas.create_rectangle(50,50, 200,200, fill = "yellow")
canvas.create_rectangle(200,200, 300,400, fill = "red", outline="blue", width = 10)

window.mainloop()