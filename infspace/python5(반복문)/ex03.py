# 1부터 사용자가 입력한 수 num까지 더하여 합계를 구하는 프로그램을
# for 문을 이용해서 작성하시오.

hap=0
num=int(input("숫자를 입력하세요 : "))
for i in range(1,num+1):      # stop 값이 들어가지 않기 때문에 +1
    hap += i
print("1부터", num, "까지의 정수의 합계 : ", hap)


