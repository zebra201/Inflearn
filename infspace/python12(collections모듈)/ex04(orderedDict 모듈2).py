# 일반적인 딕셔너리를 정렬을 하여 OrderedDDict 로 포장하기

dic = {}
dic['z'] = 100
dic['m'] = 200
dic['3'] = 300
dic['g'] = 400
dic['e'] = 500
dic['f'] = 500
dic['d'] = 500
dic['h'] = 500
dic['1'] = 500
dic['c'] = 500
dic['i'] = 500

# 키의 값으로 정렬을 해봄
li1 = (sorted(dic.keys()))
li2 = (sorted(dic.values()))

print(li1)
print(li2)
print(dic["3"])
# key 값과 value 값이 서로 정렬되어 있지 않음
print("-" * 50)    

from collections import OrderedDict

# 넘어오는 t의 값은 딕셔너리의 요소이다.
# 따라서 0번째 인덱스 키값이 될 것
def sort_by_key(t):
    return t[0]     # t값이 0이면 key 값으로 정렬, 1이면 value 값으로 정렬

dic1 = {}
dic1['z'] = 100     # z : 100
dic1['m'] = 200
dic1['3'] = 300
dic1['g'] = 400
# OrderedDict로 wrapping 을 하면 기존 딕셔너리와 리스트의
# 순서를 지키면서 딕셔너리 형태로 관리할 수 있다.
for k,v in OrderedDict(sorted(dic1.items(), key = sort_by_key)).items():
    print(k,v)
    
print("-" * 50)
li3 = sorted(dic1.items(), key = sort_by_key)
print(li3)
print("-" * 50)


# 딕셔너리의 동등성 비교
# 동등성은 논리적 동등이라는 것을 의미한다. 논리적 동ㅇ등이란 주소는 다르지만
# 요소들의 값이 순서가 비록 틀리더라도 논리적 동등으로 바라보는 시점이다.
str1 = "이현호"
str2 = str()
str2 = "이현호"

print(id(str1))
print(id(str2))
print(str1 == str2)

a = 10
b = 10
a += 1
b += 2
print(id(a))
print(id(b))
print("-" * 50)

# 일반적인 딕셔너리 동등성 비교
dic1 = {"가":1, "나":2, "다":3}
dic2 = {"가":1, "다":3, "나":2}
print(id(dic1))
print(id(dic2))
print(dic1 == dic2)
print("-" * 50)

from collections import OrderedDict
# orderedDict 는 순서도 확인한다.
# 일반적인 딕셔너리보다 좀 더 깐깐하고 디테일하게 비교하는 것이 바로
# OrderedDict의 특징이다.
ordered_dic1 = OrderedDict({"가":1, "나":2, "다":3})
ordered_dic2 = OrderedDict({"가":1, "다":3, "나":2})
ordered_dic3 = OrderedDict({"가":1, "나":2, "다":3})
print(id(ordered_dic1))
print(id(ordered_dic2))
print(ordered_dic1 == ordered_dic2)
print(ordered_dic1 == ordered_dic3)

# 결론
# 첫 번째는 OrderedDict 모듈은 딕셔너리의 순서대로 저장하지 않는 방식을 순서대로
# 저장하는 방식으로 개선되었다. (파이썬 버전이 3.6 이후로는 저장과 출력이
# OrderedDict와 동일하게 작동을 하고 있지만 2.x 버전에서는 문제점이 발생)
# 두 번째는 딕셔너리의 동등성 비교에서 일반적인 딕셔너리라는 순서를 유지핮
# 않아도 해당 키와 값이 동등하다면 True를 리턴하지만, OrderedDict에서는
# 순서, 키, 값이 무조건 같아야만 True를 리턴한다.
# OrderedDict 를 사용을 하면 정확한 데이터의 순서나 값을 유지하는데 일반
# 딕셔너리에 비해서 장점이 있다.
# 딕셔너리보다는 OrderedDict 모듈을 이용하는 것이 좋다.