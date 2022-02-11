# 구의 부피를 계산하는 함수 sphereVolume() 함수를 작성하여
# 그리고 ,반지름을 사용자로부터 임력을 받고 구의 부피를 구하는 함수를 호출해서 테스트해라
# 구의 부피 = 4/3 * 3.14 * (r**3)

import math
# 구의 부피를 구하는 함수를 선언 및 구현
def sphereVolume(radius):
    volume = (4.0/3.0) * math.pi  * math.pow(radius, 3)
    return volume


radius = float(input("반지름 값을 입력하세요 : "))
print("반지름이 : ", radius, "인 구의 부피 : ", round(sphereVolume(radius),2))


