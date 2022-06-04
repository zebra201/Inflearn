# while 문과 리스트 객체의 pop()을 이용해
# 80점 이상의 점수들의 총합을 구하시오.

# student=[85,65,77,83,75,22,98,88,38,100]
# i=0
# sum=0
# while i <= 9:
#     if student[i] < 80:
#         student.pop(i)
#     else:
#         sum=sum+student[i]
#         i=i+1
# print(sum)


student=[85,65,77,83,75,22,98,88,38,100]
i = -1
sum = 0
while i < 9:
    i += 1
    if student[i] < 80:
        print(student[i])
        continue
    sum=sum+student[i]
print(sum)

print("-" * 50)

student=[85,65,77,83,75,22,98,88,38,100]
i = len(student)
sum=0
while i > 0:
    i = i - 1
    if student[i] < 80:
        student.pop(i)
    else:
        sum += student[i]
print(sum)



# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# num = -1
# sum = 0
# while num < 9:
# 	num += 1
# 	if A[num] < 50: continue
# 	sum = sum + A[num]
# print(sum)