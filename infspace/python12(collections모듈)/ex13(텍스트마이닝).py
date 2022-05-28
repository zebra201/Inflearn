# 텍스트 마이닝 기법
from wsgiref.simple_server import demo_app


def file_read(text):
    f_name = open("c:\\Temp\\law.txt", mode = "r", encoding = "UTF-8")
    for line in f_name:
        words = line.strip().split()
        for word in words:
            if len(word) >= 2:
                text.append(word)
    print("단어분활 : ", text)


if __name__ == "__main__":
    # 기본값으로 초기화하는 모듈
    from collections import defaultdict
    # 순서를 가지게하는 모듈
    from collections import OrderedDict
    text = []
    file_read(text)
    word_count = defaultdict(lambda : 0) # 값을 0으로 초기화
    # text 에 담긴 단어들의 빈도수를 증가시키는 부분
    for word in text:
        word_count[word] += 1
    
    for i, v in OrderedDict(sorted(word_count.items(), key = lambda t : t[1], reverse=True)).items():
        if v >= 2:
            print(i,v)