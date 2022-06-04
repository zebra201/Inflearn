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