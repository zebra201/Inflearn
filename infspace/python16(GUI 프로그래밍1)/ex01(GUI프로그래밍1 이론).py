# # 이론1
# # 파이썬 라이브러리 중 "tkinter"
# # 파이썬에서 그래픽 사용자 인터페이스(GUI) 를 개발할 때 필요한 모듈이다.
# # 유일한 GUI 모듈은 아니지만 현재 가장 많이 사용되는 GUI 모듈이다.
# # 다른 툴킷보다 배우기 쉽고 간편
# # 레이블은 사용자가 볼 수 있지만 상호작용을 할 수는 없다.

# from tkinter import *

# # 루트 윈도우 생성
# # tkinter 모듈 안에 있는 Tk 클래스가 윈도우를 나타낸다.
# window = Tk()

# # 레이블 위젯은 텍스트나 이미지를 표시
# label = Label(window, text = "Hello, World!")

# # pack()은 텍스트를 표시할 정도로만 레이블 위젯 크기를 축소
# # pack() 메소드가 호출되어야 위젯이 화면이 나타난다
# label.pack()

# # pack()이 호출되면 위젯에 나타난다.
# # 윈도우를 닫을 떄까지 이벤트 루프에서 대기
# # window.mainloop()
# # --------------------------------------------------------------

# # 이론2
# # 버튼과 이벤트 처리 : 버튼은 다양한 용도로 사용되는 표준 tkinter 위젯이다
# # 사용자와 상호작용을 할 목적으로 설계된 위젯이다.
# # 반드시 pack()을 호출해야 화면에 벝은이 표시된다.
# b1 = Button(window, text = "이것은 파이썬 버튼입니다.")
# b2 = Button(window, text = "이것은 파이썬 버튼입니다.")
# # padding = 안쪽여백
# # margin = 바깥여백
# # padx = 가로 여백
# # padx = 세로 여백
# b1.pack(side=LEFT, padx=10)
# b2.pack(side=LEFT, padx=10, pady=10)

# # 버튼의 텍스트는 다음과 같이 변경 가능
# b1["text"] = "One"
# # window.mainloop()

# # tkinter 프로그램은 이벤트에 기반을 두고 ㅈ동작
# # 이벤트가 발생하였을때 호출되는 이러한 함수를 콜백함수, 또는 핸들러라고 한다
# # ex --> button = Button(window,text = "one", command = 함수 이름)

# def callback():
#     button["text"] = "버튼이 클릭되었음"

# button = Button(window, text = "클릭", command = callback)
# button.pack(side=LEFT)
# window.mainloop()

# ------------------------------------------------------------
# 실습
# tkinter 라는 모듈을 이용하여 GUI 프로그램 만들기
# tkinter 는 파이썬에서 그래픽 사용자 인터페이스(GUI)를 개발할 때
# 반드시 필요한 모듈이다.

from tkinter import *

# Tk라는 클래스에 생성자 호출
window = Tk()       # 루트 윈도우 생성
# 레이블 위젯을 생성한 것 뿐, 출력은 따로 입력해야함
label = Label(window, text = "Hello tkinter")
# 레이블 위젯을 윈도우에 배치해준다.
label.pack()
window.mainloop()   # 윈도우가 나타나면서 사용자의 동작(이벤트) 대기