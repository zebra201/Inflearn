# 파이썬 라이브러리 중 "tkinter"
# 파이썬에서 그래픽 사용자 인터페이스(GUI) 를 개발할 때 필요한 모듈이다.
# 유일한 GUI 모듈은 아니지만 현재 가장 많이 사용되는 GUI 모듈이다.
# 다른 툴킷보다 배우기 쉽고 간편
# 레이블은 사용자가 볼 수 있지만 상호작용을 할 수는 없다.

from tkinter import *

# 루트 윈도우 생성
# tkinter 모듈 안에 있는 Tk 클래스가 윈도우를 나타낸다.
window = Tk()

# 레이블 위젯은 텍스트나 이미지를 표시
label = Label(window, text = "Hello, World!")

# pack()은 텍스트를 표시할 정도로만 레이블 위젯 크기를 축소
# pack() 메소드가 호출되어야 위젯이 화면이 나타난다
label.pack()

# pack()이 호출되면 위젯에 나타난다.
# 윈도우를 닫을 떄까지 이벤트 루프에서 대기
window.mainloop()