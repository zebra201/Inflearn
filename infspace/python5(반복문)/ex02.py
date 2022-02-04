# range()의 함수 실습하기

# 1. range(x) 매개변수 1개짜리 함수를 이용.
hap = 0
for x in range(10):
    hap = hap + x
print("1. 0부터 9까지의 누계 : ", hap)

# 2. range(start,stop) 매개변수 2개짜리 함수를 이용.
# 누적을 하는데 stop 값은 포함하지 않음.
hap = 0     # hap 을 계속 초기화 해야 함. 위에서도 사용
for x in range(0,10):
    hap = hap + x
print("2. 0부터 9까지의 누계 : ", hap)

# 함수 한개에 여러개의 역할을 짐을 지게 한다 => 오버로딩의 개념

# 3. range([start],stop,[step]) 매개변수 3개짜리의 함수를 이용.
# 대괄호 []로 감싸져 있는 매개변수 값은 생략 가능하다.
# 누적을 하는데 step 만큼 건너띄어 리스트를 생성한다.
hap = 0
for x in range(0,10,1):
    hap = hap + x
print("3. 0부터 9까지의 누계 : ", hap)

# 문자열 실습
# 문자열도 시퀀스의 대상에 포함된다.
# 하여 for 문을 통해 문자를 추출하여 출력할 수 있다.
s = "Shin Eun Huck"
for ch in s:
    print(ch, end=" ")
    
