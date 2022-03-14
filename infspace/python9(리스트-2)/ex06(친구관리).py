# 연락처 관리 프로그램 만들기
# 출력결과

# 1. 친구 리스트 출력
# 2. 친구추가
# 3. 친구삭제
# 4. 이름종료
# 9. 종료
# 메뉴를 선택하시오 : 2
# 이름을 입력하세요 : 홍길동
# -----------------------
# 1. 친구리스트 출력
# 2. 친구추가
# 3. 친구삭제
# 4. 이름변경
# 9. 종료
# 메뉴를 선택하시오 : 1
# ['홍길동']

# friend_list =[]
# answer = 0
# flags = True
# while flags :
#     answer = int(input("원하는 번호를 선택하세요. : "))
#     if answer == "1":
#         print(friend_list)
#     elif answer == "2":
#         name = input("이름을 입력하세요 : ")
#             friend_list[] = 
        
        
# 출력 문구를 나타내는 함수        
def menu_print():
    print("1. 친구리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("9. 종료")
    
# 메뉴를 저장할 함수가 필요
menu_choice = 0     # 메뉴 번호를 저장
friends = []        # 친구 목록을 저장할 리스트
phone = []

while True :
    menu_print()
    menu_choice = int(input("메뉴를 선택하시오 : "))
    print("--------------------------------------")
    
    # 무한 루프를 빠져나가는 코드
    if menu_choice == 9:
        print("프로그램을 종료합니다")
        break
    elif menu_choice == 1:
        print("친구 리스트 입니다.")
        print(friends)
    elif menu_choice == 2:
        name = input("이름을 입력하세요 : ")
        friends.append(name)
    elif menu_choice == 3:
        del_name = input("삭제하고 싶은 이름을 입력하세요 : ")
        if del_name in friends :    # 리스트에 삭제하고 싶은 이름이 있다면
            friends.remove(del_name)
            print(del_name, "님이 삭제되었습니다.")
        else:
            print(del_name, "님이 존재하지 않습니다.")
    elif menu_choice == 4:
        old_name = input("변경하고 싶은 이름을 입력하세요 : ")
        if old_name in friends :
            index1 = friends.index(old_name)
            new_name = input("새로운 이름을 입력하세요 : ")
            friends[index1] = new_name
        else:
            print(old_name, "님이 존재하지 않습니다.")

# 친구 추가시 연락처도 함께 추가하는 프로그램으로 업데이트 해보시기 바랍니다.