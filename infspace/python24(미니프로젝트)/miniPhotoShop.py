# 미니 포토샵 만들기
# 외부에서 제공하는 라이브러리를 설치하여 사용하여
# 완성도 높은 프로그램을 제작하는 능력을 키울 수 있다.
# 이미지에 대한 고급 기능은 파이썬에서 제공하지 않지만
# 외부 라이브러리를 이용하여 파이썬 안에서 사용할 수 있게한다.

from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
# 이미지 처리 기능을 제공하는 Pillow 라이브러리를 import 함.
from PIL import Image, ImageFilter, ImageEnhance, ImageOps


# 전역변수 선언 및 초기화
window, canvas, paper = None, None, None
photo, photo2 = None, None
oriX, oriY = 0, 0

def displayImage(img, width, height):
    global window, canvas, paper, photo, photo2, oriX, oriY
    # 화면 크기 설정
    window.geometry(str(width) + "x" + str(height))
    print(str(width) + ", "+ str(height))
    # 기존 canvas 에 출력한 그림이 있다면...
    if canvas != None:
        canvas.destroy()        # canvas 를 깨끗하게 만든다.
    
    # canvas 생성
    canvas = Canvas(window, width=width, height=height)
    paper = PhotoImage(width=width, height=height)
    # 이미지의 폭을 절반 값과 높이의 절반 값의 위치에 이미지를 생성한다.
    canvas.create_image((width/2, height/2), image=paper)
    
    rgbString = ""
    rgbImage = img.convert("RGB")
    # cnt = 0
    
    # 높이와 너비만큼 더블루프를 돌면서 rgb 값을 getpixel()로
    # 추출하여 16진수 형태로 rgbString에 누적시키고 있다.
    for i in range(0, height):
        tmpString = ""
        for j in range(0, width):
            # 복사된 이미지 객체에 getpixel() 를 이용하여 rgb 값을 얻어낼 수 있다.
            r,g,b = rgbImage.getpixel((j, i))
            tmpString += "#%02x%02x%02x " % (r, g, b)   # 반드시 x 값 뒤에 한 칸 공백을 두어야 한다.(중요)
            # cnt += 1
        rgbString += "{" + tmpString + "} "      # } 뒤에 한칸 공백(중요)
    # print(rgbString, "cnt : ", cnt)
    # rgb 문자열 값을 paper 에 대입시키면서 paper 에 이미지를 출력시키고 있다.
    paper.put(rgbString)
    canvas.pack()
        

# 파일 열기
def func_open():
    # photo 는 원본 이미지를 저장할 변수,
    # photo2 는 이미지 처리 후 나타나는 결과 이미지를 저장할 변수,
    # oriX, oriY 는 원본 이미지의 폭과 높이를 저장할 변수
    global window, canvas, paper, photo, photo2, oriX, oriY
    # 파일다이얼로그(열기)를 통하여 원하는 이미지를 사용자가 선택할 수 있도록 한다.
    readFp = askopenfilename(parent = window, filetypes=(("모든 그림 파일", "*.jpg;*.jpeg;*.bmp;*"
                                                          ".png;*.tif;*.gif"),("모든 파일", "*.*")))

    # 파이썬에서 제공하는 PhotoImage() 가 아닌 Pillow 라이브러리에서 제공하는
    # image.open() 함수를 사용하도록 한다.
    # 파이썬에서 제공하는 PhotoImage() 클래스는 이미지 파일의 확장자가
    # .gif, .png 만 지원하므로 한계가 있다.
    # 사용자가 선택한 이미지를 읽고 RGB 모드로 변화시키고 있다.
    photo = Image.open(readFp).convert('RGB')
    # 원본 이미지의 너비와 높이를 저장하고 있다.
    oriX = photo.width
    oriY = photo.height
    
    # 원본 이미지(pillow 라이브러리에 있음) 를 photo2 변수에 복사하여 대입
    photo2 = photo.copy()
    newX = photo2.width
    newY = photo2.height
    print(newX, ",", newY)      # 복사된 이미지의 높이와 너비값을 출력해봄
    # 복사한 내용을 가지고 displayImage() 함수를 호출하고 있다.
    displayImage(photo2, newX, newY)
    
    

# 파일 저장
def func_save():
    global window, canvas, paper, photo, photo2, oriX, oriY
    # photo2 가 None 이라는 것은 복사된 이미지
    # 객체가 없다... 라면 return 을 이용하여 함수를 종료시킴
    if photo2 == None:
        return
    # 파일 다이얼로그(저장)를 띄어서 사용자로부터 파일명을 입력받고 저장하는 방식인데
    # 여기서는 이미지 파일을 저장할 때 기본값으로 .jpg 파일로 저장하게끔 하였다.
    saveFp = asksaveasfile(parent=window, mode="w", defaultextension=".jpg",
                           filetypes=(("JPG 파일","*.jpg;*.jpeg"),("모든 파일", "*.*")))
    # 사용자가 입력한 파일명으로 저장
    photo2.save(saveFp.name)

# 파일 종료
def func_exit():
    exit()

# 확대
def func_zoomin():
    global window, canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("확대배수", "확대할 배수를 입력해주세요.", minvalue=2, maxvalue=5)
    photo2 = photo.copy()
    
    # Pillow 라이브러리에서 제공하는 resize() 함수는
    # 간단하게 이미지를 확대 및 축소를 할 수 있다.
    # 하지만 확대 배수가 너무 크면 메모리나 속도 측면에서 시간이 오래 걸릴수 있다.
    # photo2 에 이미지 사이즈를 변경하여 변경된 이미지 객체를 photo2 에 대입하고 있다.
    photo2 = photo2.resize((int(oriX * scale), int(oriY * scale)))
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)
    
    
# 축소
def func_zoomout():
    global window, canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("축소배수", "축소할 배수를 입력해주세요.", minvalue=2, maxvalue=5)
    photo2 = photo.copy()
    
    photo2 = photo2.resize((int(oriX / scale), int(oriY / scale)))
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

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
    
