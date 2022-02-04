# 리스트에 대한 실습
# 리스트의 정의 : 여러 개의 값을 모아서 하나의 변수에 저장할 수 있는 데이터 파일.
# 아주 유용하게 널리 사용된다. 리스트는 [] 안에 값을 저장한다.
city = ["서울", "부산", "대구", "광주", "인천"]
# 리스트의 길이를 알아내고 싶을 때에서 역시 len() 함수를 사용하면 된다.
print(len(city))
print(city)
print(city[2])

# 리스트에서는 아래와 같이 해당 인덱스 값이 변경 가능한 객체이다.
city[1] = "전주"
print(city)

# 리스트는 정수, 문자열에 국한되지 않고 여러 개의 값을 저장할 수 있다.
temp = ["대구", "부산", 100, 10.798]
print(temp)

# 한 사람의 정보를 출력
name = input("한 사람의 이름 :")
age = input("한 사람의 나이 :")
address = input("한 사람의 주소 :")
height = int(input("한 사람의 키 :"))
weight = int(input("한 사람의 몸무게 :"))

person = [name, age, address, height, weight]
print(person)


    