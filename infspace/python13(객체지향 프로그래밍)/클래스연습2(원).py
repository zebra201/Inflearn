# 문제
# 원(Circle)을  클래스로 표시해 보자. 원은 반지름(radius)을 가지고 있다.
# 원의 넓이와 둘레를 계산하는 메소드를 정의해보자.
# 생성자는 매개변수가 존재하는 생성자를 만들어보자.
# 출력결과
# 원의 반지름 : 10
# 원의 넓이 : 314.16
# 원의 둘레 : 62.83
# ------------------------------------------------------

from math import pi

class Circle:
    # 필드 선언
    __radius = 0
    
    # 생성자
    def __init__(self, radius):
        self.__radius = radius
    
    # getter, setter
    def getRadius(self):
        return self.__radius
    def setRadius(self, radius):
        self.__radius = radius
        
    # 둘레, 넓이 구하는 식
    def calArea(self):
        area = pi * self.__radius * self.__radius
        return area
        
    def calCircum(self):
        circumference = 2 * pi * self.__radius
        return circumference
    

if __name__ == "__main__":
    circle1 = Circle(float(input("반지름을 입력하세요 : ")))
    print("입력된 반지름 값 : ", circle1.getRadius())
    print("원 둘레의 값 : ", round(circle1.calArea(),2))
    print("원 넓이의 값 : ", round(circle1.calCircum(),2))