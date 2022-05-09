# deque와 list의 성능 비교

from collections import deque
import time     # 성능테스트를 하기 위해서 time 모듈을 가져옴

# 저장 성능 테스트
# 아무런 요소가 없는 deque 를 생성함
deque_test = deque()
start = time.time()     # 시작 시간을 저장(second 단위)

for i in range(100000000):
    deque_test.append(i)

end = time.time()
print("deque append 시간 : ", end - start)

# 빈 리스트를 생성함.
list = list()
start = time.time()     # 시작 시간을 저장(second 단위)
for i in range(100000000):
    list.append(i)
end = time.time()
print("list append 시간 : ", end - start)
print("-" * 50)


# # 추출 기능 테스트
# 
# start = time.time()
# for i in range(100000000):
#     deque_test.pop()
# end = time.time()
# print("deque pop 시간 : ", end - start)

# start = time.time()     # 시작 시간을 저장(second 단위)
# for i in range(100000000):
#     list.pop()
# end = time.time()
# print("list pop 시간 : ", end - start)


# 추출 기능 테스트
start = time.time()
for i in range(10000000):
    deque_test.popleft()
end = time.time()
print("deque popleft 시간 : ", end - start)

start = time.time()     # 시작 시간을 저장(second 단위)
for i in range(1000):
    list.pop(0)
end = time.time()
print("list pop(0) 시간 : ", end - start)

# 결론은 list, deque를 성능 테스트를 해보니 데이터를 추가를 할 때는
# deque 가 훨씬 좋은 성능을 보여준다. 또한 대용량일 수록 더욱더 많은 차이를 나타낸다
# 추출할 때는 역시 deque 가 list 보다 훨씬 빠른 성능을 보여준다
# 데이터 용량이 크면 클수록 deque를 사용하는 것을 고려해야 한다.