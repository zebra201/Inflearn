# 이론
# 잘못된 동작으로 오류가 발생하였을 때
# 프로그램의 오류를 알려주고 복구하는 방법

# 파일의 기초
# RAM(Random Access Memory) : 휘발성 성질
# ROM(Read Only Memory) : 비휘발성 성질
# HDD(Hard Disk Drive) : 플래터와 헤드로 작동하여 파일을 저장
# SSD(Soild State Drive) : HDD 와 다르게 반도체 메로리에 파일을 저장

# 파일은 보조기억장치상에서 논리적인 정보 단위이다.
# 파일 안에는 바이트들이 순차적으로 저장되어 있고 맨 끝에는
# EOF(End-of-File) 마커가 있다. 모든 파일은 입출력 동작이 발생하는 위치를
# 나타내는 파일 포인터를 가지고 있다.

# 이론2
# \ (백슬러시) 는 기호  자체를 의미한다.
# 파일에서 한 줄을 읽으려면 파일 객체가 가지고 있는 readline() 메소드를 호출한다.
# 파일을 열면 파일 포인터가 맨 첫 부분을 가리킨다.
# "w" 모드로 파일을 열었따면 파일에 텍스트를 쓸 수 있다. write() 메소드를 사용
# 파일 작업을 마쳤다면 close()를 호출하여 파일을 닫는다.
# close() 보다 안전한 방법은 try...finally 블록을 사용한다.
# -----------------------------------------------------------------

# 실습1
# 파일은 데이터를 영구적으로 저장하는 형태이다.
# 파일을 다루는 방법에 대해 알아보자.
# 1. 파일을 열기
# open() 내장 함수는 파일을 열고자 할 때 사용하는 함수이다.
file = open("c:\\Temp\\test.txt", "r", encoding="UTF-8")
# readline() 함수는 파일에서 내용을 읽어오는ㄷ네 줄단위 읽어온다.
# 개행문자(\n)까지 가져온다.

line = file.readline().rstrip()
# while line != "":
#     print(line)
#     line = file.readline()
while line != "":
    print(line)
    # rstrip() 메소드는 오른쪽에 공백을 제거하는 함수인데
    # \n, \t 등을 다 제거 해준다.
    line = file.readline().rstrip()
file.close()