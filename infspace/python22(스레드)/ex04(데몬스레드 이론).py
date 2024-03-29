# 데몬(daemon) 스레드 이론
# 데몬스레드는 메인스레드가 종료될 때, 자신의 실행 상태와 상관없이
# 종료되는 서브 스레드(종속성 스레드)를 의미한다.

# 동시성
# 프로그램을 구현했는데 성능이 부족한 경우, 알고래즘을 개선할 수도 있지만
# 어려운 방법이다. 따라서 동시성과 병렬성을 통해 개선할 수 있다.
# 동시성은 멀티태스킹을 말하며, 하나의 일을 처리하지만 아주 빠르게 번갈아가며
# 처리하므로 동시에 하는 것처럼 보인다.

# 병렬성
# 동시성과 다르게 진짜로 동시에 여러 개의 일을 처리하는 것이다.
# 멀티코어에서 하나씩 스레드를 맡아 독립적으로 진행

# 현재 대부분의 컴퓨터는 멀티코어 이므로 동시성과 병렬성을 동시에 가진다.

# 스레드 동기화
# 한 스레드가 어떤 클래스(객체)에 접근했을 때 다른 스레드를 접근하지 못하게 함.
# 스레드의 문제점은 서로 모든 자원을 공유하지만 전역변수에 동시 접근하게되면
# 원하지 않는 결과를 초래할 수 있다.
# 따라서 동기화를 통해 다른 스레드의 접근을 제한할 수 있다.

# 스레드 동기화 처리는 Lock
# Lock 은 특정 스레드에서 변수를 사용하기 시작했다면 다른 스레드 사용을 제한하는 것을
# Lock 이라고 한다.
# 임계영역은 둘 이상의 스레드가 동시에 접근해서는 안되는 공유자원을
# 접근하는 코드를 말한다.
# Lock.aquire() : 잠금 - 다른 스레드들의 접근을 제한한다.
# Lock.realease() : 잠금을 해제하여 접근을 허용한다.

# -------------------------------------------------------------------------
# 데몬스레드 실습
# 데몬(daemon) 스레드 : 종속성 스레드라고도 한다. 데몬스레드는 자신이 실행중에 있어도
# 메인스레드가 종료하게 되면 같이 종료 되는 것이 바로 데몬스레드이다.
# ex ) 네이버 메일작성 자동저장, 파이썬 인터프리터와 같은 것이 바로 데몬스레드이다.
import threading
import time
class Worker(threading.Thread):
    # 생성자
    def __init__(self, name):
        super().__init__()
        self.name = name
        
    def run(self):
        print("작업스레드 시작 : ", threading.currentThread().getName())
        time.sleep(3)
        # 메인스레드가 종료되니 이 부분은 아마 출력되지 않을 것이다
        # 데몬스레드로 설정되어 메인스레드가 종료되니 데몬스레드도
        # 메인스레드가 종료됨에 따라 같이 종료되지 때문이다.
        print("작업스레드 종료 : ", threading.currentThread().getName())

if __name__ == "__main__":
    print("메인스레드 시작")
    for i in range(5):
        name = str(i)
        thread = Worker(name)
        # print("thread가 데몬입니까? ", thread.isDaemon())
        # daemon 변수에 저장되어 있는 스레드 인스턴스를 데몬 스레드로 바꾼다.
        # daemon 속성을 기본값을 False 이지만, 데몬스레드로 만들기 위해서는
        # 이 속성의 값을 True 설정해야한다.
        thread.daemon = True
        # print("thread가 데몬입니까? ", thread.isDaemon())
        thread.start()
    print("메인 스레드 종료됨.")