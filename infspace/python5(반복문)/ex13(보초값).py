# 사용자로부터 임의의 개수의 성적을 입력받아서 합계와 평균을 계산한 후
# 출력하는 프로그램을 작성해보시오. 단 sentinel 은 음수의 값을 사용하시오.

# n = 1
# score = 0
# hap = 0
# aver = 0

# score = int(input("점수를 입력하세요 : "))
# while score >= 0 :
#     hap += score
#     aver = (aver+score)/n
#     n += 1
#     print("입력한 값의 합계는 : %d 이고, 평균은 %d 입니다." %(hap, aver))

cnt = 0
hap = 0
score = 0
aver = 0.0
# 센티널(보초값)을 사용자에 제시하는 코드
print("종료하시려면 음수를 입력하세요.(예 : -1)")

while score >= 0 :
    score = int(input(str(cnt+1) + "번째 성적을 입력하세요 : "))
    # 음수값인지 검사하는 코드
    if score >= 0:
        hap += score    # 성적의 합계를 구하는 코드
        cnt += 1        # 학생의 수를 누적하는 코드
# 평균을 계산하고 출력하는 코드
if cnt > 0 :
    aver = hap / cnt
# 합계와 평균을 출력하는 코드
print(str(cnt) + "명의 학생 합계는 %d 입니다." % hap)
print(str(cnt) + "명의 학생 평균은 %0.1f 입니다." % aver)