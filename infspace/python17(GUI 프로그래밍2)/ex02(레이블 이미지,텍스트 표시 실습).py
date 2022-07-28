# 레이블에 이미지와 텍스트를 동시에 나타내기

from tkinter import *

window = Tk()

# window.geotmetry("800x1200")
# PhotoImage 클래스는 jpg 확장자를 지원하지 않음.
photo = PhotoImage(file = "image1.PNG")
# 이미지가 들어가 있는 레이블은 윈도우 우측 배치
lbl = Label(window, image = photo)
lbl.pack(side = RIGHT)
msg = """안녕하세요 파이썬 실습입니다.\n
      안녕하세요 파이썬 실습입니다.\n
      안녕하세요 파이썬 실습입니다."""

# 텍스트를 우측 정렬하여 출력
lbl2 = Label(window, justify=RIGHT,
                    padx = 10,
                    text = msg).pack(side = LEFT)

window.mainloop()