# 이론

# 레이블
# 기본적으로 텍스트를 표시하는 위젯이지만 이지미도 함께 표시할 수 있다.
# PhotoImage 클래스의 생성자에 이미지 파일의 이름을 주면 이미지 파일을 객체로 만들 수 있다.

# 엔트리 위젯
# tkinter의 기본 위젯 중의 하나이며, 사용자가 입력한 한 줄 텍스트 문자열을 가져오는데 사용한다.
# 두 줄 텍스트를 가져오려면 텍스트 위젯을 사용한다.
# ---------------------------------------------------------------------------------

# Label 에 대한 실습
# Label 위젯에 이미지 표시하기
# (JPG 등 안되는 확장자가 있으므로 주의할것)

from tkinter import *

window = Tk()

# 이미지 인스턴스를 생성하여 photo 변수에 저장
# file = 에 이름을 주면 인스턴스를 생성
photo = PhotoImage(file = "image1.PNG")
lbl = Label(window, image=photo)
# 이미지 객체를 레이블에서 참조를 얻는 것이다.
lbl.photo = photo
lbl.pack()

window.mainloop()