# 파이썬 파일 현재 위치 확인 및 변경하는 실습
# tell() : 파일의 현재 위치를 확인할 때 사용한다.
# seek() : 파일 현재 위치를 변경할 때 사용한다.
# seek(0) : 파일의 처음 위치로 돌아간다.

file = open("ex05(test).txt", "r", encoding="UTF-8")
print("파일포인터의 현재 위치 : ", file.tell())

print(file.read())
print("파일포인터의 현재 위치 : ", file.tell())
print("-" * 50)

file.seek(0)        # 맨 처음 위치로 돌아가게 하였다.
print("파일포인터의 현재 위치 : ", file.tell())

file.seek(5)        # 파일의 5번째 인덱스 위치로 임의로 가게끔 함.
print("파일포인터의 현재 위치 : ", file.tell())

# 15바이트 만큼 읽어서 출력
# (영문에서는 문제 없음, utf-8 에서는 한글이3바이트로 인식하여 에러발생)
# 이런 이유로 start 인덱스를 0으로 설정하지 않으면 에러 발생
# 인코딩을 ANSI로 저장하면 출력이 잘 됨.
print(file.read(15))

file.close()