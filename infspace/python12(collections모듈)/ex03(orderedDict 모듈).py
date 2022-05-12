# OrderedDIct 모듈 : 순서를 가진 딕셔너리 객체
# 딕셔너리는 순서를 보장하지 않는 개체이다.
# d = OrderedDict()
# 파이썬 버전 3.7 이상으로 올라오면서, 딕셔너리도 순서를 저장하는 방식으로 개선됨.

# from typing import OrderedDict
from collections import OrderedDict

d = OrderedDict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 400

print(d.items())
print(d['x'])
print("-" * 50)

# 일반적인 딕셔너리 테스트
# 딕셔너리는 인덱스가 없었으나, 파이썬 버전이 3.6 이상이 되면서,
# 일반 딕셔너리가 입력된 순서대로 정확하게 출력되고 있다.
# 버전이 2.x 에서는 순서가 보장되지 않는다. (파이썬 튜터를 통해 확인가능)
dic = {}
dic['a'] = 100
dic['b'] = 200
dic['c'] = 300
dic['d'] = 400
dic['e'] = 500
dic['f'] = 500
dic['g'] = 500
dic['h'] = 500
dic['i'] = 500
dic['j'] = 500
dic['k'] = 500


for k,v in dic.items():
    print(k,v)
print("-" * 50)    


# OrderedDict는 딕셔너리 순서, 동등성 비교를 개선한 모듈이다.
from collections import OrderedDict

dic = OrderedDict()
dic['a'] = 100
dic['b'] = 200
dic['c'] = 300
dic['d'] = 400
dic['e'] = 500
dic['f'] = 500
dic['g'] = 500
dic['h'] = 500
dic['i'] = 500
dic['j'] = 500
dic['k'] = 500


for k,v in dic.items():
    print(k,v)