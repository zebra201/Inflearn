# if ~ elif ~ else(옵션) 대한 연습

score = int(input("성적을 입력하세요(0~100) : "))
# 다중 조건 중 하나만 만족하면 그 이후의 조건은 검사하지 않는다.(중요)
# if 구문으로만으로도 작성이 되지만 CPU에 부하가 걸리므로
# 좋은 프로그램이 되지 않음.

if score >= 90 :
    print("학점 A")
elif score >= 80 :
    print("학점 B")
elif score >= 70 :
    print("학점 C")
elif score >= 60 :
    print("학점 D")
else:       # else 구문은 옵션이지만 다중 조건을 설정할 때는 절대 조건을 명기해서는 안된다.
    print("학점 F")