# 함수나 변수들을 모아 놓은 파일을 모듈이라고 한다.
# __name__ 은 인터프리터가 실행 전에 만들어 둔 내장 전역변수에 해당한다.
# 문제를 한번에 해결하려고 하지 말고, 충분히 작아질 때까지 작은 크기의 문제들로 분해한다.

# 모듈을 활용하는 첫번째 방법
import fibo

# # fibo.py 모듈의 fib()를 사용하겠다라는 것이다.
# fibo.fib(1000)

# # fibo.py 모듈의 sum()를 사용하겠다라는 것이다.
# print(fibo.sum(10))


# 모듈을 활용하는 두 번 째 방법
# from fibo import fib, sum
# from fibo import *
# fib(100)
# s = sum(10)
# print(s)

# 위 두 방법의 차이점은 import 를 사용하면 파일명.함수명()으로 호출되므로
# 사용한 함수의 출처를 알 수가 있다.
# from fibo import * 를 사용하면 파일명 필요가 없다.
# 함수명으로 바로 호출이 가능하다.

# # __name__ 은 내장 전역변수로 인터프리터가 만들어 놓은 것이다.(import 방식으로 불러와야함)
# print(fibo.__name__)

# # 실행파일에서는 __name__ 이라는 내장전역변수는 __main__ 값을 지니게 된다.
# print(__name__)

def main():
    # fibo.py 모듈의 fib()를 사용하겠다라는 것이다.
    fibo.fib(1000)
    # fibo.py 모듈의 sum()를 사용하겠다라는 것이다.
    print(fibo.sum(10))
    print(fibo.__name__)
    print(__name__)

if __name__ == "__main__":  # 프로그램의 시작점이 되는 형태
    main()


