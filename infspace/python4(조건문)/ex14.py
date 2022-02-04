# 몸무게와 키를 입력받고 BMI가 20.0 이상이고 25미만이면
# 표준입니다 라고 출력을 하고 아니면 체중관리가 필요합니다 라고
# 출력하는 프로그램 만들기.
# BMI = 몸무게 / 키**2

height = float(input("키(cm)를 입력하세요 : "))
weight = float(input("몸무게(kg)를 입력하세요 : "))
# height /= 100.0 은 height = height / 100.0 과 동일하다
BMI = weight / (height**2) * 10000
# if 20 <= BMI < 25 :
print("BMI 값 : ", BMI)
if BMI >= 20 and BMI < 25:
    print("표준입니다")
else :
    print("체중관리가 필요합니다")