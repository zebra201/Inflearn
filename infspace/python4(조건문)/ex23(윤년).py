# 사용자로부터 연도를 입력받고 윤년 여부를 판단하는 프로그램 만들기
# 윤년의 조건
# 1. 연도가 4로 나누어 떨어지면 윤년이다.
# 2. 100으로 나누어 떨어지는 연도는 제외한다.
# 3. 400으로 나누어 떨어지는 연도는 윤년이다.

year = int(input("연도를 입력하세요 : "))
# 윤년인지 아닌지에 대한 조건식을 코드화.

result = ""
# if (year % 400) == 0:
#     result = "윤년"
# elif (year % 100) == 0:
#     result = "평년"
# elif (year % 4) == 0:
#     result = "윤년"
# else:
#     result = "평년"
# print(result, "입니다.")

if ((year % 4) == 0 and (year % 100) != 0) or (year % 400) == 0:
    result = "윤년"
else:
    result = "평년"
print(year,"년은", result, "입니다.")