# 사용자로부터 문자열을 입력받아서 알파벳 문자의 개수, 숫자의 개수,
# 스페이스의 개수를 출력하는 프로그램을 작성하시오.

# count_ch = 0
# count_nu = 0
# count_sp = 0

# x = " "
# y = "0123456789"

# statements = input("문자열(영문자, 숫자, 공백)을 입력하세요 : ")
# for letter in statements:
#     if letter in x:
#         count_sp += 1
#     elif letter in y:
#         count_nu += 1
#     else:
#         count_ch += 1
# print("문자의 개수 : {} , 숫자의 개수 : {}, 공백의 개수 : {}".format(count_ch, count_nu, count_sp)) 

statements = input("문자열을 입력하세요(영문자, 숫자, 공백) : ")
alpha_cnt = 0
digit_cnt = 0
spaces = 0

for ch in statements :
    if ch.isalpha():        # 알파벳이라면...
        alpha_cnt += 1
    elif ch.isdigit():      # 숫자라면...
        digit_cnt += 1
    elif ch.isspace():
        spaces += 1
    else : 
        print("해당하는 문자는 알파벳, 숫자, 공백이 아닙니다.")
print("알파벳 문자의 개수 : ", alpha_cnt)
print("숫자 문자의 개수 : ", digit_cnt)
print("공백 문자의 개수 : ", spaces)
