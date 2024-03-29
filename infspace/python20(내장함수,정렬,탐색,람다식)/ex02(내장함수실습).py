# 내장함수를 이용한 문제해결
# 초대받는 사람의 이름을 리스트로 만들었다.
names = ["이현호", "김연아", "손연재", "손아섭"]
# 초대받은 사람과 동행하는 사람의 숫자를 리스트로 만들었다.
persons = [1,3,0,6]

# 파티의 총 인원 구하기
print("파티의 총 인원 : ", sum(persons) + 4)

# 파티에 최소 한사람이 오는지 확인하는 방법
# any() 함수를 이용하여 확인하면 된다.
print("파티에 한 사람이라도 오는가? : ", any(persons))

# 모든 초대받은 그룹이 전부 오는지를 확인하는 방법
# all() 함수를 이용하여 확인
print("모든 초대받은 그룹이 전부 오는가? : ", all(persons))

# 가장 많이 오는 그룹에는 몇 사람이 있는가?
# max() 함수를 이용하면 된다.
print("가장 많이 오는 그룹 : ", max(persons))

# 초대받은 사람과 동행하는 사람수를 묶어서 출력해보기
# for 문 zip() 함수 사용
for name, person in zip(names, persons):
    print(name, person)