# 조건문 if 구문만 사용
score  = 63
# 몇 십개의 if 구문이 존재하더라도, CPU는 모든 if 문을 참조한다.
# 그러므로 App 프로그램의 성능은 떨어진다.
if score >= 90:
    print("점수가 90점 이상입니다. 학점은 A등급입니다.")
if score >= 80:
    print("점수가 80점 이상입니다. 학점은 B등급입니다.")
if score >= 70:
    print("점수가 70점 이상입니다. 학점은 C등급입니다.")
if score >= 60:
    print("점수가 60점 이상입니다. 학점은 D등급입니다.")
    