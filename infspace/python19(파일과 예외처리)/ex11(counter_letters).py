# 사용자로부터 파일 안에 문자들의 개수를 세는 프로그램
filename = input("파일 이름을 입력하세요 : ").strip()
infile = open(filename, "r", encoding="UTF-8")

freqs = {}

for line in infile:
    for char in line.strip():       # 문자들의 양쪽 공백 제거
        if char in freqs:
            freqs[char] += 1        # 문자 하나를 누적
        else:
            freqs[char] = 1         # 제일 처음 나왔을 때
            
print(freqs)  
        
infile.close()