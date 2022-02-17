# 원의 면적과 원의 둘레를 구하는 프로그램을 작성하는데
# PI = 3.141592 전역 상수를 선언하고 상수를 활용하도록 한다
# 원의 면적 : PI * r^2,
# 원의 둘레 : 2 * r * PI


# def cal(r):
#     area = PI * (r**2)
#     circum = 2 * r * PI
#     print("원의 면적 : ", area)
#     print("원의 둘레 : ", circum)
#     return

# PI = 3.141592
# r = float(input("반지름을 입력하세요 : "))
# cal(r)


# 전역 상수를 선언
PI = 3.141592

# 프로그램 시작하는 함수
def main():
    radius = float(input("원의 반지름을 입력하세요 : "))
    print("반지름이", radius, ", 원의 면적 : ", circleArea(radius))
    print("반지름이", radius, ", 원의 둘레 : ", circleCircumference(radius))

# 원의 면적을 구하는 함수를 선언 및 구현
# 원의 면적 공식 : PI * radius의 제곱
def circleArea(radius):
    return PI * radius * radius

# 원의 둘레를 구하는 함수를 선언 및 구현
# 원의 둘레 공식 : 2 * PI * radius
def circleCircumference(radius):
    return 2 * PI * radius

# 프로그램의 시작을 알리는 메인함수 호출
main()