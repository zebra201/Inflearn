# 얕은 복사 : 리스트 자체는 다른 곳(힙, 변수는 스택)에 저장되고, 참조값만 변수에 저장된다.
# 참조값이란 메모리에서 리스트 객체의 주소값이다.
# 얕은 복사는 원본 리스트의 값까지 변경시킨다.(같은 주소값을 가지고 있기 때문)

# 깊은 복사(deep copy)
# 첫 번째 : list() 메소드 사용
# 두 번째 : deepcopy() 나 copy() 메서드 사용, from copy import deepcopy, values = deepcopy(scores)
# 세 번째 : [:] 인덱스를 이용, values = scores[:]

# 값으로 호출하기(Call by Value) : 변수의 값이 복사되는 방식
# 참조로 호출하기(Call by Reference) : 변수의 참조가 전달되는 방법
# 변경가능한 객체 : 리스트, 딕셔너리
# 변경불가능한 객체 : 정수형, 문자열, 튜플

# -----------------------------------------------------------
# 리스트 복사하기
# 얕은복사(shallow copy) : 주소값을 공유하는 개념, 원본 리스트에 영향을
# 끼치는 복사 방법, 엄밀히 말하자면 진정한 복사가 아니다.

scores = [10,20,30,40,50]
refer = scores # scores의 주소값을 refer 변수에게 복사
print("scores 의 주소값 : ", id(scores))
print("refer 의 주소값 : ", id(refer))
refer[0] = 100
refer.append(-70)
refer.insert(1, -100)
print("scores 의 주소값 : ", id(scores))
print("refer 의 주소값 : ", id(refer))
print("scores 의 요소값 : ", scores)
print("refer 의 요소값 : ", refer)