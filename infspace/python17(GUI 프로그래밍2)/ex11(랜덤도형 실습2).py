
from tkinter import *

class Canvas_Shape:
    def __init__(self):
        window = Tk()
        window.title("여러가지 도형 그리기")
        
        # 윈도우 창에 캔버스를 만들고 배치함.
        self.canvas = Canvas(window, width=600, height=400, bg="white")
        self.canvas.pack()
        # 여러가지 버튼을 배치하는 Frame 컨테이너를 생성하고 윈도우에 배치하기
        # window, bg = "black", width=600, height=100
        frame = Frame()
        frame.pack()
        # 도형을 만들어 주는 여러가지 버튼을 생성하여 Frame 에 배치하기(이벤트 처리 연결)
        btnRectangle = Button(frame, text="사각형", command = self.displayRect)
        btnOval = Button(frame, text="원", command = self.displayOval)
        btnArc = Button(frame, text="호", command = self.displayArc)
        btnPolygon = Button(frame, text="다각형", command = self.displayPolygon)
        btnLine = Button(frame, text="선", command = self.displayLine)
        btnString = Button(frame, text = "문자열", command = self.displayString)
        btnClear = Button(frame, text = "전체삭제", command=self.clearCanvas)
        
        # 위에서 만든 버튼을 격자형으로 배치한다.
        btnRectangle.grid(row = 1, column = 1)
        btnOval.grid(row = 1, column = 2)
        btnArc.grid(row = 1, column = 3)
        btnPolygon.grid(row = 1, column = 4)
        btnLine.grid(row = 1, column = 5)
        btnString.grid(row = 1, column = 6)
        btnClear.grid(row = 1, column = 7)
        
        window.mainloop()

        
    # 멤버 메서드를 구현
    def displayRect(self):
        # tags 위젯 특정 부분에 이름을 추가, 속성 및 식별자가 되기도 하고 그룹화가 가능하다.
        self.canvas.create_rectangle(10,10, 190,90, tags = "rect")
    
    def displayOval(self):
        self.canvas.create_oval(10,10, 190,90, fill = "red", tags = "oval")
        
    def displayArc(self):
        self.canvas.create_arc(10,10, 190,90, start=0, extent=90, fill = "red", tags = "arc")
        
    def displayPolygon(self):
        self.canvas.create_polygon(10,10, 190,90, 30,50, fill = "blue", tags = "polygon")
        
    def displayLine(self):
        self.canvas.create_line(10,10, 190,90, fill = "red", width = 5, tags = "line")
        # activefill 속성은 라인에 색상을 바꾸게 해주는 것이다.
        # arrow 속성은 first, end, last(시작, 끝, 양끝지점) 화살표 속성으로 나타낸다.
        self.canvas.create_line(10,10, 190,10, width=5, arrow = "last", activefill="blue", tags = "line")
        
    # 문자열 출력
    def displayString(self):
        self.canvas.create_text(60,10, text = "여기서는 여러가지 도형을 그립니다.",
                                font = ("Times 10 bold underline"), tags="string")
    
    # 그림제거
    def clearCanvas(self):
        self.canvas.delete("rect","oval","arc","polygon","line","string")
        
    
        
        
if __name__ == "__main__":
    Canvas_Shape()