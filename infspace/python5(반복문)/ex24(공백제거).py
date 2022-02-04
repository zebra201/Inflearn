# 입력받은 문자열의 모든 공백을 제거한 문자열을 출력하는 프로그램 만들기

# result = ""
# statements = str(input("문자열을 입력하세요 : "))
# for i in statements:
#     if i != " ":
#         result += i
# print("공백을 제거한 문자열 : " + result)

statements = input("원하는 문자열을 입력하세요 : ")
result = ""     # result 라는 string 타입의 변수를 빈 문자열로 초기화해줌. 

for ch in statements:
    # 루프 문자가 공백이 아니라면....
    if ch != " ":
        result += ch
print("입력한 문자열 : " + statements)
print("공백을 제거한 문자열 : " + result)

