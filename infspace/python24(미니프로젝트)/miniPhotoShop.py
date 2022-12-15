# 미니 포토샵 만들기
# 외부에서 제공하는 라이브러리를 설치하여 사용하여
# 완성도 높은 프로그램을 제작하는 능력을 키울 수 있다.
# 이미지에 대한 고급 기능은 파이썬에서 제공하지 않지만
# 외부 라이브러리를 이용하여 파이썬 안에서 사용할 수 있게한다.

from tkinter import *

# 전역변수 선언 및 초기화
window, canvas, paper = None, None, None
photo, photo2 = None, None
oriX, oriY = 0, 0

# 파일 열기
def func_open():
    pass

# 파일 저장
def func_save():
    pass

# 파일 종료
def func_exit():
    pass

# 확대
def func_zoomin():
    pass

# 축소
def func_zoomout():
    pass

# 상하반전
def func_mirror1():
    pass

# 좌우반전
def func_mirror2():
    pass

# 회전
def func_rotate():
    pass

# 이미지 밝게
def func_bright():
    pass

# 이미지 어둡게
def func_dark():
    pass

# 블러 처리
def func_blur():
    pass

# 엠보싱 처리
def func_embo():
    pass

# 흑백
def func_bw():
    pass

if __name__ == "__main__":
    window = Tk()       # 윈도우 설정
    window.geometry("250x250")      # 윈도우 크기 설정
    window.title("미니포토샵")
    
    mainMenu = Menu(window)     # 메뉴바를 생성
    window.config(menu = mainMenu)      # 윈도우의 메뉴를 mainMenu 로 설정
    
    # tearoff 속성은 메뉴의 점선을 없애준다.
    fileMenu = Menu(mainMenu, tearoff=False)
    
    # add_cascade() 함수는 상위메뉴와 하위메뉴를 연결해준다(상위메뉴 = mainMenu)
    # 다른 메뉴가 확장이 되어야 되기 때문에 add_cascade() 사용하여 메뉴의 이름을
    # 파일로 설정하였고, menu 속성 값을 fileMenu 로 지정한 것이다.
    mainMenu.add_cascade(label = "파일", menu=fileMenu)
    
    # add_command() 는 메뉴 항목을 생성해준다.
    # 파일 열기 메뉴아이템을 클릭했을 때 func_open() 호출이 된다.
    fileMenu.add_command(label="파일 열기", command=func_open)
    fileMenu.add_command(label="파일 저장", command=func_save)
    # 구분선을 추가하기
    fileMenu.add_separator()
    fileMenu.add_command(label="종료", command=func_exit)
    
    image1Menu = Menu(mainMenu, tearoff=False)
    mainMenu.add_cascade(label="이미지 처리(1)", menu=image1Menu)
    image1Menu.add_cascade(label="확대", command=func_zoomin)
    image1Menu.add_cascade(label="축소", command=func_zoomout)
    image1Menu.add_separator()
    image1Menu.add_cascade(label="상하 반전",command=func_mirror1)
    image1Menu.add_cascade(label="좌우 반전",command=func_mirror2)
    image1Menu.add_cascade(label="회전",command=func_rotate)
    
    image2Menu = Menu(mainMenu, tearoff = False)
    mainMenu.add_cascade(label="이미지 처리(2)", menu=image2Menu)
    image2Menu.add_command(label="밝게", command=func_bright)
    image2Menu.add_command(label="어둡게", command=func_dark)
    image1Menu.add_separator()
    image2Menu.add_command(label="블러", command=func_blur)
    image2Menu.add_command(label="엠보싱", command=func_embo)
    image1Menu.add_separator()
    image2Menu.add_command(label="흑백이미지", command=func_bw)
    
    
    window.mainloop()
    
