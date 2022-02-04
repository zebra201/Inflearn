# for문 : 정해진 횟수만큼 반복하는 구조(자주 사용, 쉬움)
# while 문 : 어떤 조건이 만족되는 동안, 반복을 계속하는 구조(통상, 무한루프용, break가 필요)
# 문자열이나 리스트가 바로 시퀀스

for x in range(5):  # 리스트에 대한 반복
    print("hello Python")
    
for name in ["철수","영희","길동","유신"]:
    print("안녕!" + name)
    
# print(x, end=" ") -> 변수 x 의 값을 출력한 후 줄을 바꾸지 말고 출력해라.

for x in range(10):
    print(x, end=" ")
    
for x in [0,1,2,3,4,5,6,7,8,9]:
    print(x, end=" ")
    
sum = 0
for x in range(10):
    sum += x
    # sum = sum + x
print(sum)

# range() 함수는 start 부터 stop-1 까지의 step의 간격으로 정수들을 생성.
sum = 0
for x in range(0,10):   # stop 값은 포함하지 않음. 10-1 = 9 까지의 리스트
    sum = sum + x
print(sum)

