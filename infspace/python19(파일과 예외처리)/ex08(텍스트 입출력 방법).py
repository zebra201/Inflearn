# 이론
# 다양한 텍스트 파일 입출력 방법
# for-each 구문 :  파일을 문자열들이 저장되어 있는 시퀀스(컨테인너) 객체로 볼 수 있다.
# 다시 읽으려면 파일을 닫았다가 열어야한다.
# 파이썬은 strip() 함수를 잘 사용하면 공백을 제거할 수 있다.
# 단어에 들어 있는 모든 문장 부호들을 제거하고 싶으면
# word = word.rstrip(".,?!")
# 파일 read() 함수는 한번에 읽을 수 있지만 모든 문자가 하나의 거대한 문자열로 반환되므로
# 많은 양의 메모리가 소모되므로 좋은 방법은 아니다.
# readlines() 함수, 메소드는 각 줄이 저장된 리스트를 반환한다.
# ------------------------------------------------------------

# 실습
# for 문
# infile = open("ex05(test).txt", encoding="UTF-8")
# for line in infile:
#     print(line)

# 단어를 분리하기
# infile = open("ex08(proverbs).txt", "r")
# # 파일도 시퀀스 객체임
# for line in infile:
#     line = line.rstrip()        # 오른쪽 공백문자 제거
#     word_list = line.split()    # 단어를 분리
#     for word in word_list:
#         print(word)
# infile.close()

# 구분자를 지정해서 단어를 출력
# line = "apple,grape,banana,pear"
# word_list = line.split(",")
# print(word_list)

# 한문자씩 출력하기
infile = open("ex05(test).txt", "r", encoding="UTF-8")
ch = infile.read(1)
while ch != "":
    print(ch)
    ch=infile.read(1)
infile.close()