from tkinter import *

window = Tk()

counter = 0
# 이벤트 핸들러(콜백함수) 작성
def clicked():
    global counter  # 전역변수 counter 를 사용하겠다 라는 의미
    counter += 1
    # Label 의 text 속성을 변경하고 있다.
    label["text"] = "버튼 클릭 횟수 :" + str(counter)

def reset():
    global counter
    counter = 0
    label["text"] = "버튼 클릭 횟수 :" + str(counter)

if __name__ == "__main__":
    label = Label(window, text = "아직 클릭되지 않았음")
    label.pack()
    
    # label2 = Label(window, text = "초기화")
    # label2.pack()
    
    button = Button(window, text = "증가", command = clicked)
    button.pack()
    
    button2 = Button(window, text = "초기화", command = reset)
    button2.pack()
    
    window.mainloop()