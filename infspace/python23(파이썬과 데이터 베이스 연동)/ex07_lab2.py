# 문제2
# 문제1에서 입력한 데이터 3건을 아래와 같이 출력해주는 프로그램을 작성하시오.(select문 이용)

# 출력결과
# 제품코드      제품명      가격(만)        재고수량
# --------------------------------------------------
# p001          노트북      110             5
# p002          마우스      3               22
# p003          키보드      2               11
# --------------------------------------------------

import sqlite3

# 전역변수 선언
con, cur = None, None
pCode, pName, price, amount = "", "", "", ""

if __name__ == "__main__":
    # 모듈안에 있는 것이므로 함수보다는 '메소드'가 정확한 표현!
    con = sqlite3.connect("c:/pythonDB/naverDB")
    cur = con.cursor()
    cur = con.execute("select * from productTable")
    
    print("제품코드      제품명      가격(만)        재고수량")
    print("--------------------------------------------------")
    while True:
        row = cur.fetchone()
        if row == None:
            print("종료되었습니다.")
            break
        pCode = row[0]
        pName = row[1]
        price = row[2]
        amount = row[3]
        print("%5s       %5s        %5d           %5d" % (pCode, pName, price, amount))
        print("--------------------------------------------------")
   
    con.close()