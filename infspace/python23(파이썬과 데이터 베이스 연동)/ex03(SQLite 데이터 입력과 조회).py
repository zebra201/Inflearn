# 이론
# 파이썬 코드에서 SQLite 를 활용해 데이터를 입력하고 조회해보자

# import sqlite3
# 파이썬에서 데이터를 입력하는 코딩 순서
# 1. 데이터베이스 연결, 연결자 = sqlite3.connect("DB이름")
# 2. 커서생성 (커서이름=연결자.cusor())
# 3. (테이블 만들기) (커서이름.execute("CREATE TABLE 문"))
# 4. 데이터 입력(반복) (커서이름.execute("INSERT 문"))
# 5. 입력한 데이터 저장 (연결자.commit())
# 6. 데이터베이스 닫기 (연결자.close())
# 이는 SQLite3 와 파이썬 SQLite 는 별도이다.

# 커서(Cursor)는 데이터베이스에 SQL 문을 실행하거나 실행된 결과를 돌려받는 통로이다.
# 반드시 만들어야한다.

# # create table userTable(id char(4), userName char(15), email char(15), birthYear int);

# insert into userTable values(?,?,?,?),(data1,data2,data3,data4)