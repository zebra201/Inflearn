# 리스트의 기초 연산들 실습하기

# 리스트에 요소 삽입하기
# append() 메서드 : 리스트.append(추가할 요소) 리스트 요소의 항상 마지막 끝에 추가된다.
# insert() 메서드 : 리스트명.insert(인덱스, 추가할 요소) 원하는 인덱스에 요소를 추가할 수있다.
li1 = ["TV", "오디오", "PC", "키보드"]
print("li1 의 주소 : ", id(li1))
print(li1)
# append() 사용
li1.append("마우스")
print("li1 의 주소 : ", id(li1))
print(li1)
# insert() 사용하여 원하는 인덱스에 요소 추가, 뒤에 요소들이 한 칸씩 밀려났다.
li1.insert(1, "휴대폰")
print("li1 의 주소 : ", id(li1))
print(li1)

# 리스트에서 요소 찾기
# in, not in 연산자들은 리스트에 요소가 존재하는지 확인하는 용도
print("-------------------------")
hero = ["스파이더맨", "배트맨", "슈퍼맨", "아이언맨", "헐크", "홍당무"]
if "배트맨" in hero:
    print("배트맨이 존재합니다.")
else:
    print("배트맨이 존재하지 않습니다.")

# 리스트에서 요소를 찾을 때 해당 요소의 인덱스를 알고자 한다면 index() 를 사용하면 된다.
# 아래와 같이 list 에 해당하는 값이 존재하지 않으면 index() 는 에러를 발생시킨다.
# 하여, 조건절과 in, not in 연산자를 이용하여 존재하는지 확인을 먼저 하는 습관을 들이도록 한다.
if "홍당무" in hero:
    index = hero.index("홍당무")
    print("홍당무의 인덱스 : ", index)
else:
    print("홍당무가 존재하지 않습니다")

# 리스트에서 요소를 삭제하는 방법
# 1번째 : 리스트명.pop(인덱스), 리스트에서 인덱스에 해당하는 요소를 삭제한 후, 요소를 반환한다.
# 2번째 : 리스트명.remove("요소"), 리스트에서 해당하는 요소가 있으면 삭제한 후, 요소를 반환 안한다.
# 3번째 : del 리스트명[인덱스], 리스트에서 인덱스에 해당하는 요소를 삭제한 후, 요소를 반환 안한다.
hero = ["스파이더맨", "배트맨", "슈퍼맨", "아이언맨", "헐크", "태권V", "배트맨"]
element = hero.pop(0)
print("element : ", element)
print(hero)

# remove() 메서드는 리스트의 요소 중 중복된 요소가 존재한다면 인덱스가 작은 요소를 먼저 제거를 한다.
hero = ["스파이더맨", "배트맨", "슈퍼맨", "아이언맨", "헐크", "태권V", "배트맨"]
value = "배트맨"
# 아래와 같이 중복된 요소를 한번에 삭제를 하고 싶다면 반복문을 이용하여 제거를 하도록 하자.
while value in hero:
    hero.remove(value)
print(hero)

# del 키워드로 요소를 삭제하기
hero = ["스파이더맨", "배트맨", "슈퍼맨", "아이언맨", "헐크", "태권V", "배트맨"]
del hero[:]     # 좌측과 같은 결과를 나타내는 것이 clear() 동일하다.
print(hero)

# 리스트의 모든 요소를 삭제를 하고자 한다면, 리스트명.clear() 사용하면 된다.
hero = ["스파이더맨", "배트맨", "슈퍼맨", "아이언맨", "헐크", "태권V", "배트맨"]
element = hero.clear()
print(element)
print(hero)

# 리스트에 포함된 특정 요소의 갯수를 알고자 할 때, count() 를 이용하면 된다.
hero = ["스파이더맨", "배트맨", "슈퍼맨", "아이언맨", "헐크", "태권V", "배트맨"]
cnt = hero.count("배트맨")
print(cnt)

# extend(list 타입의 매개변수)는 리스트를 더하는 함수( += 와 동일한 효과)
li1 = [1,2,3]
li2 = [10.1, 20.2]
# li1 += li2
li1.extend(li2)
print(li1)

