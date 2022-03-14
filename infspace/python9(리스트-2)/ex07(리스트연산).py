# 일반적인 리스트 연산들 실습
# 최소값과 최대값을 구하는 알고리즘

s = [-10, -50, 100, 50, -7.2, -60]
min1 = s[0]
for i in range(1, len(s)):
    if min1 > s[i]:
        min1 = s[i]
print("최소값 : ", min1)


# 아래 코드는 이미 앞서서 배운바 있다.
# 내장함수를 이용하여 최소값 최대값을 구하는 코드이다.
num = [1,5,-9,100]
print("최소값 : ", min(num))
print("최대값 : ", max(num))
print("----------------------------------------")

# 최대값과 최소값을 구하는 알고리즘은 상당히 중요한 개념이다.
# 아래의 코드를 이해하도록 하자.
price = [1000,3000,500,10000,20000,700]

# 먼저 price[]에 있는 0번째 인덱스 값을 변수에 저장을 한다.
lowPrice = price[0]
# 이 후, 루프를 돌면서 조건식으로 값이 작으면 해당하는 값을 lowPrice 변수에 재저장한다.
for i in range(1, len(price)):
    # 참이라는 것은 price[i] 가 lowPrice 보다 작다라는 것을 의미
    if price[i] < lowPrice:
        lowPrice = price[i]
print("가장 낮은 가격 : ",lowPrice)
print("----------------------------------------")

# 문자열에 대해서 가장 짧거나, 긴문자열을 구하는 알고리즘을 구현해보자.
words = ["dog","cat","horse","lion","tiger","elephant","bi"]
words_han = ["안녕","하이","반갑습니다","가지마세요","가세요","오랜만입니다"]
# 문자열 리스트에서 min()는 제일 첫 글자가 아스키코드 중에서 가장 작은 단어를
# 반환해주고 있다.
print("아스키 코드 값이 작은 단어 : ", min(words))
print("아스키 코드 값이 큰 단어 : ", max(words))
print("아스키 코드 값이 작은 단어 : ", min(words_han))
print("아스키 코드 값이 큰 단어 : ", max(words_han))

# 문자열에서 가장 짧은 문자열을 구하는 알고리즘 코드
shortest_word = words[0]
list_word = []
for i in range(1, len(words)):
    if len(words[i]) <= len(shortest_word):
        if len(words[i]) < len(shortest_word):
            list_word.clear()
            list_word.append(words[i])
        else:
            list_word.append(shortest_word)
            shortest_word = words[i]
            list_word.append(shortest_word)
        
print("가장 짧은 단어 : ", list_word)

for i in range(len(list_word)):
    print("가장 짧은 단어 목록 : ", list_word[i])