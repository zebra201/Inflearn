# 자료구조의 개념
# 자료구조 : 데이터의 특징을 고려하여 데이터를 저장하는 방법
# 자료구조의 특징 : 최대한 메모리를 효율적으로 저장 및 반환하는 방법으로,
# 데이터를 관리하는 것, 대용량일수록 빨리 저장하고 빨리 검색하고, 메모리를 최대한 효율적으로
# 사용하면 유저들에게 실행결과를 빨리 돌려주는 방법,

# 스택(stack) : 후입선출(LIFO, 나중에 들어온 것이 먼저 나감, push, pop)
stack_data = []
# 스택에 값을 push 하고 있다.
stack_data.append(10)
stack_data.append(20)
stack_data.append(30)
stack_data.append(40)
stack_data.append(50)
print(stack_data)

# 스택에서 추출할 때는 pop() 메서드를 사용한다.
# pop() 메서드는 스택에서 마지막으로 들어온 데이터를 삭제하면서 삭제된 데이터를 반환한다.
print(stack_data.pop())
print(stack_data.pop())
print(stack_data)

# 입력받는 텍스트를 역순으로 추출하는 프로그램
word = input("문자열을 입력해주세요 : ")
# list()메서드를 사용하여 문자열을 리스트로 반환하고 있다.
word_list = list(word)
print(word_list)

result = []
# _ 라는 기호는 파이썬에서 상당히 많이 사용, for 문을 루핑시킬때,
# 루프 변수에 값을 사용하지 않을 때,  _로 할당 받는 것이다.
for _ in range(len(word_list)):
    # 사용자에게서 입력받은 문자 리스트의 마지막 부분부터 result[] 에 담고 있다.
    result.append(word_list.pop())
print(result)