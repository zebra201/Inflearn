# 함수를 이용하여 각 알파벳의 글자의 수를 세어서 키로 저장을 하고
# 단어는 값으로 저장한느 딕셔너리를 리턴하는 코드를 보자 (set 이용)

from collections import defaultdict
# words 라는 set 를 받아서 길이를 키로 저장을 하고 값을 리스트 값으로 하고
# 단어는 값으로 저장하는 딕셔너리를 리턴하는 함수
def counterWords(words):
    grouper = defaultdict(set)
    print(grouper)
    for word in words:
        length = len(word)
        # set 에는 append 가 없으므로, add 사용
        grouper[length].add(word)
    return grouper
    
    

if __name__ == "__main__":
    set1 = set()
    set1.add("한국")
    set1.add("미국")
    set1.add("우즈베키스탄")
    set1.add("사우디아라비아")
    set1.add("스페인")
    
    dic1 = counterWords(set1)
    print(dic1)