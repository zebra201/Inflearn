# 지역변수(local variable) : 함수 안에서 선언된 변수, 함수 안에서만 사용
# 전역변수(global variable) : 함수 외부에서 선언된 변수
# 함수 안에서 변수에 어떤 값을 저장하면 무조건 지역변수로 간주한다. 디폴트가 지역변수
# 함수 안에서 전역변수 값을 사용하고 싶다면 global s 코드를 입력하여 사용가능하다.

def test():
    text = "파이썬 공부"       # 지역변수 text에 문자열 할당, 범위는 test() 내에서만 사용
    print(text)                # 출력함수를 이용하여 text를 출력함.
# test()를 호출한 후, "파이썬 공부"라는 문자열을 출력하면서 리턴값은 없다.
test()
# 아래 출력함수에서 NameError: name 'text' is not defined 에러코드 발생
# 이유는 바로 text 변수가 정의되지 않았기 때문이다.
# text 변수는 지역내에서 한번 호출된 후 사라짐.
# print(text)