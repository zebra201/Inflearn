# 문제
# 은행 계좌에 돈을 저금할 수 있고 인출을 할 수도 있다.
# 은행 계좌를 간단하게 클래스로 정의해보자
# 은행계좌(Account)는 현재 잔액(balance) 을 필드로
# 선언하고 기본 생성자를 작성하고
# 입금(deposit) 메소드와
# 출금(withdraw) 메소드를 작성해보자
# 출력결과
# 통장에 1,000,000원이 입금됨
# 현재잔액 : 1,000,000원
# 통장에 200,000원이 출금됨
# 현재잔액 : 800,000원
# -------------------------------------------------------

class Account:
    # 필드 선언
    __balance = 0
    
    # 기본생성자
    def __init__(self):
        self.__balance = 0
    
    # getter() 메서드 제공        
    def getBalance(self):
        return self.__balance
    
    # 입금 메서드 만들기
    def deposit(self, amount):
        self.__balance += amount
        print("통장에 ", format(amount,","),"원이 입금됨")
        print("현재잔액 : ", format(self.getBalance(),",") ,"원")
    
    # 출금 메서드 만들기
    def withdraw(self, amount):
        self.__balance -= amount
        if self.__balance < 0:
            print("잔액이 부족합니다.")
            return
        else:
            print("통장에 ", format(amount,","),"원이 출금됨")
            print("현재잔액 : ", format(self.__balance,",") ,"원")
    

if __name__ == "__main__":
    # choice = int(input("입급은 deposit, 출금은 2번을 눌러주세요 : "))
    account = Account()
    account.deposit(1000000)
    account.withdraw(200000)