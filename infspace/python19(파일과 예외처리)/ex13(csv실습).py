# 최저 기온 구하기
import csv

f = open("ex09(weather).csv", "r")
data = csv.reader(f)
# 헤더를 제거하기
header = next(data)
temp = 1000

for row in data:
    if temp > float(row[3]):    # 최저 기온은 3번 인덱스에 존재
        temp = float(row[3])
        
print("가장 추웠던 온도는 ", temp, "입니다.")
f.close()