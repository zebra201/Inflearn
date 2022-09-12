# 하나의 파일을 읽어서 그 안의 알파벳을 카운팅하는 프로그램 만들기

# 알파벳은 26자 이므로 26개의 리스트 만들기
counter = [0] * 26
infile = open("ex10(mobydick).txt")
ch = infile.read(1)
while ch != "":
    ch = ch.upper()     # 대문자로 바꾼다.
    # 알파벳이라면
    if ch >= "A" and ch <= "Z":
        # ord()는 유니코드를 반환,
        # A를 빼면 현재 알파벳의 문자번호를 알 수 있다.
        i = ord(ch) - ord("A")
        counter[i] += 1
    ch = infile.read(1)
print(counter)