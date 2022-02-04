# 더블 루프를 이용하여 아래와 같이 출력하는 프로그램을 작성하시오.
# 출력결과
#      *
#     ***
#    *****
#   *******
#  *********

# 1. 더블 루프 사용

for i in range(1,6):
    # 공백을 찍는 내부 루프
    for j in range(5-i):
        print(" ", end="")
    # 별표를 찍는 부분
    for k in range(1, i*2):
        print("*", end="")
    # 줄바꿈
    print("")
    
    
  
print("-"*50) # 다음 문제와 구분

for i in range(1, 11, 2):
    # 중앙정렬을 위해서는 ^ 특수문자를 사용하면 된다.
    print("{:^10}".format("*"*i))
    
    
# 더블 루프를 이용하여 아래와 같이 출력하는 프로그램을 작성하시오.
# 출력결과
#      *
#     ***
#    *****
#   *******
#  *********
#  *********
#   *******
#    *****
#     ***
#      *

print("-"*50) # 다음 문제와 구분
# 상단 삼각형 부분
for i in range(1,6):
    for j in range(5-i):
        print(" ", end="")
    for k in range(1, i*2):
        print("*", end="")
    print("")

# 하단 역삼각형 부분
for i in range(5):
    for j in range(i):
        print(" ", end="")
    for k in range(10, (2*i)+1, -1):
        print("*", end="")
    print("")