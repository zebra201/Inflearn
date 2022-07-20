# 이론3
# tkinter 위젯 클래스
# Button : 간단한 버튼으로 명령을 수행
# Canvas : 화면에 무언가를 그릴때 사용
# Entry : 한 줄의 텍스트를 입력 받는 필드
# Frame : 컨테이너 클래스 (다른 위젯들을 그룹핑 하는데 사용)
# Label : 텍스트나 이미지를 표시
# Listbox : 선택사항을 표시한다
# Menu : 메뉴를 표시
# Message : 텍스트를 표시
# Scale : 슬라이더를 끌어서 수치값을 입력
# Scollbar : 캔버스, 엔트리 등을 위한 스크롤 바

# 단순 위젯과 컨테이너 위젯
# 배치 관리자 : 컨테이너 안에서 위젯들의 위치와 크기를 결정하는 객체
# -------------------------------------------------------------

# 실습3
# 단순위젯 : Entry 위젯
# Entry 위젯 : 사용자가 키보드로 입력한 내용을 전달하는 위젯, 예를 들면
# 아이디나 패스워드 등 get() 을 사용하면 입력한 내용을 가져올 수 있다.
# 사용자의 입력을 삭제하려면 delete() 사용한다.

from tkinter import *

window = Tk()
window.title("엔트리 위젯 실습")

# entry 위젯은 옆으로 나열하는 방식이므로 높이 설정은 따로 없다.
# 별도로 주고 싶다면
window.geometry("400x200")
entry = Entry(window, fg = "black", bg = "yellow", width = 80)
entry.pack()

window.mainloop()