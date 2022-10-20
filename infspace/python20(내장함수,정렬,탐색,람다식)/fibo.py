# 피보나치 수열 모듈 만들기
# 정수 형태로 피보나치 수열을 출력하는 함수
def fib_num(n):
    a,b = 0,1
    while b < n:
        print(b, end=" ")
        a,b = b, a+b
    print()
    
# 리스트 형태로 피보나치 수열로 출력하는 함수
def fib_list(n):
    result = []
    a,b = 0,1
    while b < n:
        result.append(b)    # 순차적으로 리스트에 b 값을 추가한다.
        a,b = b, a+b
    return result