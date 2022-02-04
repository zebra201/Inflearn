# 불리언(bool) 변수 알아보기
# 불리언 변수의 용도는 플래그 변수 형태로 사용을 많이 한다.
# 타 언어에서는 불리언 변수의 값은 소문자로 시작하지만 true, false
# 파이썬에서는 불리언 변수의 값은 대문자로 시작한다. True, False
flag = True
print(type(flag))
print(flag)

# 파이썬에서 bool 변수의 값을 바꾸기 위해서 not 연산자를 이용하면 된다.
flag = not flag
print(type(flag))
print(flag)

if flag:
    print("참이라서 실행.")
else:
    print("거짓이라서 실행.")
    flag = not flag   # flag 가 다시 참으로 변환되고 아래 코드 실행.

    
if flag:
    print("참이라서 실행.")
else:
    print("거짓이라서 실행.")
