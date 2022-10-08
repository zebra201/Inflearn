# 이터레이터
# for 루프를 이용하여 리스트 안의 요소들을 반복할 수 있지만
# 파이썬에서는 여러 종류의 반복 가능한 객체(iterable)가 있으며,
# 이들 객체는 이터레이터(iterator)라고 불린다.
# 이터레이션(iteration)이 반복을 의미하므로 '반복가능한 객체' 라고 해석할 수 있다.
# 객체가 반복 가능한 객체가 되려면 다음 2개의 메소드를 구현해야한다.,
# _iter_() 는 반복 가능한 객체 자신을 반환한다
# _next_() 는 다음 반복을 위한 값을 반복한다.

# 제네레이터
# 함수를 사용하여 반복 가능한 객체를 생성한다.
# 제네레이터는 키워드 yield 를 사용하여 함수로부터
# 반복 가능한 객체를 생성하는 하나의 방법이다.
# 이터레이터와 출력은 같지만 메모리 적재 방식이 다르다.

# -----------------------------------------------
# 실습
# 이터레이터라는 것은 갯체를 반복가능한 객체로 만들어 주는 것
# __iter__(), __next__() 2개의 메소드를 클래스에 정의해주어야
# 비로소 반복가능하게 되는 것이다

class MyCounter(object):
    # 생성자 정의(초기화 메소드)
    def __init__(self, low, high):
        self.current = low
        self.high = high
    # 반복가능한 객체가 되기 위해서 아래 2가지 메소드를
    # 추가 및 정의를 한다.
    # __iter__() 메소드는 자기 자신을 반환하게끔 정의를 하도록 한다.
    def __iter__(self):
        return self
    
    def __next__(self):
        # current 값이 high 값을 초과하게 되면
        # StopIteration 예외를 발생하게 하였다.
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            # self.current 값이 1을 증가했지만 이전값을 출력하기위해서 -1을 해서 리턴해준다
            return self.current - 1
        
if __name__ == "__main__":
    counter = MyCounter(1,10)       # 생성자 호출
    for n in counter :
        print(n, end=" ")
        