# 큐(Queue) : FIFP (First In First Out), 선입선출, 수도호스, 파이프
# 먼저 들어간 데이터가 먼저 나오는 형식
# 큐에서는 삽입할 때는 offer(), 추출시에는 poll() 사용한다.

queue = []
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)
print(queue)

# 선입선출(먼저들어간 데이터가 먼저 나감, 인덱스를 매개변수로 준다.)
print(queue.pop(0))
print(queue.pop(0))
print(queue)