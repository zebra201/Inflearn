# 1에서부터 100까지의 누적합계를 구하는데 누적값이 2000이상이 되면
# for 문을 빠져 나오는 프로그램을 작성하시오.
# 디버깅 -> 에러를 추적하여 수정하는 과정.
    
# 매우 중요(중단점)
# breakpoint(중단점, F9)는 디버깅(에러를 잡아나가는 과정)에 아주 효율적으로
# 사용할 수 있다. (F5 로 디버깅 실행, shift + F5 로 종료)
# 한 단계식 변수의 값이 변화되는 과정을 살펴보기 위해서는
# F10 키를 눌러 디버깅을 할 수가 있다.(F9 로 중단점 설정)
# 수 없이 많은 에러를 만날 수록 자신이 성장한다.
# 디버깅 모드로 추적. 에러에 혼란스러워 하지 말라.
# 개인별로 차이가 있을 뿐
hap = 0
for i in range(1,101):
    # 2000이상이면 for 루프를 빠져 나오는 코드
    if hap >= 2000:
        print("마지막으로 더해진 i의 값 : ", i-1)
        break
    else:
        hap += i
print("hap : ", hap)