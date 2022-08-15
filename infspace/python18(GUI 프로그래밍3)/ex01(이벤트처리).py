# 이론
# tkinter 응용 프로그램은 대부분의 시간을 이벤트 루프에서 소모한다.
# 즉 mainloop() 에서 이벤트를 기다리면서 반복 루프를 실행한다.
# 이를 이벤트 - 구동방식이라고 한다
# Button-1 : 마우스 좌클릭
# Button-2 : 마우스 휠클릭
# Button-3 : 마우스 우클릭
# 이벤트 처리 : 키보드 이벤트는 현재 키보드 포커스를 소유하고 있는 위젯으로 보내진다.
# focus_set() 메소드를 이용하여 원하는 위젯으로 포커스를 이동시킬 수 있다.
# 이벤트 지정자
# <Double-Button-1> : 마우스 버튼1이 더블클릭될 때 발생.
# <Enter> : 마우스 포인터가 위젯으로 진입하였을 때 발생.
# <Leave> : 마우스 포인터가 위젯을 떠났을 때 발생
# <FocusIn> : 마우스 포인터가 현재의 위젯으로 이동
# <FocusOut> : 마우스 포인터가 현재의 위젯에서 벗어남
# <Return> : 사용자가 엔터키를 입력
# <Key> : 키를 누를 때 발생하며, 이벤트 객체의 char멤버에 저장
# a : a를 눌렀을 때 발생
# <Shift-Up> : 사용자가 시프트 키를 누른 상태로 위쪾 화살표 키를 누르면 발생
# <Configure> : 위젯이 크기를 변경하였을 때 발생, 위젯 위치나 플래폼을 변경해도 발생
# --------------------------------------------------------------

# 실습
# 이벤트 처리에 대한 슬라이드에 있던 코드 실습
# 지금까지는 command 속성을 이용하여 이벤트 처리를 했다면
# bind() 함수를 이용하여 이벤트 처리를 해보도록 하자.
# 문법 : 위젯.bind(이벤트 지정자, 이벤트 처리 함수)

from tkinter import *

window = Tk()
# 이벤트 처리함수 정의
def callback(event):
    print(event.x, event.y, "에서 마우스 이벤트 발생")
    
frame = Frame(window, width = 200, height = 200)
# frame 에 이벤트를 등록하는 것
# 프로그램을 실행하고 마우스 왼쪽 버튼을 클릭했을 때, callback 함수가 실행된다.
frame.bind("<Button-1>", callback)
frame.bind("<Button-2>", callback)  # <Button-2> 휠을 눌렀을 때
frame.bind("<Button-3>", callback)  # <Button-3> 우클릭 했을 때
frame.pack()

window.mainloop()
