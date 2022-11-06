# Calculator 에 공유 객체에 접근하는 스레드 클래스 작성
from ex08_Calculator import *

class User2(threading.Thread):
    def __init__(self):
        super().__init__()
        
    def setCalculator(self, calculator):
        # 메인에서 생성한 calculator 인스턴스를 매개변수로 받아서 접근
        self.calculator = calculator
        self.setName("User-2")      # 스레드 이름 설정
        
    def run(self):
        self.calculator.setMemory(50)
