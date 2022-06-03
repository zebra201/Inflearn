# 이론
# 생성자(Constructor)는 인스턴스를 생성하면 무조건 호출되는 메서드이다.
# myCar1 = Car()
# myCar1.color = "빨강"
# myCar1.speed = 0
# 인스턴스를 생성하면서 필드값을 초기화시키는 메서드를 생성자라고 한다.
# 자바와 달리 파이썬에서는 생성자는 하나만 존재해야 한다.
# __init__() : 생성자
# class Car :
#     color = ""
#     speed = 0
#     def __init__(self):
#         self.color = "빨강"
#         self.speed = 0

# 아래와 같이 인스턴스를 만들면, 이제 대입을 할 필요 없이 기본적으로
# color 는 "빨강", speed = 0으로 초기화가 이루어진다.
# myCar1 = Car()
        
# 매개변수가 있는 생성자
# class Car :
#     color = ""
#     speed = 0
#     def __init__(self, color, speed):
#         self.color = color
#         self.speed = speed

# myCar1 = Car("빨강", 30)
# myCar2 = Car("파랑", 60)

# 생성자 추가, getter() 메소드
# getter() 메소드 : 캡슐화라는 개념이 존재, 클래스의 필드를 외부로 노출시키는 것을 방지한다.(은닉화)
