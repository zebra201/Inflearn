# 임의의 숫자를 발생시켜 사용자로부터 입력을 받아
# 숫자를 맞추는 게임을 만들어보기(while)

from random import *
# 1~100까지 임의의 수(난수)를 발생시키는 코드

cnt = 0
num = randint(1,100)
print("발생한 난수의 값은 %d 입니다." % num)

print("1부터 100까지의 숫자를 맞추어 보세요.")
print("기회는 단 10번입니다")

# 무한루프가 아닌, 10번안으로 맞추기(즉, cnt < 10)
while cnt < 10 :
    guess = int(input(str(cnt+1) + "번 째 도전, 숫자를 입력하세요 : "))
    cnt += 1
    
    if guess < num:
        print("입력한 수가 정답보다 낮습니다.")
    elif guess > num:
        print("입력한 수가 정답보다 높습니다.")
    elif guess == num:
        print("정답입니다! 시도횟수 : %d번" % cnt)
        code = input("게임을 계속 하시겠습니까? y or n : ")
        # 중첩 if 문이 들어가서 게임의 지속 여부를 확인하는 코드
        if code == "n":         # 게임 종료코드
            print("게임을 종료합니다.")
            break
        else:                   # 게임 지속코드
            print("-------------------------------")
            # 게임을 재시작을 하기 위해서 다시 난수발생과 cnt를 초기화 해야한다.
            print("게임을 재시작합니다.")
            num = randint(1,100)
            print("발생한 난수의 값은 %d 입니다." % num)
            cnt = 0
            
print("10번의 기회가 소진되었습니다. 게임이 종료됩니다.")
    