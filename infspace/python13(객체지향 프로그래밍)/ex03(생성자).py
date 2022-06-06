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

from Person import *

if __name__ == "__main__":
    # 기본 생성자 호출
    # 기본 생성자는 호출되면 무조건 똑같은 초기값을 지니고 메모리에
    # 생성된다. 그리고 그 값을 변경하려면 직접 setter() 나
    # 인스턴스명.필드 = 값 을 대입하여 변경해야하는 단점이 존재한다.
    person1 = Person()
    person1.__str__()
    print("-" * 50)
    person2 = Person()
    person2.__str__()
    print("-" * 50)
    print("person1.name : ", person1.getName())
    person1.setName("김길동")
    person1.age = 50
    print("person1.name : ", person1.getName())
    # age 라는 필드는 __ 가 붙지 않았기에 public 성질을 지니고 있어서
    # 외부에서 바로 접근이 가능하다.
    print("person1.address : ", person1.getAddress())
    print("person1.age : ", person1.age)
    
    
    
    # 같은 값을 가지고 있지만 다른 객체이다.
    # print("Person1의 주소", id(person1))
    # print("Person2의 주소", id(person2))