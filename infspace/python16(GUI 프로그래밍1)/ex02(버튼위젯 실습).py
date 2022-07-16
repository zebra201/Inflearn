# 버튼 위젯 실습
from tkinter import *

window = Tk()   # 루트 윈도우 생성

# 버튼만 생성
button = Button(window, text = "클릭하세요",
                bg = "yellow", fg = "blue", width = 80, height = 20
                , font = "고딕 50")
# 버튼 pack을 해야만 출력
button.pack()


window.mainloop()