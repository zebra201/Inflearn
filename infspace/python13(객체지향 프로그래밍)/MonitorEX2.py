from MonitorEX1 import *

if __name__ == "__main__":
    # company, inch, price, color
    # "삼성", 30, 150000, "검정"
    monitor2 = Monitor2("삼성", 30, 150000, "검정")
    monitor2.__str__()
    print("-" * 50)
    
    monitor2.setCompany("LG")
    monitor2.setInch(20)
    monitor2.setPrice(300000)
    monitor2.setColor("빨강")
    monitor2.__str__()