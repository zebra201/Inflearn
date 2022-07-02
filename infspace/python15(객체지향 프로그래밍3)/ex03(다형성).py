# 이론

# 다형성 (여러가지 형태를 가질 수 있는 성질)
# 조상클래스의 참조변수로 자손클래스의 인스턴스를 다룰 수 있음.
# 추상클래스
# 메소드의 목록만 가진 클래스이며, 상속받는 클래스에서
# 메소드 구현을 강제하기 위해 사용한다.
# 메소드 위에 @abstractmethod 를 붙여 추상메소드로 지정한다.
# 추상클래스를 상속받았다면 @abstractmethod 가 붙은 추상 메소드를 모두 구현해야한다.
# ------------------------------------------------------------------------

# 실습

# 다형성의 개념은 여러가지 형태를 가질 수 있는 능력이다.
# ㅂ보이는 실제 모습 혹은 행위는 다른 특징을 지닐 수 있다.

class Animal :
    def __init__(self, name, age, weight, instance):
        self.__name = name
        self.__age = age
        self.__weight = weight
        # 아래 코드는 Animal 을 독립적인 클래스의 인스턴스를 받는다.
        self.__instance = instance
        
    def show(self):
        print("이름 : ", self.__name)
        print("종류 : ", self.__instance.d_name)
        print("나이 : ", self.__age)
        print("몸무게 : ", self.__weight)
        # 매개변수로 넘어오는 독립클래스의 메소드인 sound() 각각 호출
        self.__instance.sound()
        print("-" * 50)
    
class Tiger():
    d_name = "호랑이"
    def sound(self):
        print("어흥")
        
class Dog():
    d_name = "개"
    def sound(self):
        print("멍멍")
        
class Cat():
    d_name = "고양이"
    def sound(self):
        print("야옹")
    
if __name__ == "__main__":
    ani1 = Animal("호돌이", 8, 180, Tiger())
    ani1.show()
    ani2 = Animal("댕댕이", 4, 8, Dog())
    ani2.show()
    ani3 = Animal("야옹이", 3, 5, Cat())
    ani3.show()