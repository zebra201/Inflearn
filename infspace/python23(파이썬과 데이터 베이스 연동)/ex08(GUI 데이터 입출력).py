# GUI(tkinter 모듈 이용) 환경을 만들어서 데이터를 입력, 출력해주는 프로그램 실습

from tkinter import *

if __name__ == "__main__":
    window = Tk()                       # 윈도우 생성
    window.geometry("600x300")          # 화면크기 설정
    window.title("GUI 데이터 입출력")   # 윈도우 제목 설정
    
    editFrame = Frame(window)           # Frame 컨테이너를 윈도우에 생성함.
    # pack()는 기본 값으로 side 매개변수에 TOP 값을 가진다.
    # 하여 위로 정렬시키면서 Frame 컨테이너 속 위젯을 중앙배치한다.
    editFrame.pack()
    
    # 조회결과를 출력할 Frame 컨테이너를 윈도우에 생성함.
    listFrame = Frame(window)
    listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)
    
    # 위젯들 배치(editFrame 배치)
    # Entry 위젯에서 width 속성은 픽셀값이 아니고, 텍스트 단위임을 상기하자.
    edit1 = Entry(editFrame, width=10);   edit1.pack(side=LEFT, padx=10, pady=10)
    edit2 = Entry(editFrame, width=10);   edit2.pack(side=LEFT, padx=10, pady=10)
    edit3 = Entry(editFrame, width=10);   edit3.pack(side=LEFT, padx=10, pady=10)
    edit4 = Entry(editFrame, width=10);   edit4.pack(side=LEFT, padx=10, pady=10)
    
    # 데이터를 저장하는 버튼이며 insertData()를 이벤트 핸들러로 등록함.
    btnInsert = Button(editFrame, text="입력")
    btnInsert.pack(side=LEFT,padx=10,pady=10)
    # 데이터를 조회하는 버튼이며 selectData()를 이벤트 핸들러로 등록함.
    btnSelect = Button(editFrame, text="조회")
    btnSelect.pack(side=LEFT,padx=10,pady=10)
    
    window.mainloop()