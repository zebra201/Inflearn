statements = "     안녕!"
# 왼쪽 공백만 제거하는 함수( lstrip() )
print("제거전 문자열 : " + statements)
print("왼쪽 공백제거 : " + statements.lstrip())
print("----------------------------------------")

statements = "    안녕!              "
# 오른쪽 공백만 제거하는 함수( rstrip() )
print("제거전 문자열 : " + statements)
print("오른쪽 공백제거 : " + statements.rstrip())
print("----------------------------------------")

statements = "              안녕!              "
# 양쪽 공백만 제거하는 함수( strip() ), 단 중간 공백은 제거가 안된다.
print("제거전 문자열 : " + statements)
print("양쪽 공백제거 : " + statements.strip())
print("----------------------------------------")


# 문자열 나누기
statements = "나는 열심히 파이썬 공부를 합니다."
print(statements.split())       # 리스트로 반환하여 나뉘어짐.