# 문제
# 피보나지 이터레이터 만들기
# 피보나치
# 1 1 2 3 5 8 13 21 34

# 풀이
class FibIterator(object):
    def __init__(self, a=1, b=0, maxValue=50):
        self.a = a
        self.b = b
        self.maxValue = maxValue
    
    def __iter__(self):
        return self
    
    def __next__(self):
        n = self.a + self.b
        if n > self.maxValue:
            raise StopIteration
        self.a = self.b
        # print("self.a : ", self.a, "self.b : ", self.b)
        self.b = n
        # print("self.a : ", self.a, "n : ", n)
        return n
    
if __name__ == "__main__":
    for n in FibIterator():
        print(n, end=" ")
        