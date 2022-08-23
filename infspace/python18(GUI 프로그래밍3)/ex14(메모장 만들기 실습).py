# 메모장 만들기
# GUI 만들기

from tkinter import *

top = Tk()
top.title("메모장")
top.geometry("400x400")

ta = Text(top)      # 텍스트 위젯을 생성함
sb = Scrollbar(ta)  # 텍스트 위젯의 스크롤바를 생성함
sb.config(command=ta.yview())   # yview = y축 스크롤바
sb.pack(side=RIGHT, fill=Y)

# 메모장의 기본크기를 설정했지만, 나중에 변경될 수 있기 때문에 설정함.
# Text 위젯이 자동으로 확대 되기 위해서 아래와 같은 코드를 사용
# weight 는 상대적인 크기를 나타내는 매개변수이며 1로 지정하면 전체화면의
# 크기에 맞추어서 확장이 자동으로 이루어진다.
top.grid_rowconfigure(0, weight=1)      # 줄을 전체 크기로 설정함
top.grid_columnconfigure(0, weight=1)   # 열을 전체 크기로 설정함
ta.grid(sticky=N+E+S+W)     # Text 위젯이 좌우 상하를 다 채우도록 고정

# 메뉴 만들기
mb = Menu(top)

# 파일 메뉴를 만드는 코드
fi = Menu(mb, tearoff=False)    # 점선 없애기
fi.add_command(label="새파일")
fi.add_command(label="열기")
fi.add_command(label="저장")
fi.add_separator()      # 분리선 추가
fi.add_command(label="종료")
mb.add_cascade(label="파일", menu=fi)   # 파일 메뉴를 메뉴바에 붙이기

# 편집 메뉴를 만드는 코드
e = Menu(mb, tearoff=False)
e.add_command(label="잘라내기")
e.add_command(label="복사")
e.add_command(label="붙이기")
e.add_command(label="삭제")
mb.add_cascade(label="편집", menu=e)    # 편집 메뉴를 메뉴바에 붙이기

# 도움말 메뉴를 만드는 코드
h = Menu(mb, tearoff=False)
h.add_command(label="메모장 정보")
mb.add_cascade(label="도움말", menu=h)   # 도움말 메뉴를 메뉴바에 붙이기

top.config(menu=mb)
top.mainloop()
