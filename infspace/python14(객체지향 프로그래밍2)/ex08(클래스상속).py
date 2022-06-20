# 이론1

# 클래스 상속은 기존 클래스에 있는 필드와 메서드를
# 그대로 물려받는 새로운 클래스를 만드는 것이다.
# 상속받은 후에는 새로운 클래스에서 추가로 필드나 메서드를 만들어 사용 가능하다.
# 자동차와 트럭의 경우 공통되는 부분 즉, 색상 속도 같은 경우
# 각각을 모두 클래스로 생성하는 것 보다, 공통된 특징을
# 자동차라는 클래스로 생성한 후 특징을 물려받는 것이 효율적이다.
# 슈퍼 클래스 = 부모 클래스 = 조상 클래스
# 서브 클래스 = 자식 클래스 = 자손 클래스
# 관련이 없는 클래스들을 직접적인 관계로 만들어준다.

# class 서브 클래스(슈퍼클래스):
#     이 부분에 서브 클래스의 내용 코딩

# class TV:
#     color = ""
#     inch = 0
#     power = False

# SmartTV는 TV 클래스를 상속 받아 총 4개의 멤버를 가지고 있다.
# 필드(멤버)의 개수는 하위로 내려갈 수록 많아진다.
# class SmartTV(TV):
#     smart = ""
# --------------------------------------------------------

# 이론2
# 메소드 오버라이딩(Overriding)은 상위 클래스의 메소드를
# 서브 클래스에서 재정의 하는 것( )
# 즉, 선언부는 동일하나 구현부 부분을 다르게 정의
# 상속 후 구현부에서 pass 를 사용하면 변화 없음

# super() 메서드
# 서브 클래스에서 메소드 오버라이딩을 할 떄, 슈퍼 클래스의 메소드나
# 속성을 사용해야 하는 경우에 사용한다.
# --------------------------------------------------------

# 실습1
# 클래스의 상속 : 조상(부모, 슈퍼)클래스의 멤버(필드, 메소드 생성자 제외)들을
# 그대로 자손(자식, 서브)클래스가 물려받아 새로운 클래스를 만드는 것이다.
# 이렇게 상속이 이루어지면 직접적인 관계가 이루어진다.
# 조상클래스의 멤버가 추가, 삭제, 수정에 따라서 자손클래스가
# 영향을 받는다. 역으로 자손클래스의 멤버가 추가, 삭제, 수정이 되면
# 조상클래스에 영향을 끼치지 않는다.
# 자손클래스로 내려가면 갈수록 멤버의 개수가 많아지고
# 반대로 조상클래스로 올라가면 멤버의 개수가 적어진다.

# 조상클래스
class Car : 
    # 조상클래스의 멤버는 3개이다.
    
    def __init__(self):
        self.speed = 0
        self.door = 0
    
    def upSpeed(self, speed):
        self.speed += speed
        print("현재 속도(조상클래스) : %d" % self.speed)
        print("문의 개수(조상클래스) : %d" % self.door)
        
# 자손클래스
class Sedan(Car):
    # 자손클래스의 멤버는 4개이다. (조상3개 + 자손1개)
    def __init__(self, speed, door):
        # 조상클래스의 생성자를 호출하는 부분
        # 조상없는 자손이 있는가?
        Car.__init__(self)
        self.speed = speed
        self.door = door
    
    # 자손클래스에서 추가한 메소드
    def downSpeed(self, speed):
        self.speed -= speed
        print("현재 속도(자손클래스) : %d" % self.speed)

if __name__ == "__main__":
    # car 인스턴스에는 downSpeed() 메소드가 없다.
    # 하여 호출할 수가 없다.
    car = Car()
    car.upSpeed(50)         # Car 클래스의 메소드 호출
    print("car 주소 : ", id(car))
    sedan = Sedan(100, 4)
    print("sedan 주소 : ", id(sedan))
    sedan.upSpeed(150)      # 조상클래스 메소드 호출
    sedan.downSpeed(100)    # 자손클래스 메소드 호출