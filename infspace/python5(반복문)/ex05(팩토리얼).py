# for 문을 이용하여 팩토리얼(factorial)을 계산하는 프로그램을 작성해보자.
# 팩토리얼(n!) 은 1부터 n까지의 정수를 모두 곱한 것을 의미.
# 구해보는 프로그램을 만들어보자.
# f(1) = 1이다.

fact = 1.0
n = int(input("팩토리얼 값을 구할 정수를 입력 : "))
for i in range(1,n+1):
    fact *= i  # fact = fact * i (복합대입연산자를 사용한 코드)
print(n, "!은 : ", fact)
