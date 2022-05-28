# namedtuple 모듈은 튜플의 형태로 데이터 구조체를 저장하는 방법이다.
# ex : 학생이라는 정보를 저장하기 위한 변수(학번, 이름, 학년, 학과)
# 튜플이지만 _replace() 로 객체 값을 변경할 수 있다.
# _fields 를 통해 필드명 출력이 가능하다.
# getattr()는 namedtuple()의 인스턴스(객체)의 값을 추출해준다.
# double-star-opperator(**) 딕셔너리를 namedtuple() 로 변환해준다.

# namedtuple 모듈은 튜플의 형태로 데이터를 구조화에 맞게끔
# 저장하는 자료구조이다.

# 일반적인 튜플의 경우
person1 = ("이현호", 14, "남")
person2 = ("강은비", 17, "여")
for n in [person1, person2]:
    # %n 들어가면서 튜플의 값들을 각각에 형식지정자에 맞게끔 적용시킨다
    print("%s은(는) %d세의 %s 입니다." %n)
# print("%s은(는) %d세의 %s 입니다." % (person1[0], person2[1], person1[2]))
# 일반적인 튜플은 .(접근연산자) 사용을 하지 못하고 인덱스로만 접근이 가능하다.

print(person1[0])
# 일반적인 튜플은 값의 수정이나 변경이 이루어지지 않는다.
# person1[0] = "김현호"

print("-" * 50)

# namedtuple 인 경우
from collections import namedtuple
# Person 이라는 namedtuple 을 정의
Person = namedtuple(typename="Person", field_names=("name age gender addr"))
p1 = Person(name = "김연아", age = 20, gender = "여성", addr = "대전")
p2 = Person(name = "손연재", age = 22, gender = "여성", addr = "서울")
for n in [p1,p2]:
    print("%s은(는) %d세의 %s 입니다. 그리고 거주지는 %s 입니다." %n)
# Person 이라고 정의를 해놓았고 그의 필드들이 3개가 존재하고 있기 때문에
# namedtuple 은 .(접근연산자)를 이용할 수도 있지만 인덱스로 접근도 가능하다.
print(p1.name, p1.age, p1.gender)
print(p2.name, p2.age, p2.gender)
print(p2[0], p2[1], p2[2])
print("-" * 50)

# namedtuple 의 _make() 메소드 : 기존의 생성된 namedtuple 에
# 새로운 인스턴스를 생성해주는 메소드이다.
# _make() 안의 매개변수로 들어가는 것은 시퀀스 자료형이어야 한다.
p3 = Person._make(["이현호", 20, "남성", "세종"])
for n in [p1,p2,p3]:
    print("%s은(는) %d세의 %s 입니다. 그리고 거주지는 %s 입니다." %n)
print("-" * 50)

# namedtuple에서는 인덱스를 통한 값변경은 되지 않지만,
# _replace() 메소드로 값 변경이 가능하다.
p1 = p1._replace(name = "강백호")
p2 = p2._replace(age = 100)
p3 = p3._replace(addr = "달성군")
for n in [p1,p2,p3]:
    print("%s은(는) %d세의 %s 입니다. 그리고 거주지는 %s 입니다." %n)
print("-" * 50)    

# 생성되어진 Person 이라는 namedtuple 의 _fields 로써
# Person에 있는 필드명 tuple() 형식으로 리턴을 해준다.
print(p1._fields)

# getattr() 메소드를 통해 필드명으로 그 값을 출력할 때 사용한다.
print(getattr(p1, 'name'))
print(getattr(p2, 'name'))
print(getattr(p3, 'name'))

# **(double-star-operator) 원래 제곱할 때 사용하는 연산자이나,
# namedtupe() 딕셔너리 자료구조를 namedtupe() 변환하여 반환한다.
dic = {'name' : "신은비", "age" : 15, "gender" : "여성", "addr" : "대전"}
print(type(dic))
print(dic)
p4 = Person(**dic)
print("%s은(는) %d세의 %s 입니다. 그리고 거주지는 %s 입니다." %(p4.name, p4.age, p4.gender, p4.addr))
print(type(p4))