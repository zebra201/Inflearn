# 반복문으로 문자열 관련 처리하기 실습
fruit = "apple"
# fruit 문자열 변수에 값을 하나씩 문자형태로 가져와서 출력하는 코드
for letter in fruit:
    print(letter, end=" ")
print("")
print("------------------------------------")

# 사용자로부터 문자열(영문)을 입력받아서 모음을 전부 없애는 코드를 작성.
# s = input("문자열을 입력하세요(영문자) : ")
# # 영문자의 모음의 문자열
# vowels = "aeiouAEIOU"
# result = ""
# for letter in s:
#     # 하나씩 반복하는 문자가 모음 문자열에 존재하지 않는다면, 참을 반환
#     if letter not in vowels:
#         result += letter
# print("자음만 출력됨 : " + result)
# print("")
# print("------------------------------------")

# 문자열을 입력받아서 자음과 모음의 개수를 집계하는 코드
original = input("문자열(영문)을 입력하세요 : ")
voewls = ""
consonant = ""
count_v = 0
count_c = 0
check = "aeiouAEIOU"
for i in original:
    if i in check:   
        voewls += i
        count_v += 1
    else:
        consonant += i
        count_c += 1
print("모음 : " + voewls, "모음의 수는 : " + str(count_v))
print("자음의 개수 : " + consonant, "자음의 수는 : " + str(count_c))
print("")
print("------------------------------------")

original = input("문자열을 입력하세요(영문자) : ")
# 입력받은 문자열을 전부 소문자로 변경한다.
word = original.lower()     # 대문자로 바꾸고 싶다면 upper() 라는 함수 사용
vowels = 0
consonants = 0
# 문자열의 길이가 0을 초과하고, 알파벳이라면...참을 반환한다.
if len(original) > 0 and original.isalpha():   # is함수는 항상 불리언 타입 반환
    for ch in word:
        # 루프 변수의 값이 모음에 속한다면
        if ch in "aeiou":
            vowels += 1
        else:       # 자음이라면
            consonants += 1
print("모음의 개수 : ", vowels)
print("자음의 개수 : ", consonants)
            