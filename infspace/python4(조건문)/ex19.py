# 사용자로부터 태어난 연도를 입력받아서 초,중,고,대학생으로 분류하시오.(현재나이기준)
# 나이 :  8~13(초등학생), 14~16(중학생), 17~19(고등학생), 20~27(대학생)
# 이 외의 나이라면 일반인으로 분류를 하도록한다.

birth_year = int(input("태어난 연도를 입력하세요 : "))
# 나이 계산(현재나이 기준)
age = (2021 - birth_year) + 1
print("현재나이 : ", age)
if age >= 8 and age <=13:
    print("초등학생입니다.")
elif age >= 14 and age <= 16:
        print("중학생입니다.")
elif age >= 17 and age <= 19:
        print("고등학생입니다.")
elif age >= 20 and age <= 27:
        print("대학생입니다.")        
else :
    print("일반인입니다.")


    