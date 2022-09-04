# 파일에 쓰기 실습

# open() 읽기 모드는 파일이 없으면 FileNotFoundError 가 발생한다
# 하지만 모드를 쓰기 모드로 바꾸면 새로운 파일을 생성한다.

# 모드가 쓰기 모드인 경우는 파일이 없을 때는 파일도 생성하고 write() 함수를
# 통해서 데이터를 파일에 보내면 기존에 내용이 있다면 다 지우고 새로 보낸 데이터로 대체된다.
file = open("c:/Temp/input.txt", "w")
file.write("김연아\n")
file.close()
# 추가 모드는 기존에 있던 내용을 그대로 두고 그 뒤에 연결하여 데이터를 추가한다.
file = open("c:/Temp/input.txt", "a")
file.write("이현호\n")
# print 문의 매개변수인 file 을 이용하면 해당 파일에 내용을 추가 할 수 있다.
print("박태환\n", file=file)
file.close()
