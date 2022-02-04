# 입력받은 문자열을 거꾸로 출력하는 프로그램을 작성하시오.


# result = ""
# result2 = ""

# word = input("문자를 입력하세요 : ")
# for ch in word :
#     result += ch
#     for i in result[-1]:
#         result2 += result[-1]
# print("결과 : ", result2)

statements = input("문자열을 입력하세요 : ")
s_reverse = ""
for ch in statements :
    s_reverse = ch + s_reverse
print("입력한 문자열 : " + statements)
print("역순으로 출력한 문자열 : " + s_reverse)
print("--------------------------------------------")

# list() 함수는 문자열을 리스트 타입(문자열 배열, 스트링 타입)으로 바꾸는 함수이다.
s_list = list(statements)
# print(type(s_list)) # => 클래스 list
# reverse() 는 리스트 타입'만'을 역순으로 바꾸어 주는 함수이다
s_list.reverse()
# join() 함수는 역순으로 된 문자열을 연결해서 출력해주는 코드이다.
print("".join(s_list))

print("--------------------------------------------")

s1 = statements
# '문자열에만' 역순으로 하는 함수.
print("".join(reversed(s1)))

# 파이썬에서는 [::-1]를 사용해서 문자열을 역순으로 출력할 수 있다.
print("--------------------------------------------")
print(statements[::-1])

print("--------------------------------------------")
# 문자열 3번째 인덱스부터 역순으로 출력하는 방법.
print(statements[3::-1])
print(statements[3::1])