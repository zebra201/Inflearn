# 지구에서 가장 가까운 별은 프록시마 켄타우리라는 별이라고 한다.
# 프록시마 켄타우리는 지구로부터 40 * 10^12 km 떨어져 있다고 한다.
# 빛의 속도로 이 별에 간다면 시간이 어람나 걸리는지 계산하는 프로그램
# 빛의 속도 초당 30만km 이다.

# 빛의 속도 값 저장
from math import *

light_speed = 300000
distance = 40 * pow(10, 12)
# print(distance, "km")

seconds = distance / light_speed
print("걸리는 시간 : ", seconds, "초")
light_year = seconds / (60 * 60 * 24 * 365)
print("걸리는 년도 : ", light_year, "년")

# 정수 10 과 실수 10.0 은 동일하다
print(10 == 10.0)
# 문자열 10과 실수 10.0 은 완전히 다르다.
print('10' == 10.0)