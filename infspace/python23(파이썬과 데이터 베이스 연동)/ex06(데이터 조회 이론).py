# 이론
# 파이썬에서 데이터를 조회하는 코딩 순서
# 1. 데이터베이스 연결 (연결자 = sqlite3.connect("DB이름"))
# 2. 커서(통로,포인터) 생성 (커서이름 = 연결자.cursor())
# 3. 데이터 조회 (커서이름.execute("SELECT문"))
# 4. 조회한 데이터 출력(4반복) (커서이름.fetchone())
# 5. 데이터 베이스 닫기 (연결자.close()) (데이터입력이 아니므로 commit() 필요없다)

# tkinter 와 sqlite3 모듈을 합쳐서 4회 동안 실습예정(프로그램 제작)

# -------------------------------------------------------------
# 실습
# 파이썬에서 데이터를 조회하는 프로그래밍의 순서
# 1. DB연동
# 2. 커서 생성
# 3. 데이터조회 (select 문) : 커서를 통해서 조회를 하는데
#    조회된 내용은 전부 커서에 저장이 된다. (메모리 저장)
# 4. 조회된 내용들은 출력 : 커서를 이용하여 fetchone(), fetchall() 함수들을 통해서
#    콘솔에 출력하게 된다.
# 5. DB 연결종료
# 6. commit()이 빠진 이유는 조회부분이기 때문에 디스크에
#    저장, 삭제, 수정 이런 쿼리가 아니기 때문에 commit()을 사용할 이유가 없다.

import sqlite3
# 전역변수 선언
con, cur = None, None
id, userName, email, birthYear = "", "", "", ""
row = None          # 한 행을 가져와서 저장할 전역변수
rows = None         # 전체 행을 가져와서 저장할 전역변수

if __name__ == "__main__":
    # DB 연결
    con = sqlite3.connect("c:/PythonDB/naverDB")
    # 커서 생성
    cur = con.cursor()
    cur.execute("select * from userTable")      # 조회된 데이터 전부 저장됨
    
    # 1990년 포함 이후에 출생한 사용자들을 출력하는 쿼리
    # cur.execute("select * from userTable where birthYear >= 1990")
    
    # 출생년도를 기준으로 오름차순 정렬하는 쿼리이다
    # 단, 기본값이 asc 이기 때문에 생략가능하다.
    # cur.execute("select * from userTable order by birthYear")
    
    # 출생년도를 기준으로 내림차순 정렬하는 쿼리이다. 하지만 내림차순하는 desc 생략불가
    # cur.execute("select * from userTable order by birthYear desc")
    
    # 아래 쿼리문은 한 명만 출력해주는 쿼리문이다.
    # cur.execute("select * from userTable where id = 'shin'")
    
    print("사용자ID     사용자이름      이메일              출생년도")
    print("---------------------------------------------------------")
    # 무한루프를 돌면서 1행씩 가져와서 출력을 한다.
    while True:
        row = cur.fetchone()        # 튜플형태로 행을 하나씩 가져온다.
        # 무한루프를 빠져나가는 상황
        if row == None:      # 더이상 가져올 데이터가 없다면 탈출
            print("종료되었습니다.")
            break
        # 한 행에 있는 데이터를 각각 전역변수에 저장 후 출력
        id = row[0]
        userName = row[1]
        email = row[2]
        birthYear = row[3]
        print("%5s    %15s    %15s        %5d" % (id,userName,email,birthYear))
    
    # print("전체 행을 한번에 가져오는 fetchall() 함수 사용")
    # fetchall() 를 사용하면 튜플리스트 형태로 전체 행을 반환해준다.
    # rows = cur.fetchall()
    # for data in rows:
    #     print(data)
    
    
    print(rows)
    
    
    # DB연결 해제
    con.close()
    
    