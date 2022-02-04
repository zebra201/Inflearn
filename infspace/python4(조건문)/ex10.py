# 쇼핑몰에서 물건을 구매할 때, 구입액이 5만원 이상이면 5%의 할인을
# 해준다고 하자. 사용자에게 구입금액을 입력받고 최종적으로 할인금액과
# 지불금액을 출력하는 프로그램 만들기.

pay_money = int(input("구입금액 : "))
dis_money1 = 0  # 없어도 되긴 함.
dis_money2 = 0  # 없어도 되긴 함.
if pay_money >= 50000:
    dis_money1 = pay_money * 0.95
    dis_money2 = pay_money * 0.05       # 할인금액
    # dis_money1 = pay_money - dis_money2
    print("할인금액 :", dis_money2, "원")
    print("할인된 지불금액 : ", dis_money1, "원")
else:
    print("할인금액 : 0", "원")
    print("지불금액 : ", pay_money, "원")
