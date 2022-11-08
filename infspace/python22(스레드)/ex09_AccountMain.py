# 실행 파일

from ex09_Account import *
from ex09_withDrawThread1 import *
from ex09_withDrawThread2 import *

if __name__ == "__main__":
    # 공유객체 생성
    account = Account(0)
    # 스레드 클래스으 ㅣ생성자에서는 account 를 None 초기화를 한다.
    thread1 = withDrawThread1(account)
    thread2 = withDrawThread2(account)
    # 스레드 클래스의 setAccount() 에서는 account 를 실제 인스턴스의 주소로 치환한다.
    # 아래 2개의 스레드는 account 인스턴스를 공유하게 된다.
    thread1.setAccount(account)
    thread2.setAccount(account)
    # 스레드 실행
    thread1.start()
    thread2.start()