# 문자열의 인덱싱
# 인덱싱이란 문자열에서 문자를 추출하는데 문자열에는 각각에 해당하는
# 문자에 번호(인덱스)가 존재한다. [인덱스]하면 문자열에서 문자를 추출할수 있다.
# 인덱스라 함은 무조건 0부터 시작.
# 파이썬 특수기능인 인덱스를 처리할 때 음수도 사용이 가능.
# 마지막 인덱스는 n-1 이 성립.

word = "Python"
print(len(word))

print(word[0])
print(word[5])
# len(word)는 어차피 문자열의 길이인 6을 반환을 하기 때문에 -1을 해주면 끝문자를 반환해준다.
print(word[len(word)-1])
# 해당 문자열의 인덱스의 범위 밖의 값을 주면 index out of range에러 발생.
# print(word[100])

# 파이썬에서는 한번 작성된 문자열은 변경이 불가능하다.(문법임)
# word[2] = 'B'

# 사용자로부터 문자열을 입력을 3개를 받도록 한다.
# ex : OST 라는 단어를 받으면 각 해당
# 문자열의 첫번째 문자를 인덱싱하여 문자열로 만들어보자.
# signature = "Original Sound Track"
# print(signature[0], signature[9], signature[15])
item1 = input("첫 번째 단어를 입력하시오 : ")
item2 = input("두 번째 단어를 입력하시오 : ")
item3 = input("세 번째 단어를 입력하시오 : ")
# 위 3개의 문자열 중 첫 번째 단어만 추출하여 또다른 문자열을 만들고 있다.
word = item1[0] + item2[0] + item3[0]
print("새로 만든 문자열 :", word)