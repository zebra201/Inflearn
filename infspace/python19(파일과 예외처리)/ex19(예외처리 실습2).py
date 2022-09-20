# 정수를 받고자 할 때의 예외처리
# try:
#     n = int(input("숫자를 입력하세요 : "))
# except ValueError:
#     print("정수가 아닙니다")


# 파일에 대한 예외 처리(읽기)
# try:
#     fname = input("파일 이름을 입력하세요 : ")
#     infile = open(fname, "r")
#     infile.close()
# except FileNotFoundError:
#     print("해당 파일이 존재하지 않습니다.")


# 파일에 대한 예외 처리(쓰기)
# try:
#     infile = open("ex05(test).txt", "w", encoding="UTF-8")
#     infile.write("파일에 내용을 기재합니다.")
# except FileNotFoundError:
#     print("해당 파일이 존재하지 않습니다.")
# # finally 는 예외 상관 없이 무조건 실행
# finally:
#     infile.close()

# 강제로 예외를 발생시키는 구문
raise NameError("비밀번호가 잘못 되었습니다")