# 학생들의 성적을 처리하는 프로그램을 만들기
# 조건 : 사용자로부터 성적을 입력을 받아서 리스트에 저장한다.
# 성적의 평균을 구하고
# 해당 점수가 80점 이상 성적을 받은 학생의 수를 출력하라.
# 출력결과
# 성적을 입력하시오 : 10
# 성적을 입력하시오 : 20
# 성적을 입력하시오 : 60
# 성적을 입력하시오 : 70
# 성적을 입력하시오 : 80
# 성적 평균은 48.0 입니다.
# 80점 이상 성적을 받은 학생은 1 명입니다.
# 학생수는 상수값으로 Student = 5 를 이용한다.

# from math import *

# flags = True
# data = 0
# while flags :
#     scores=[]
#     if data != "q":
#         data = int(input("성적을 입력하세요 : (종료 : q)"))
#         scores.append(data)
#     else:
#         if 
#     print(avg(scores))

#-----------------------------------------------------------

student = 5     # 전역상수 선언
scores = []     # 학생들의 성적을 저장할 리스트
score_sum = 0   # 학생들의 성적 합계를 저장할 변수
scores_aver = 0.0   # 학생들의 성적 평균을 저장할 변수
cnt_80 = 0          # 80점 이상인 학생수 합계를 저장할 변수

for i in range(student):
    score = int(input("성적을 입력하세요 : "))
    scores.append(score)       # 학생들의 성적을 list 에 저장함(append() 이용)
    score_sum += score         # 성적 합계
    if score >= 80:
        cnt_80 += 1

score_aver = score_sum / len(scores)    # 평균을 구함

# 80점 이상 학생수 구하기
print("성적 평균은", score_aver, "입니다.")
print("80점 이상인 학생 수는 ", cnt_80,"명입니다.")
