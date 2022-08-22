# 파일 열기, 저장 실습

# 파일 열기 filedialog 를 임포트 해야한다.

from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.geometry("400x100")
root.title("파일 저장")

lbl1 = Label(root, text = "저장된 파일이름")
lbl1.pack()

# asksaveasfile() mode="w" 매개변수는 쓰기 모드라는 의미이다.
# defaultextension = ".jpg" 매개변수는 사용자가 확장자를 입력하지 아니하면
# 기본적으로 jpg 확장자를 사용하겠다는 함수이다.
# 파일포인터가 있어서 리소스를 사용하는 것이다.
saveFp = asksaveasfile(parent=root, mode="w", defaultextension=".jpg",
                       filetype=(("jpg파일","*.jpg"),("모든파일","*.*")))
lbl1.configure(text=saveFp)
# 리소스를 사용했다면 반드시 close() 메소드를 호출해줘야 한다.
saveFp.close()


root.mainloop()