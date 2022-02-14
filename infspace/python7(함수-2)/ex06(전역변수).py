# 전역변수(global variable) : 함수의 외부에 정의된 변수를 전역변수라고 칭한다.
# 파이썬에서는 전역변수를 다루는 형태가 타 언어들에 비해서 접근방식이라는 측면에서는
# 융통성이 떨어진다.

# def test():
#     print(text)     # test() 함수 내에 text 란느 지역변수가 없을 때는 전역 변수를 가져와서 사용한다.

# text = "파이썬을 공부합니다"    # 전역변수인 text 변수에 문자열 할당
# test()


# def test():
#     # test() 함수 내에 text 라는 지역변수가 없을 때는 전역 변수를 가져와서 사용한다.
#     # NameError: name 'text' is not defined 발생함 그 이유는 test() 호출시
#     # text 가 정의되어 있지 않기 때문에 에러가 발생
#     print(text)

# test()
# text = "파이썬을 공부합니다"    # 전역변수인 text 변수에 문자열 할당

def test():
    # 지역변수 text 변수에 문자열 할당, 전역변수 text도 할당이 되어 있지만
    # 함수 내에서는 지역변수가 무조건 출력된다. 그 이유는 바로 함수 내에서는
    # 지역변수가 디폴트 이기 때문이다.(중요)
    text = "파이썬 공부"
    print(text)             # 지역변수 text 값을 출력

text = "자바를 공부"    # 전역변수 text 에 문자열 할당
test()
# 지역변수 text는 함수 호출 후 소멸되었기에 전역변수인 text 의 문자열 출력
print(text)


