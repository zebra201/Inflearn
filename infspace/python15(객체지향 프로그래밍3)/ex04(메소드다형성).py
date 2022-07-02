# 2. 메소드의 다형성

class SalesWorker:
    def __init__(self, name):
        self.__name = name    
    def work(self):
        print(self.__name, "물건을 팝니다.")
        
class DevWorker(SalesWorker):
    def __init__(self, name):
        super().__init__(name)
        self.__name = name
    def work(self):
        print(self.__name, "물건을 개발합니다.")

if __name__ == "__main__":
    worker1 = SalesWorker("데이브")
    worker2 = SalesWorker("이현호")
    worker3 = SalesWorker("김연아")
    worker4 = DevWorker("김갑수")
    worker5 = DevWorker("고길동")
    worker6 = DevWorker("홍수정")
    
    # 인스턴스의 타입에 따라 코드는 동일하나, 실제 호출되는 work()
    # 메소드가 달라 출력결과가 다르다.
    workers = [worker1, worker2, worker3, worker4, worker5, worker6]
    for worker in workers :
        worker.work()
        
    # 데이브 물건을 팝니다.
    # 이현호 물건을 팝니다.
    # 김연아 물건을 팝니다.
    # 김갑수 물건을 개발합니다.
    # 고길동 물건을 개발합니다.
    # 홍수정 물건을 개발합니다.