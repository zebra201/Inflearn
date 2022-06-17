# 클래스 안의 상수를 많이 사용한다. 상수는 보통 클래스 변수 형태를
# 지정하여 사용한다.
class Character:
    # 상수값 정의
    WEAK = 0
    NORMAL = 10
    STRONG = 20
    VERY_STRONG = 30
    
    # 메소드 생성자
    def __init__(self):
        self.__hp = Character.NORMAL
    
    def levelUP(self):
        self.__hp = Character.STRONG
    
    def damage(self):
        self.__hp = Character.WEAK
    
    def getHP(self):
        return self.__hp
    
    # __str__() 메소드는 print() 주목적으로 하는 것이 아니고
    # 문자열을 리턴하게끔 해주는 것이 목적이다.
    def __str__(self):
        return "HP : " + str(self.__hp)

if __name__ == "__main__":
    ch = Character()
    print(ch)
    ch.levelUP()
    print(ch)
    ch.damage()
    print(ch)