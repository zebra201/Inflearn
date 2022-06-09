# 문제
# 은행 계좌에 돈을 저금할 수 있고 인출을 할 수도 있다.
# 은행 계좌를 간단하게 클래스로 정의해보자
# 은행계좌(Account)는
# 현재 잔액(balance)을 필드로 선언하고 기본 생성자를 작성하고
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
    
    # 생성자 선언
    def __init__(self):
        self.__balance = 0
    
    # getter, setter
    def getBalance(self):
        return self.__balance
    
    # 입금 메소드
    def deposit(self, amount):
        self.__balance += amount
        print(format(amount,","),"원이 입금되었습니다")
        print("현재 잔액은", format(self.getBalance(),","),"입니다.")
        return self.__balance
    
    # 출금 메소드
    def withdraw(self, amount):
        self.__balance -= amount
        if self.__balance < 0:
            print("잔액이 부족합니다.")
            return
        else :
            print(format(amount,","),"원이 출금되었습니다")
            print("현재 잔액은", format(self.getBalance(),","),"입니다.")
    

if __name__ == "__main__":
    account1 = Account()
    account1.deposit(1000000)
    account1.withdraw(200000)
    
    

