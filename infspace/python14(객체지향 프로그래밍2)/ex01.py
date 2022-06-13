# 이론1
# 인스턴스가 전달되면 함수가 인스턴스를 변경할 수 있다.
# 함수에 인스턴스를 전달하면 객체의 참조값이 전달된다.
# 특수 메소드 사례
# 2차원 공간에서 벡터(vector)는 (a,b)와 같이 2개의 실수로 표현될 수 있다.

# 이론2
# 객체지향 개념에서
# 오버로딩 : 같은 메소드 명으로 매개변수 와 데이터 타입,
# 순서에 따라서 다른 메소드가 호출되는 것(new), 파이썬에서는 미지원
# 오버라이딩 : 상속관계, 같은 메서드명, 매개변수도 동일,
# 개수도 동일한데 그것을 구현부만 다르게한다.(modify), 파이썬에서 지원

# 변수의 종류
# 지역 변수 : 함수 안에서 선언되는 변수
# 전역 변수 : 함수 외부에서 선언되는 변수
# 인스턴스 변수 : 클래스 안에 선언된 변수, 앞에 self. 가 붙는다.

# None 참조값(null)
# None 은 아무것도 차몾하지 않고 있다는 것을 나타내는 특별한 값
# tv = None
# 어떤 변수가 None 인지 아닌지 검사하려면,
# if tv is None:
#     print("현재 TV가 없습니다")
# tv.setChnannel(5) # 이는 오류이다

# 클래스 상수 정의
# 상수들은 흔히 클래스 변수로 정의된다.