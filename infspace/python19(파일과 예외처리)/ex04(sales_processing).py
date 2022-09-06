# sales.txt 파일을 읽어서 총 매출과 평균 일매출을
# 파일로 내보내는 프로그램을 작성하시오.
# 내보내는 파일이름은 summary.txt 로 하시오.

# lines = ""

# with open("ex04(sales).txt", "r") as file:
#     line = file.readline().rstrip()
#     while line != "":
#         print(line)
#         line = file.readline().rstrip()
# ------------------------------------------------------------------

# 사용자로부터 입력 파일 이름과, 출력파일 이름을 입력받는다.
infilename = input("입력 파일 이름 : ")
outfilename = input("출력 파일 이름 : ")

# 입출력을 하기 위해서 파일을 연다.
# 중요한 것은 encoding 부분을 동일하게 가져가야만 글자가
# 깨지는 것을 방지할 수 있으므로 습관을 들여야함 (중요)
infile = open(infilename, "r", encoding="UTF-8")
outfile = open(outfilename, "w", encoding="UTF-8")

# 합계와 횟수를 위한 변수를 정의한다.
sum = 0
count = 0

# 입력 파일에서 한 줄을 읽어서 합계를 계산하고 평균을 구하기 위해서
# count 변수값을 1씩 증가시키고 있다.
line = infile.readline().rstrip()
while line != "":
    sales_num = int(line)
    sum += sales_num
    count += 1
    line = infile.readline().rstrip()

# 총 매출과 평균 일매출을 summary.txt에 기록하고 있다.
outfile.write("총 매출 = " + str(sum) + "\n")
outfile.write("평균 일매출 = " + str(sum/count))

infile.close()
outfile.close()