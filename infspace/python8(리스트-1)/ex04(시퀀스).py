# 1byte(8bit) -> 1Kbyte(1024byte) -> 1Mbyte(1024Kbyte) -> 1G(1024Mbyte) -> 1T(1024Gbyte) -> 1P(1024Tbyte)
# 파이썬에서 리스트는 넓게 보면 시퀀스 자료형에 속한다.
# 시퀀스 요소들은 순서를 가지고 있고, 인덱스를 사용하여 참조할 수 있다.

# 인덱싱이란 리스트에서 하나의 요소를 인덱스 연산자를 통하여 참조(접근)하는 것을 의미한다. 항상 0부터 시작

myList = [0,1,2,3,4,5,6,7]
print(myList[3:6])

squares = [0,1,4,9,16,25,36,49]
print(squares[3:6])

# 문자열과 다르게 리스트는 변경이 가능하다.