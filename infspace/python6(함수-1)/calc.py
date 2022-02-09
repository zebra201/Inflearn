# 제곱을 계산하여 반환하는 함수

# 함수를 선언 및 구현
def square(num):
    temp = num * num
    return temp     # 반환값 처리


# 두 수 중 큰 값을 리턴
def get_max(x, y):
    # return 문은 최소화하는게 좋은 코드이다.
    temp = 0        # 임시변수 선언
    if x > y :
        temp = x
    else :
        temp = y
    return temp

# 두 수 중 작은 값을 리턴
def get_min(x, y):
    # return 문은 최소화하는게 좋은 코드이다.
    temp = 0        # 임시변수 선언
    if x > y :
        temp = y
    else :
        temp = x
    return temp

# 거듭제곱 구하여 해당하는 값을 반환하는 함수
def power(x,y):
    result = 1  # 지역변수를 0으로 초기화를 하면 거듭제곱 자체가 0이 되어버림.
    for i in range(y):
        result *= x
    return result


