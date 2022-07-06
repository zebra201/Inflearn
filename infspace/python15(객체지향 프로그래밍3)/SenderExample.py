# ContentSender, KakaoSender, SmsSender 클래스의 실행파일

from KaKaoSender import * 
from SmsSender import *

if __name__ == "__main__":
    cs1 = KakaoSender("카카오톡", "이재훈", "100만원 송금")
    cs1.sendMsg("김사장")
    
    print("------------------------------------------")
    cs2 = SmsSender("SMS문자", "이현호", "고맙습니다")
    cs2.sendMsg("앞으로 잘 부탁드립니다")