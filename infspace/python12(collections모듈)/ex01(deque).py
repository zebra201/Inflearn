# 자료구조 - collections 모듈
# collections 모듈이란 기존에 배웠던 자료구조(리스트, 큐, 스택, 튜플, 딕셔너리) 등
# 좀 더 확장하여 제작된 파이썬의 내장 모듈이다.

# 1) deque (데크, double-ended queue)모듈은 스택과 큐를 모두 지원하는 모듈이며,
# 양방향으로 데이터를 입출력 할 수 있는 자료구조이다.
# deque 모듈은 메모리의 효율적 사용과 빠른 속도라는 측면에서도 유용하다.
from collections import deque
# 아무 요소가 없는 deque를 생성함.
deque_list = deque()
print(deque_list)

# 아래 코드는 기존 리스트와 같이 데이터가 추가가 됨을 알 수 있다.
for i in range(5):
    deque_list.append(i)
print(deque_list)

# deque에 있는 요소들을 삭제하기
# print(deque_list.pop(0))    # deque에서는 pop(0) 것이 지원이 안된다.
# deque에서는 스택도 지원하는 모듈이므로 pop() 사용하면 늦게 들어간
# 데이터부터 삭제됨을 알 수가 있다.
print(deque_list.pop())
print(deque_list.pop())
print(deque_list.pop())
print(deque_list)

print("-" * 50)

# appendleft() 메서드 사용 : 먼저들어간 데이터가 뒤로 나감
deque_list.clear()
print(deque_list)
for i in range(5):
    deque_list.appendleft(i)
    print(deque_list)