# CSV 파일은 split() 메소드를 이용하여 파싱을 할 수 있다.
# CSV 파일을 읽는 프로그램을 작성해보자. (Comma Separated Values )

# data = input("불러올 데이터 이름을 입력하세요 : ")
# data_read = open(data, mode = 'r', encoding = "UTF-8")
# print(data_read)


def main():
    # f_name = open(file="c:\\Temp\\sample.csv", mode = "r", encoding="UTF-8")
    f_name = open(file="c:\\Temp\\sample.csv", mode = "r")
    
    # read() : 파일을 처음부터 끝까지 읽을 떄 사용
    # readline() : 파일의 내용을 한 줄 씩 읽어들일때 사용
    # readlines() : 파일을 읽으면 한 줄, 한 줄이 각각 리스트의 원소로 들어간다.
    
    for line in f_name.readlines():
        # 공백문자 제거하기
        line = line.strip()
        print(line)
        print(type(line))
        
        # 한 라인을 단어로 분리한다.
        words = line.split(",")
        for word in words:
            print("   ", word)
        
        # 사용 후 반드시 종료할 것
    f_name.close()
    
    
if __name__ == "__main__":
    main()