# 문자열에 대한 실습

# 큰따옴표(double quotation)로 묶으면 문자열이 된다. (권장)
welcome = "Happy New Year 2022"
print(welcome)

# 작은따옴표(single quotation)로 묶어도 문자열이 된다.
welcome = 'Happy New Year 2022'
print(welcome)

# 문자열을 만들때, 더블은 더블, 싱글은 싱글로 맞추어야 한다.
# welcome = "Happy New Year 2022'
# print(welcome)

# EOL에 " 누락 역시 에러 발생
# welcome = "Happy New Year 2022
# print(welcome)

# 아래와 같이 "" 안에 또 다른 ""이 들어 있다면
# 컴파일러가 혼돈을 일으켜 에러가 발생한다.
# message = "은혁이가 "안녕하세요" 라고 인사했습니다."
# print(message)

message = "은혁이가 '안녕하세요' 라고 인사했습니다."
print(message)

# 파이썬에서는 따옴표를 출력하과자 할 때, \를 이용한다.
# \가 따옴표 앞에 있으면 '는 특수한 의미를 잃어버리고
# 하나의 문자로 편승이 되어 문자열을 이룬다.

message = 'doesn\'t'
print(message)

message = "\"Yes, I can do it\""
print(message)

# 특수문자 형태인 \n은 개행(Enter)을 하는 문자이다.
message = 'First \nSecond \nThird'
print(message)

# 특수문자 \t 는 탭만큼 띄우는 문자이다.
message = 'c:\temp\name'
print(message)

# 위에서 살펴봤던 \t, \n 이런 이스케이프 문자들의 기능을 제거를 시키기 위해서
# 문자열 시작 앞에 r을 붙여준다. (중요함)
message = r'c:\temp\name\a.mp3'
print(message)

# 문자열의 길이를 알고자 한다면 len()함수를 이용한다.()
# 한글, 영어 상관없이 인식한다.
message = "신은혁"
print("문자열의 길이 :", len(message))
