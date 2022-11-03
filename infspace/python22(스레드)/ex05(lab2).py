# 문제2
# 클래스 AutoSaveThread 를 만들고 클래스 안에 멤버메소드로
# save() 작성한다
# run() 에서는 무한루프를 돌면서 1초간 일시정지코드를 작성하고
# 자신의 인스턴스에 있는 save() 메소드를 호출하도록 한다.
# 메인코드에서는 아래와 같이 출력되도록 프로그램을 작성하시오.

# 출력결과
# 작업내용 저장함!
# 작업내용 저장함!
# 작업내용 저장함!
# 작업내용 저장함!
# 메인스레드 종료됨
# ----------------------------------------------

# 풀이
import threading
import time
class AutuSaveThread(threading.Thread):
    def __init__(self):
        super().__init__()
    def save(self):
        print("작업내용 저장함!")
    def run(self):
        # 1초단위로 save()메소드를 호출하고 있다.
        while True:
            time.sleep(1)
            self.save()
            
# 메인코드 시작
if __name__ == "__main__":
    autuSaveThread = AutuSaveThread()
    # print("autoSaveThread 가 데몬입니까?", autuSaveThread.isDaemon())
    # 데몬스레드가 되는 코드(종속성 스레드가 된다)
    autuSaveThread.daemon = True
    # print("autoSaveThread 가 데몬입니까?", autuSaveThread.isDaemon())
    autuSaveThread.start()
    time.sleep(5)
    print("메인스레드 종료됨")