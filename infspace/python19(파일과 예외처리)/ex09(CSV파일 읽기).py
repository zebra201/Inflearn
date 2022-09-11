# CSV 파일 읽기
import csv

f = open("ex09(weather).csv", "r")
# CSV 파일은 reader() 함수를 사용해야 한다.
data = csv.reader(f)
# 헤더 제거
header = next(data)

for row in data:
    print(row)
f.close()