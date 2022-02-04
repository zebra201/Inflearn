# 사용자로부터 출력하고 싶은 구구단을 출력하는 프로그램을 만들어보자.

# n = int(input("원하는 구구단 수를 입력하세요 : "))
# gugu = 0
# for i in range(1, 10):
#     for j in range(1,n+1):
#         gugu = i * j
#     print(n,"단의", i, "단은", gugu)

# num = int(input("출력하고 싶은 단을 입력하세요 : "))
# for i in range(1,10):
#     print(num, "*", i, "=", (num*i))
    
    
num = int(input("출력하고 싶은 단(2~9)을 입력하세요 : "))

for i in range(1,10):
    # 사용자의 잘못된 입력을 걸러내는 방법.
    if num < 2 or num > 9:
        print("범위가 잘못되었습니다.")
        break
    else:
        print(num, "*", i, "=", (num*i))
