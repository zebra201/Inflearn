# sqlite3(DBMS) 설치 후 실습
# select * from userTable;
# DB를 만든 뒤 테이블 생성
# 명령어를 입력 후 세미콜론(;) 입력이 필요함.

# .open : DB를 열거나 없다면 생성한다.
# sqlite> .open naverDB
# sqlite> .databases
# main: C:\sqlite\naverDB r/w
# sqlite> .help     # 명령어 도움말

# DDL : Data Definition Language



# .schema userTable: userTable 이 어떻게 만들어졌는지 말해줌
# create table userTable : userTable 새성
# drop table userTable : userTable 삭제
# sqlite> .table    # 테이블 열기
# userTable

# userTable에 데이터 입력
# insert into userTable values('john', 'john Bann', 'jhon@naver.com', 1990);

# sqlite> select * from userTable;      # 입력한 데이터값 확인
# john|john Bann|jhon@naver.com|1990

# sqlite> .header on        : 헤더를 보이게 설정
# sqlite> .mode column      : 각 칸의 콜럼 좌측정렬을 해줌

# id    userName   email           birthYear
# ----  ---------  --------------  ---------
# john  john Bann  jhon@naver.com  1990
# kim   Kim Chi    kim@daum.net    1992
# lee   Lee Pal    lee@paran.com   1988
# shin  신은혁        shin@kakao.com  2008

# where(조건)으로 id 가 shin 인 userName 을 'Shin Eun Hyuk' 으로 변경
# 만약 where id 조건을 주지 않으면 모든 userName 이 변경된다.
# sqlite> update userTable set userName='Shin Eun Hyuk' where id = 'shin';

# sqlite> select * from userTable;

# id    userName       email           birthYear
# ----  -------------  --------------  ---------
# john  john Bann      jhon@naver.com  1990
# kim   Kim Chi        kim@daum.net    1992
# lee   Lee Pal        lee@paran.com   1988
# shin  Shin Eun Hyuk  shin@kakao.com  2008

# delete from userTable;        # 조건이 없다면 userTable 전체삭제
# id 가 john 인 데이터만 삭제
# sqlite> delete from userTable where id = 'john';

# *(아스타리스크) : 전체를 의미한다

# update userTable set userName = "이현호" where id = 'shin';
