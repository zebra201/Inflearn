# 조상클래스 정의
class Disk(object):
    __capacity = 0    # 용량
    __rpm = 0         # 속도
    
    def __init__(self, capacity, rpm):
        self.__capacity = capacity
        self.__rpm = rpm
    
    # getter 생성
    def getCapacity(self):
        return self.__capacity
    def getRpm(self):
        return self.__rpm
    
    # __str__ 은 문자열만 사용가능    
    def showPrint(self):
        return "디스크의 용량은" + str(self.__capacity) + "GB이며," \
            "RPM 은 " + str(self.__rpm) + "입니다"
        