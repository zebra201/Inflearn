from TV import TV
    

if __name__ == "__main__" :
    # 인스턴스 생성
    tv1 = TV()
    tv2 = TV()
    tv3 = TV()
    # 인스턴스의 필드와 메소드를 tv1 인스턴스명(참조변수) 조작
    tv1.color = "검정색"
    tv1.powerTV(True, "tv1")
    tv1.channelUp(9, "tv1")
    tv1.volumeUp(25, "tv1")
    tv1.printTV("tv1")
    tv1.channelUp(-100, "tv1")
    tv1.powerTV(False, "tv1")
    tv1.volumeUp(30, "tv1")
    print("-" * 50)
    
    tv2.color = "흰색"
    tv2.powerTV(True, "tv2")
    tv2.channelUp(17, "tv2")
    tv2.volumeUp(50, "tv2")
    tv2.printTV("tv2")
    tv2.channelUp(-100, "tv2")
    tv2.powerTV(False, "tv2")
    tv2.volumeUp(20, "tv2")