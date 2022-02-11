# 사용자로부터 10진수를 입력받아서 문자 2진수 문자열로 변환하여
# 반환하는 decTobin(num)를 작성하고 테스트 해보시오

def decTobin(num):
    binary = "" #초기화
    
    while num != 0:     # num이 0이 아닐때까지 루프
        value = num % 2
        if value == 0:
            binary = "0" + binary
        else:
            binary = "1" + binary
        num = num // 2
        print("num : ", num)
    return binary
        
decNum = int(input("10진수를 입력하세요 : "))
print("10진수 ", decNum, "을 2진수로 변경한 값", decTobin(decNum))

