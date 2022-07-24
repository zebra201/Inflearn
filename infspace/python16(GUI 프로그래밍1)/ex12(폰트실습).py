# 폰트에 대한 실습
# (configure 메서드를 사용하여 변경)
# 모든 위젯이 font라는 속성을 거의 다 가지고 있다.
# 이 font의 속성을 변경하면 폰트로 변경시킬 수 있다.
# 폰트는 미리 객체로 생성해놓고 여러 곳에 사용하면 메모리가 절약된다.

from tkinter import *
from tkinter import font

class App:
    def __init__(self):
        root = Tk()
        # 폰트 지정
        self.customFont = font.Font(family = "궁서", size = 12)
        
        # buttonFrame = Frame()
        label = Label(root, text = "Hello, world, 폰트 변경", font = self.customFont)
        # buttonFrame.pack()
        label.pack()
        
        bigger = Button(root, text = "폰트를 크게", command = self.BigFont)
        smaller = Button(root, text = "폰트를 작게", command = self.SmallFont)

        bigger.pack()
        smaller.pack()
        
        root.mainloop()
        
    def BigFont(self):
        size = self.customFont["size"]
        print("폰트 크게 : ", size)
        # 폰트의 속성을 변경하고자 하면 configure() 사용하면 된다.
        self.customFont.configure(size = size + 2)
        print("폰트 크게 : ",self.customFont)
        
    def SmallFont(self):
        size = self.customFont["size"]
        print("폰트 작게 : ", size)
        self.customFont.configure(size = size - 2)
        print("폰트 작게 : ",self.customFont)
        
if __name__ == "__main__":
    App()