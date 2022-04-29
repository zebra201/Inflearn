# 영한 사전 만들기
# 공백 딕셔너리 생성하고 여기에 영어단어를 키로 하고 설명을 값으로 저장하면 될 것이다.
# 출력결과
# 단어를 입력하시오(종료하려면 "종료") : one
# 하나
# 단어를 입력하시오(종료하려면 "종료") : python
# 해당하는 단어가 없습니다
# 단어를 입력하시오(종료하려면 "종료") : 종료
# 프로그램을 종료합니다
# -------------------------------------------------------

# dic = {"one":"하나", "two":"둘"}


# if __name__ == "__main__":
#     set1 = {}
#     set1 = input("단어를 입력해 주세요 :")
#     if dic.keys == set1:
#         print("하나")
#     else:
#         print("해당하는 단어가 존재하지 않습니다.")

# -------------------------------------------------------

eng_dict = dict()   # 빈 딕셔너리 생성
# 빈 딕셔너리에 데이터를 추가하기
# eng_dict["one"] = "하나, 일"
# eng_dict["two"] = "둘, 이"
# eng_dict["three"] = "셋, 삼"
# eng_dict["four"] = "넷, 사"
# eng_dict["five"] = "다섯, 오"

eng_dict = {'one': '하나, 일', 'two': '둘, 이', 'three': '셋, 삼', 'four': '넷, 사', 'five': '다섯, 오'}


while True:
    word = input("단어를 입력하세요(종료하려면 '종료') : ")
    # 무한루프를 빠져나가는 코드가 필요하다
    if word == "종료":
        print("프로그램을 종료합니다.")
        break
    # 입력한 단어가 있는지 확인
    elif word in eng_dict:
        print(eng_dict.get(word))   # 딕셔너리에 해당하는 단어가 존재하면 출력
        print("-" * 50)
    else:
        print("해당하는 단어가 존재하지 않습니다.")
        print("-" * 50)