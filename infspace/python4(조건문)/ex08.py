# 사용자로부터 두 개의 정수를 입력받아서 둘 중에서 큰 수를 출력하는 프로그램 만들기

# num1 = int(input("첫 번째 정수를 입력하세요 :"))
# num2 = int(input("두 번째 정수를 입력하세요 :"))
# 내가 만든 공식에는 같은 경우를 고려하지 않았음.
# if num1 > num2:
#     print(num1)
# else:
#     print(num2)
    
    
num1 = int(input("첫 번째 정수를 입력하세요 :"))
num2 = int(input("두 번째 정수를 입력하세요 :"))

maximum = 0
if num1 > num2:
    maximum = num1
else:
    maximum = num2
print("둘 중에 큰 수 : ", maximum)