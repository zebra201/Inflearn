# 클래스
class JSS:
    def __init__(self):
        self.name = input("이름 : ")
        self.age = input("나이 : ")
    def show(self):
        print("나의 이름은 {}입니다, 나이는 {}세입니다.".format(self.name, self.age))
        
a = JSS()
a.name
a.age
a.show()

# 상속 (원본을 그대로 두고, 필요한 내용을 추가)
class JSS2(JSS):
    def __init__(self):
        super().__init__()              # super는 JJS를 의미
        self.gender = input("성별 : ")  # 원하는 내용을 추가
    def show(self):
        print("나의 이름은 {}입니다, 성별은 {}자입니다, 나이는 {}세입니다.".format(self.name, self.gender, self.age))
        
# 똑같이 만들고 싶다면
# class JSS2(JSS):
#     pass

b = JSS2()
b.name
b.age
b.gender
b.show()