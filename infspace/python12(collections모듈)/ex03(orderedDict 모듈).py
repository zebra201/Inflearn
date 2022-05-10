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