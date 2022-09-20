# 이론
# 프로그램은 완벽하지 않으므로 사용자들은 잘못된 데이터를 입력할 수도 있다.
# 따라서 오류가 발생하면 오류 보고 시스템의 소스 파일을 확인해야 한다.
# 오류의 역추적(traceback) 메시지를 확인해야 한다.
# 프로그램에 오류가 발생하여 사용자의 데이터를 잃어버렸다면 좋지 않지만,
# 오류 발생시 보고하고, 저장한 뒤 계속 실행할 수 있다면 더 좋을 것이다.
# 오류의 종류
# 사용자 입력 오류 : 사용자가 다른 범위의 입력 오류
# 장치 오류 : 네트워크, 하드 디스크 작동 실패 등
# 코드 오류 : 잘못된 인덱스를 사용하여 배열 접근 시
# 잘 알려진 오류
# IOError : 파일을 열 수 없으면 발생
# importError : 파이썬이 모듈을 찾을 수 없으면 발생
# ValueError : 연산이나 내장 함수에서 인수가 적절치 않은 값을 가지고 있으면 발생
# 오류를 처리하는 전통적인 방법은 메소드가 오류 코드를 반환하는 것이지만, 항상 가능한 것은 아님
# 파이썬에서는 try-except 블록을 사용하여 오류 처리 가능.
# --------------------------------------------------------------

# 실습
# 예외처리의 목적은 프로그램의 정상적인 종료로 만들어 주는 것이다.
(x,y) = (2,0)
try :
    z = x/y
    print("try")
except ZeroDivisionError:
    print("모든 수는 0으로 나눌 수 없습니다")