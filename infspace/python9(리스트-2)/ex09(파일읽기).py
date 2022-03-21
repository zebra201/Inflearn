# strip() : 양쪽의 공백을 모두 삭제하는 함수
# 정렬하기(sorted 내장 함수는 복사본을 반환함, sort는 없음)
# a = [3,2,1,5,4]
# a.sort(reverse=True)
# print(a)

# 선택정렬 : 정렬되지 않은 리스트에서 값을 선택하여, 다른 리스트로 순서대로 넣음
# 선택정렬, 버블정렬, 삽입정렬, 병합정렬, 퀵정렬, 힙정렬 등이 있으며, 시간복합도에 따라 효율이 다르다.
# 선택정렬은 데이터의 양이 적을때 매우 효율적, 대용량 작업에는 좋지 않음.
# 버블정렬은 상호 인근 값을 검사하여 정렬, 안정성이 높으나 시간이 오래걸림
# 삽입정렬은 자료 배열에서 모든 요소를 차례대로 비교함. 속도가 빠르다. 역순시 느림.
# 퀵정렬은 매우 빠르지만, 다른 알고리즘보다 까다로움
# 제자리 정렬은 입력 리스트 외에 추가적인 공간을 사용하지 않는 선택 정렬 알고리즘이다.

# 기본적인 파일 입출력 실습
data = []
# 파일의 경로를 지정하고 읽기 모드로 문자셋 UTF-8로 설정하여
# 해당 파일을 열고 메모리에 로딩된 파일의 주소를 반환한다.
filepoint = open("C:\\ETC\\test.txt", mode="r", encoding="UTF-8")
# print(type(filepoint))
# readlines() 메서드는 파일의 저장된 내용을 한번에 다 읽는다.
for line in filepoint.readlines():
    data.append(line.strip())
    # strip() 메서드는 원래 양쪽 문자열의 양쪽 공백을 제거하는 역할을 하지만,
    # 파일을 읽어들일때는 엔터키 제거를 해준다.

# 프로그램에서 리소스를 다 사용했으면 반드시 close () 메서드를 호출하도록 한다.
print("파일에서 읽은 내용입니다.")
print(data)
filepoint.close()

# 파일에다가 내용 쓰는 방법
# 파일의 모드가 w 인 경우에는 기존 파일의 내용을 덮어써버린다.(기존 내용 삭제)
filepoint = open("C:\\ETC\\test.txt", mode="w", encoding="UTF-8")
filepoint.write("우리는 파이썬을 공부합니다.")
filepoint.write("저희도 파이썬을 공부합니다.")
print("쓰기 완료")
filepoint.close()


# 파일에다가 내용 쓰는 방법
# 파일의 모드가 a인 경우에는 기존 파일의 내용에 추가를 한다.
filepoint = open("C:\\ETC\\test.txt", mode="a", encoding="UTF-8")
filepoint.write("11.우리는 파이썬을 공부합니다.")
filepoint.write("22.저희도 파이썬을 공부합니다.")
print("추가 완료")
filepoint.close()


# csv 파일 읽는 방법
import csv
filepoint = open("C:\\ETC\\sample1.csv", mode="r", encoding="UTF-8")
reader2 = csv.reader(filepoint)
for i in reader2:
    print(i)
filepoint.close()




data=[]
filepoint = open("c:\\ETC\\test.txt", mode = "r", encoding="UTF-8")


# 연습
# for i in filepoint.readlines:
#     data.append(line.strip())
# print(data)
# filepoint.close()


# import csv
# filepoint1 = open("C:\\ETC\\test.txt",mode="r",encoding="UTF-8")
# a = csv.reader(filepoint1)
# for i in a:
#     print(i)
# filepoint1.close