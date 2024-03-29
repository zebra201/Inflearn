# 이론

# 데이터베이스으 기본 개념, 작동방법, 파이썬에서 데이터베이스를 활용하는 방법
# SQL(Structured Query Language) : 구조 질의어
# DBMS에서 어떤 작업을 하고 싶다면 DBMS 가 알아듣는 말로 지시해야한다.
# SQL 은 사용자와 DBMS가 소통하는 언어이다.
# 데이터베이스 : 파일 처리는 데이터를 저장하기 좋은 방법으로 양이 적을 때
# 적합한 형태이다. 대량의 데이터가 발생하는 현대 사회에서는 파일 처리로는 한계가 있는데,
# 이를 해결할 수 있는 방법이 데이터베이스이다.
# 한마디로, 대량의 데이터를 체계적으로 저장해 놓은 것
# 데이터베이스 관리 시스템 (DBMS)
# 관게형 데이터 베이스 (RDBMS) : 과거에는 시스템 자원을 많이 차지하여 속도가 느렸으나
# 현재는 많이 개선되었다.
# SQLite 는 표준 SQL 의 개념은 동일하게 적용되면서도
# 훨씬 가볍게 작동한다. 다만 에러가 났을때만 알려주는게 단점
# 
# 데이터 베이스 관련용어
# 데이터베이스를 구축하려면 데이터베이스 모델링 작업이 필요하다.
# 이는 현실 세계의 사용되는 데이터를 DBMS 에 어떻게 옮겨 놓을지 결정하는 과정이다.
# 데이터베이스에서는 정보를 테이블(Table)라는 표 형태의 틀에 맞추어 저장해야한다.
# DBMS 안에 여러개의 데이터베이스가 존재, 그리고 그 안에 테이블이 존재

# 행(로우, 레코드) : 실질적인 데이터(john, 1990)
# 열(컬럼, 속성) : 각 테이블은 1개 이상의 열로 구성된다.(아이디, 회원이름, 이메일)
# 데이터 : john, 1980 등 하나하나의 단편적인 정보를 의미한다.
# 테이블 : 회원 데이터가 표 형태로 표현된 것
# 데이터 형식 : 열의 데이터 형식으로 테이블을 생성할 때 열 이름과 함께 지정해야한다.
# 회원 테이블의 회원이름 열은 당연히 숫자 형식이 아닌 문자 형식이어야 한다,
# 데이터베이스(DB) : 테이블이 저장되는 저장소, 주로 원통 모양으로 표현
# DBMS(DataBase Management System) : 데이터베이스를 관리하는 시스템 또는 소프트웨어(SQLite)

# 자주 사용하는 sqlite 명령어
# .table : 현재 데이터베이스의 테이블 목록을 보여준다
# .schema 테이블 이름 : 테이블의 열 및 데이터 형식등 정보를 보여준다
# .header on : SELECT 문으로 출력할 때 헤더를 보여준다
# .mode column : SELECT 문으로 출력할 떄 컬럼 모드로 출력한다.
# .quit : SQLite 를 종료한다.
# CREATE TABLE : 테이블 이름(열이름1 데이터형식, 열이름2 데이터형식)
# DROP TABLE : 생성된 테이블을 삭제한다.
# INSERT INTO 테이블이름 VALUES(값1,값2)
# 행 데이터를 삭제 : "DELETE FROM 테이블이름 WHERE 열이름=값;" 을 사용한다.
# 행 데이터값 수정 : "UPDATE 테이블이름 SET 열이름=새값 WHERE 열이름=값;" 을 사용한다.
# SELECT FROM 테이블이름 : 데이터 조회
# ORDER BY : 오름차순 정렬할 때 사용한다.
# DESC : 내림차순 정렬할 때 사용한다.