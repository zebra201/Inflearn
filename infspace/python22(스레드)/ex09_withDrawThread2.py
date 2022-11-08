# 입출금을 같이 하는 스레드 클래스 작성
import threading

class withDrawThread2(threading.Thread):
    # 
    def __init__(self, account):
        super().__init__()
        self.account = None
    
    def setAccount(self,account):
        self.account = account
        self.setName("아들")
        
    def run(self):
        self.account.withDraw(300)