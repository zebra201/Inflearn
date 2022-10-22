# 문제 1
# random 모듈에 있는 함수를 사용하여 7개의 단어 중에서 랜덤하게
# 3개를 선택하여 출력하는 프로그램을 작성하여 보자.

import random
words = []
words.append("파이썬")
words.append("C언어")
words.append("학습")
words.append("프로그램")
words.append("코딩")
words.append("마우스")
words.append("컴퓨터")
print(words)
# ---------------------------------------------------
result = ""
for i in range(0,3):
    result += random.choice(words) + " "
print("추출한 단어 3개 : ", result)
print("-" * 50)

# 문제2
# random 모듈에 있는 함수를 사용하여 알파벳 a부터 z사이에서
# 랜덤하게 10개의 문자를 출력하는 프로그램을 작성하시오.
str1 = "abcdefghijklnmopqrstuvwxyz"
# result2 = ""
# for i in range(0,10):
#     result2 = random.choice(str1)       # 중복 허용
#     # result2 = random.sample(str1, 1)    # 중복 미허용
#     print("알파벳에서 추출한 문자", i+1," : ", result2)
# --------------------------------------------------------
# result2 = ""
# result2 = random.sample(str1, 10)    # 중복 미허용
# print("알파벳에서 추출한 문자 : ", result2)
# --------------------------------------------------------
# 중복된 값을 제외하고 해볼 것(random.choice 를 이용하여)
result2 = ""
data = []
while True:
    result2 = random.choice(str1)
    if result2 not in data:
        data.append(result2)
    if len(data)==10:
        break
    
print("알파벳에서 추출한 문자", data)
print("-" * 50)        

# --------------------------------------------------------

# 문제3
# 100과 200 사이에서 5개의 짝수 난수를 발생시키는 프로그램을 작성하시오
print("100~200 사이 짝수 난수 5개 : ", 
      random.sample([i for i in range(100,201) if i%2 == 0], 5))