# 이론
# 여러 기반 클래스로부터 상속을 받아서 파생클래스를 만드는 방법
# 다중상속의 문제점
# 상속받은 여러 기초 클래스에 같은 이름의 멤버가 존재할 가능성(충돌성)
# 하나의 클래스를 간접적으로 두 번 이상 상속받을 가능성이 있다.

# 다이아몬드 상속 문제점의 해결책
# 파이썬에서는 다이아몬드 상속 문제점의 해결책으로
# 메소드 탐색순서(Method Resolution Order, MRO)를 따른다
# ---------------------------------------------------------------

# 실습
# 클래스 다중 상속에 대한 실습
# 다중상속 : 여러 조상클래스로부터 상속을 받아서 새로운 클래스를 만드는 것
# 조상클래스를 몇 개를 상속을 받아도 상관 없다.
# 다중상속 문제점
# 1. 다중상속을 하다보면 조상클래스에서 같은 이름을 가진 멤버가
# 존재할 수 있기 때문에 충돌성이 발생할 수 있다.
# 2. 하나ㅓ의 조상클래스를 두 번 이상 상속을 받을 가능성이 있다.
# 파이썬에서는 단일, 다중상속을 다 지원하기 때문에 알고 있으면 좋다.

class Person(object):
    def __init__(self):
        pass
    def greeting(self):
        print("안녕하세요.")
        
class University(object):
    def __init__(self):
        pass
    def manage_credit(self):
        print("학점관리를 합니다.")

# 2개의 조상클래스를 상속 받음
class Undergraduate(Person, University):
    def __init__(self):
        Person.__init__(self)
        University.__init__(self)
    # 멤버가 3개
    def study(self):
        print("공부를 합니다.")
        
if __name__ == "__main__":
    student = Undergraduate()
    student.greeting()
    student.manage_credit()
    student.study()
    