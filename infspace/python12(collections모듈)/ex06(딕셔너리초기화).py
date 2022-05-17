# 함수를 이용하여 딕셔너리를 초기화한든 코드를 실습하기

from collections import defaultdict
# 일반 딕셔너리 함수를 이용하여 초기화 방법
def countLetters(word):
    counter = {}
    for letter in word:
        # 넘어온 문자열의 값을 하나가 키가 되고 그 키에 기본값으로 0을 설정함.
        if letter not in counter:
            counter[letter] = 0
    return counter


# setdefault() 메서드를 이용한 초기화 방법
def countLetters_setdefault(word):
    counter = {}
    for letter in word:
        # 위의 counterLetters() 보다 조건절은 사라졌지만
        # 루프를 돌 떄마다, setdefault()를 계속 호출함으로 비효율적이다.
        counter.setdefault(letter, 0)
    return counter


# defaultdict 모듈을 직접 이용하는 방법
def countLetters_defaultdict(word):
    # 이 함수에서는 defaultdict() 만 한 번 호출이 일어난다.
    counter = defaultdict(lambda : 0)
    for letter in word:
        counter[letter] += 1
    return counter


if __name__ == "__main__":
    dic = countLetters("가나다라마바사")
    print(dic.items())
    print("-" * 50)
    dic = countLetters_setdefault("가나다라마바사")
    print(dic.items())
    print("-" * 50)
    dic = countLetters_defaultdict("가나다라마바사")
    print(dic.items())
    

# (실습)
# 이번 예제는 함수를 이용하여 각 알파벳의 글자 수를 세어서 저장을 하고
# 딕셔너리를 리턴하는 코드를 짜보자