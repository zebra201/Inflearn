# 중복(nested) if ~ else 문 (중요, 자주 사용함)
# 사용자로부터 아이디를 입력받아서 등록되어진 아이디인지를 검사하는 프로그램을
# 작성하는데, 등록된 아이디를 '리스트(list)'에 저장하도록 한다.
# 아이디가 등록되어 있다면 패스워드를 물어보도록 하자.
# 단, 패스워드는 "1234"라고 가정하도록 한다.

id = str(input("ID를 입력하세요 : "))
id_all = ['zebra1', 'zebra2', 'zebra3', 'zebra4', 'zebra5']
if id in id_all:        # 사용자가 입력한 id 가 id_all에 있는지 확인하는 코드
    password = int(input("비밀번호를 입력하세요 : "))
    if password == 1234:
        print(id + "님 로그인 성공")
    else:
        print("비밀번호가 틀립니다.")
else:
    print("등록된 ID가 존재하지 않습니다.")