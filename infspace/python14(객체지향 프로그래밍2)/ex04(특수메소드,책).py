# 특수 메소드를 이용하여 len() 함수를 다른 메소드로 새롭게 정의해보는 예제

# 실습
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return "제목 : %s / 저자 : %s / 페이지수 : %d" % \
            (self.title, self.author, self.pages)
            
    # len() 함수를 페이지수를 리턴하게끔 만듦
    def len(self):
        return self.pages
    
if __name__ == "__main__":
    book = Book("파이썬","코딩형",874)
    print(book)
    print("책의 페이지 수 : ", book.len())