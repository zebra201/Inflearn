# 문제3
# 호출될 때마다 앞의 수에 1을 더해서 반환하는 함수를 작성해보자
# range()와 아주 유사하지만 이 함수는 상한 값이 없다.
# 함수는 제너레이터를 이용하여 구현된다.
# --------------------------------------------

# 풀이
import time
# 앞의 수에 1씩 더하여 그 값을 보내는 제네레이터 형태의 함수 정의
def inf_sequence():
    num = 0
    while True:
        yield num
        time.sleep(1)   # CPU가 빨리 실행되므로 sleep을 사용하여 늦춤
        num += 1

if __name__ == "__main__":
    for n in inf_sequence():
        print(n, end=" ")