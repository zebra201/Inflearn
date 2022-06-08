class Monitor2:
    # 필드 선언
    __company = ""
    __inch = 0
    __price = 0
    __color = ""

    def __init__(self, company, inch, price, color):
        self.__company = company
        self.__inch = inch
        self.__price = price
        self.__color = color
        print("매개변수가 있는 생성자 호출")
    
    def getCompany(self):
        return self.__company
    def getInch(self):
        return self.__inch
    def getPrice(self):
        return self.__price
    def getColor(self):
        return self.__color
    
    def setCompany(self, company):
        self.__company = company
    def setInch(self, inch):
        self.__inch = inch
    def setPrice(self, price):
        self.__price = price
    def setColor(self, color):
        self.__color = color
        
    def __str__(self):
        print("제조사 : ", self.getCompany())
        print("인치 : ", self.getInch())
        print("가격 : ", self.getPrice())
        print("색상 : ", self.getColor())