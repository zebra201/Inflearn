# 문자열의 연결
# + 연산자는 문자열 사이에 들어가면 문자열을 연결해주는 역할을 한다.

first_name = ' Hyun-ho'
Last_name = 'Lee'
name = Last_name + first_name
print(name)

# 파이썬에서는 모든 데이터에는 데이터 타입이 존재한다. 아래 소스코드에서 확인하면
# "Person"은 문자열이고, 100은 int 타입이다. 타입이 불일치하므로 연결이 안됨.
# 문자열은 숫자열로 변환이 불가.
# 숫자로 변환이 가능한 리터럴은 가능하다. ex ) int("100")
temp = "Person" + str(100)
print(temp)

# 해결하기 위해서 숫자100 을 문자열로 변환하여 타입을 일치시킴.
temp = "Person" + str(100.188)
print(temp)

# 문자열을 숫자로 변환
# 정수일때는 int()를 사용.
price = int("123456")
print(type(price))
print(price)

# 실수일때는 float()를 사용.
price = float("123456.187")
print(type(price))
print(price)

# 문자열의 반복
# 문자열에서 * 연산자를 사용하면 그만큼 반복이 된다.
arrow = "->" * 10
print(arrow)

arrow = "->"
print(arrow * 10)

# %s(형식지정자)
# %s 는 문자열이나 숫자값을 변수에 대입해서 자주 변경이 있을 경우
# 이런 형식을 지정하여 상황에 맞게끔 출력을 하도록 하면 될 것이다.
# %s 에 정수를 대입
price = 1000
print("가격 : %s" % price)

# %s 에 문자열을 대입
time = "13:49"
print("현재 시간 : %s" % time)

# %s 를 2개 이상 사용하고자 할때에는 해당하는 %s 의 개수를
# 소괄호로 묶어서 형식 지정자에 대입을 해줘야한다.
temp = "현재시간은 %s 시 %s 분 %s 초 입니다."
print(temp % (12, 38, 20))
