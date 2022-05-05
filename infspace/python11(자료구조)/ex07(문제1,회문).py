# 회문이란 것은 앞으로 읽으나 뒤로 읽으나 동일한 문장을 의미한다.
# 예를 들면 "mom", "civic", "dad" 등 읽을 때 앞뒤가 같은 것을 말한다.
# 상뇽자로부터 문자열을 입력받고 회문인지 아닌지 검사하는 프로그램을 작성해보자
# 출력결과
# 문자열을 입력하시오 : dad
# 회문입니다.
# -------------------------------------------------------------------


# if __name__ == "__main__":
#     data_set = ()
#     data = input("문자열을 입력하시오 : ")
#     datawords = data.split()
#     for x in datawords:
#         data_set += x

def main():
    string = input("문자열을 입력하세요 : ")
    string = string.replace(" ","")
    
    if check(string) == True:
        print(string + "은 회문입니다.")
    else:
        print(string + "은 회문이 아닙니다.")


# 회문 여부 True, False
def check(s):
    # 단어의 처음 인덱스와 마지막 인덱스를 저장하는 코드
    low = 0   
    high = len(s) - 1
    
    while True:
        # 회문이라면 아래 조건문에 해당하여 종료 (순서가 역전)
        if low > high :
            return True
        
        s1 = s[low]
        s2 = s[high]
        print(s1, s2)
        
        # 값이 틀려 회문이 아닐때
        if s1 != s2:
            return False
        
        # 인덱스를 증가시켜서 서로 비교항목을 바꾸도록 한다.
        low += 1
        high -= 1
    

if __name__ == "__main__":
    main()