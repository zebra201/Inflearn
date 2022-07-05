# 추상클래스의 실습
# 추상클래스 : 클래스안에 최소 추상메소드가 1개 이상 존재하면
# 그 클래스를 추상클래스라고 한다.
# abc(abstract base class 약자) 모듈을 이용하여 만든다.
# @abstractmethod 라는 어노테이션을 추상메소드 위에 붙여준다.
# 추상메소드는 선언부만 존재하고 구현부는 없는 메소드이다.
# 추상클래스는 인스턴스를 절대로 생성할 수가 없다.

from abc import *

# 문법
class StudentBase(metaclass = ABCMeta):
    # 아래 어노테이션은 인터프리터에게 study 메소드가 추상메소드이다
    # 이니 잘 체크해라라는 명령을 준다.
    @abstractmethod
    def study(self):
        pass
    
    @abstractmethod
    def go_to_school(self):
        pass
    
# Student 클래스는 인스턴스를 만들 수 없다.
# 그 이유는 추상메소드 1개를 재정의 하지 않았기 때문이다.
class Student(StudentBase):
    # study 하나만 오버라이딩 할 수 없다
    def study(self):
        print("공부를 합니다.")

# go to school 마저 하나를 구현    
class Student1(Student):
    def go_to_school(self):
        print("학교를 갑니다.")
    
if __name__ == "__main__":
    # 추상클래스는 절대로 인스턴스를 생성할 수가 없다.
    # 상속을 통하여 자손클래스에서 추상메소드를 전부 오버라이딩
    # 했을때 인스턴스 생성이 가능하다.
    # student = StudentBase()
    # student = Student()
    student1 = Student1()
    student1.study()
    student1.go_to_school()
    
# ----------------------------------------------------------------
# 추상클래스의 용도 : 추상클래스를 상속받는 각각의 자손클래스에서
# 다른 내용으로 구현될 것을 예쌍하고 뼈대(가이드라인)만 만든다
# 라는 것이다.
# 예) 추상클래스에 play() 추상메소드가 존재한다면 mp3, cdplayer,
# lpplayer, tapeplayer 클래스에는 play 메소드가 다 존재할 것이다.
# play() 메소드는 선언부만 같을 뿐 다른 내용을로 오버라이딩이 되어
# 다른 결과를 만들어줄 수 있다.