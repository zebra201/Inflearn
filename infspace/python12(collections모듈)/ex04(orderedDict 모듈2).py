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
