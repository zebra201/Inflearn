# yield from 을 사용한 실습
import time
def gen():
    list1 = [10,20,30]
    # 대기 상태로 빠지지 않고 리스트의 요소 값을 하나씩 꺼내서 보내준다.
    yield from list1
    # time.sleep(2)
    # print("gen()함수 내에서의 list1 의 요소 값 : ", list1)
    
if __name__ == "__main__":
    test_gen = gen()
    n = next(test_gen)
    print("main() 내에서의 n의 값 : ", n)
    n = next(test_gen)
    print("main() 내에서의 n의 값 : ", n)
    n = next(test_gen)
    print("main() 내에서의 n의 값 : ", n)
    # 아래 코드에서는 더이상 가져올 것이 없기 때문에
    # StopIteration 예외가 발생한다.
    n = next(test_gen)
    print("main() 내에서의 n의 값 : ", n)