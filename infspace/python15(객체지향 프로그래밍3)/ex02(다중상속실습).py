# 다중상속에 대한 실습
class Person:
    def __init__(self):
        print("나는 사람입니다.")
    def greeting(self):
        print("Person 클래스의 greeting 메소드 호출됨")

class Student(Person):
    # 생성자 생성
    def __init__(self):
        # 조상클래스 상속 호출
        Person.__init__(self)
        print("나는 학생입니다.")
    # def greeting(self):
    #     print("Student 클래스의 greeting 메소드 호출됨")
        
class Worker(Person):
    def __init__(self):
        Person.__init__(self)
        print("나는 근로자입니다.")
    def greeting(self):
        print("Worker 클래스의 greeting 메소드 호출됨")
        
# 다중 상속
class PartTimer(Student, Worker):
    def __init__(self):
        Student.__init__(self)
        Worker.__init__(self)
        print("나는 파트타임 근로자입니다.")
    # def greeting(self):
    #     print("PartTimer 클래스의 greeting 메소드 호출됨")
        
if __name__ == "__main__":
    partTimer = PartTimer()
    # 다이아몬드 상속 문제점은 같은 이름의 멤버가 있다면
    # 자손클래스에서 해당 메소드를 오버라이딩을 하지 않았다면
    # 도대체 어떤 조상클래스의 메소드가 호출되는지 알 수 없다.
    # 위와 같은 문제점을 해결하기 위해 파이썬에서는
    # 메소드 탐색순서(MRO : Method Resolution Order) 기법을 따른다.
    # MRO 기법은 복잡한 상속관계를 가질 때 어떤 멤버가 호출이
    # 먼저 되는지 알아볼 수 있는 편리한 방법이다.
    print(PartTimer.__mro__)
    partTimer.greeting()