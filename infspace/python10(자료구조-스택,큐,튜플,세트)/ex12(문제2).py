# 문제 : 텍스트 파일을 읽어서 단어를 얼마나 사용하여
# 문서를 작성하였는지를 계산하는 프로그램을 작성하시오.
# 출력결과
# 입력 파일 이름 : words.txt
# 사용된 단어의 개수 : 18
# {'travels', 'half', 'that', 'news', 'alls', 'well', 'fast', 'feather', 
#  'flock', 'bad', 'together', 'ends', 'is', 'a', 'done', 'begun', 'birds', 'of'}

# 단어에서 마침표를 제거하고 소문자로 만드는 함수.
def process(word):
    out_str = ""
    for ch in word:
        # 영문자라면...
        if ch.isalpha() :
            out_str += ch
    # 단어를 소문자로 리턴해준다.
    return out_str.lower()


if __name__ == "__main__":
    # 빈 세트를 만든다
    words = set()
    filename = input("입력 파일 이름 : ")
    # 파일을 열고 읽기 모드로 설정함.
    file = open(filename, mode = "r")
    
    # 파일의 모든 줄에 대해서 반복한다.
    for line in file :
        # 한 라인을 읽어와서 단어(토큰)별로 분리하고 있다.
        linewords = line.split()
        for word in linewords:
            # 단어를 세트에 추가한다.
            words.add(process(word))

    # process 라는 함수를 추가하여 단어 뒤의 "." 을 제거한다.
    print("사용된 단어의 개수 :", len(words))
    print(words)
    file.close()