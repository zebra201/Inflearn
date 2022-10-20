# 이론
# 모듈이란 함수나 변수 또는 클래스들을 모아 놓은 파일
# 파이썬에서는 모듈을 불러와서 사용할 수 있다.
# 모듈 안의 함수들은 import 문장으로 다른 모듈로 포함될 수 있다.
# from fibo import fib : fibo 모듈 안에 fib 함수 불러오기
# from fibo import * : fibo 모듈 안 함수 전부 불러오기
# -------------------------------------------------------

# 실습
# 모듈 : 파이썬에서는 모듈(module)은 변수나 함수, 그리고 클래스들을 모아 놓은
# 파일을 모듈이라 한다. 확장자가 반드시 .py가 되어야 한다.
# 모듈을 사용하는 이유가 유지보수를 쉽게하기 위해서 여러 파일로 분리할 수 있다.
# 또한 모듈 정의 및 구현한 함수를 따로 작성하지 않고 불러온 후
# 여러 프로그램에서 사용 가능하다. 이것이 코드의 재활용이다.
# 모듈을 사용하기 위해서는 import 키워드를 사용하여 모듈을 파일로 가져오면 된다.

# fibo 모듈 가져오기
import fibo
# fibo 모듈명, 함수명 호출을 하고 있는 형태이다.
fibo.fib_num(1000)
print(fibo.fib_list(100))
print("-"*50)

# 아래는 모듈에서 특성함수만 가져오고 싶을 때 사용한다.
from fibo import fib_num
from fibo import fib_list
fib_num(1000)
print(fib_list(100))
print("-"*50)

# *(아스타) 라는 것은 fibo 모듈에 있는 모든 것(변수,함수,클래스)을 말한다.
from fibo import *
fib_num(1000)
print(fib_list(100))
print("-"*50)

# 모듈에다가 별칭 붙이기(팀원도 알고 있어야함)
import fibo as f
f.fib_num(1000)
print(f.fib_list(100))