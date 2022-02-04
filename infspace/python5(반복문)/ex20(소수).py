# 소수를 2부터 계속 더할때, 2000까지의 루프를 돌리고,
# 소수와 합계 그리고 마지막으로 더해지는 소수는 얼마인지
# 출력하는 프로그램을 작성해보자. 단, 더블루프와 조건식을 사용해야 한다.

# hap = 0
# num = 0
# # result = 0


# for i in range(2,2000):
#     if (i % 2 == 0) or (i % 3 ==0) or (i % 5 == 0):
#         pass
#     elif i == 4 or i == 7:
#        num = i
#        hap += num
#     else:
#         if i <= 2000:
#             num = i
#             hap += num
#         else:
#             print("마지막으로 더할 소수는 :", i-1)
#             break
# print("소수의 총합은 : ", hap)
# hap = 0


start_num = 0
num = 0
hap = 0
lastData = 0

for num in range(2,2001):
    for start_num in range(2, num+1):
        # 배수이거나 소수인지를 걸러내는 조건식
        if num % start_num == 0:
            break
    # 아래 조건이 참이다 라는 것은 자기자신으로 나눠서 나머지
    # 0이 나왔다는 것은 바로 소수를 의미하므로 아래 코드를 실행.    
    if num == start_num:
        print("소수 : ", start_num)
        hap += start_num
        print("합계 : ", hap)
        lastData = start_num
        print("마지막 소수의 값 : ", lastData)
        print("===============================")
        
        
        
        
        
        