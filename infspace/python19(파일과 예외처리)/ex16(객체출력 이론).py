# 이론
# 딕셔너리와 같은 객체를 파일에 저장하기 위하여 파이썬에서는
# pickle 모듈을 가장 많이 사용한다.
# import pickle
# 객체를 pickle 모듈로 압축하려면 dump() 함수를 사용.
# 정규식 : 특정한 규칙을 가지고 있는 문자들을 메타문자를 이용하여 표현하는 수식
# 메타문자에서 가장 중요한 문자는 . 과 * 이다.
# -----------------------------------------------------------

# 실습
# 딕셔너리의 파일쓰기와 읽기
import pickle

# # 딕셔너리를 만듦,
# gameOption = {
#     "Sound" : 8,
#     "VideoQuality" : "HIGH",
#     "Money" : 10000,
#     "WeaponList" : ["gun", "missile", "knife"] 
# }

# file = open("ex16(save.p)", "wb")   # 이진 파일 오픈(확장자는 상관없음)
# pickle.dump(gameOption, file)       # 딕셔너리를 피클 모듈을 이용하여 파일로 저장
# file.close()

# -----------------------------------------------------------

# 딕셔너리로 출력된 파일 읽기
file = open("ex16(save.p)", "rb")       # 이진파일 오픈
obj = pickle.load(file)
print(obj)