# 문제 : data_list = [(90.80),(85.75),(90.100)]
# 튜플을 원소로 하는 리스트를 활용하여 학생의
# 총점과 평균을 소수 첫째자리까지 출력하는 프로그램을 작성하시오.
# enumerate() 함수를 이용한다.
# 출력결과
# 1번 학생의 총점은 170점이고, 평균은 85.0입니다.
# 2번 학생의 총점은 160점이고, 평균은 80.0입니다.
# 3번 학생의 총점은 190점이고, 평균은 95.0입니다.

# def cal():
#     sum = A+B
#     aver = (A+B)/2
#     for i, sum, aver in enumerate(data_list):
#         return ("{}번째 학생의 총점은 {}점이고, 평균은 {}입니다.".format(i, sum, aver))
        
   
# if __name__ == "__main__":
#     data_list = []
#     A = int(input("첫 번째 점수를 입력하세요 : "))
#     B = int(input("두 번째 점수를 입력하세요 : "))
#     data_list = [(A,B)]
#     print(data_list)


data_list = [(90,80),(85,75),(90,100)]
# enumerate() 함수의 역할 : 반복문 사용시 몇 번째 반복을 돌고 있는지 확인할 때 사용한다.
for i, scores in enumerate(data_list):
    # print(i, score)
    hap = 0
    # 학생 1명씩 점수를 누적시킴
    for score in scores :
        hap += score
    print("%d번 학생의 총점은 %d이고, 평균은 %0.1f입니다." % (i+1, hap, hap/2.0))
