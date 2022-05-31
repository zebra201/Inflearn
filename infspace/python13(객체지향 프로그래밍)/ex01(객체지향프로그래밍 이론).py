# 이론1
# 객체 지향 프로그래밍(OOP : object-oriented programming)
# 현실 세계에 있는 어떠한 사물을 코드로 표현하는 방법
# 내장 모듈이 아닌 직접 클래스를 만들어서 사용
# 객체 고유한 기능을 수행
# 클래스 : 설계도(붕어빵틀) = 사물을 묘사하는 것
# 클래스 요소 : 멤버 변수(필드, 속성), 멤버메소드(기능), 생성자(필수)
# 인스턴스(객체) : 붕어빵틀로 찍어낸 붕어빵들
# 클래스 안에서 구현된 함수는 함수라 하지 않고, 메소드라고 한다.
# 선언부, 구현부
# self : 자기 자신의 주소를 가지고 있는데, self.speed는 speed를 의미한다
# 주의할 점은 매개변수 self를 실제로 전달받지는 않으며, value 만 전달 받는다
# 아울러 이 self 라는 단어는 객체를 생성 해야지만 비로소 활성화 된다.

# Car 클래스 설계하기
class Car:
    # Car 클래스의 필드
    color = ""
    speed = 0
    # Car 클래스의 기능을 담당하는 메소드
    
    # 속도 높이는 메소드
    def upSpeed(self, speed):   # 메소드 호출할 때 들어오는 매개변수
        # self 는 자바에서 this와 동일, 자기 자신의 주소를 가지고 있는 인자다.
        # 인스턴스를 생성해야 비로소 self는 활성화 된다.
        if speed < 0:   # 음수 입력 방지 코드
            print("속도는 음수일 수 없습니다. 뒤로 갈까요?")
            return
        self.speed = speed      # 멤버변수에 해당함
    # 속도 낮추는 메소드
    def downSpeed(self,speed):
        if speed < 0:   # 음수 입력 방지 코드
            print("속도는 음수일 수 없습니다. 뒤로 갈까요?")
            return
        self.speed = speed
        
    # 멤버변수(필드)의 값을 출력해주는 메소드 추가
    def printFields(self, myCar):
        print("%s의 색상 :  %s / 속도 : %dKm" % (myCar, self.color, self.speed))
        
if __name__ == "__main__":
    # Car 클래스의 인스턴스를 사용하기
    myCar1 = Car()
    myCar2 = Car()
    myCar3 = Car()
    # 아래와 같이 주소를 찍어보면 각각 인스턴스는 독립적인 공간을 지니고 있다.
    print("myCar1의 주소 : ", id(myCar1))
    print("myCar2의 주소 : ", id(myCar2))
    print("myCar3의 주소 : ", id(myCar3))
    print("-" * 50)
    print("myCar1의 타입 : ", type(myCar1))
    print("myCar2의 타입 : ", type(myCar2))
    print("myCar3의 타입 : ", type(myCar3))
    
    myCar1.color = "파랑색"
    myCar1.upSpeed(50)
    myCar1.printFields("myCar1")
    
    myCar2.color = "노랑색"
    myCar2.upSpeed(100)
    myCar2.printFields("myCar2")
    
    myCar3.color = "빨강색"
    myCar3.upSpeed(-100)
    myCar3.printFields("myCar3")
    
    # 클래스를 설계하고 사용하는 루틴
    # 1. 클래스를 설게(정의)
    # 2. 인스턴스 생성하기
    # 3. 필드나 메소드를 호출하여 원하는 프로그램 만들기


# 이론2
# self 는 매개변수로 보기보다는 메소드 안에 무조건 써야하는 것으로 보는 것이 편함(문법)
# 메모리 상에서(참조변수, 스택, 인스턴스(참조변수의 주소를 가지고 있음))
# myCar1 = Car()
# myCar2 = Car()
# myCar3 = Car()
# 인스턴스가 생성되면 각 자동차는 독립적인 메모리 공간을 차지한다.
# 인스턴스명 = 참조변수

# Car 클래스의 생성과 사용 순서
# 1단계 : 클래스 선언 / class 명(필드 선언, 메소드 선언)
# 2단계 : 인스턴스 생성 / 인스턴스 = 클래스명()
# 3단계 : 필드나 메소드 사용 / 인스턴스, 필드명 = 값 / 인스턴스,메서드()


# 실습1
# 