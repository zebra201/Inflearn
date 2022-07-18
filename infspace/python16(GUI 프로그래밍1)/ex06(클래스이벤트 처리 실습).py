# 클래스로 만들어서 이벤트 처리 방법
# 클래스로 프레임을 감싸는 방법
# 아래와 같은 방법은 규모가 있는 프로그램을 작성할 때는
# 코드를 클래스로 감싸는 것이 좋다

from tkinter import *

class App:
    def __init__(self):
        window = Tk()
        helloB = Button(window, text = "Hello", command = self.hello, fg = "red")
        helloB.pack(side = LEFT)
        quitB = Button(window, text = "Quit", command = self.quit)
        quitB.pack(side = LEFT)
        window.mainloop()
        
    def hello(self):
        print("Hello 버튼이 클릭되었음!")
    
    def quit(self):
        print("Quit 버튼이 클릭되었음!")
        
if __name__ == "__main__":
    # 앱에서 인스턴스만 생성하면됨 (클래스에서 이미 코드 작성)
    App()
        