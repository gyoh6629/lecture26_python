from member import MemberService

def select_menu():
    print('===============================================================================')
    print('1.회원가입 | 2.회원목록 | 3.회원상세정보 | 4.회원정보수정 | 5.회원탈퇴 | 0.종료')
    print('===============================================================================')
    menu = int(input('선택> '))
    return menu
def input_member(question):
    while True:
        answer = input(question).strip()
        if not answer:
            print('잘못된 값입니다. 다시 입력해주세요.')
        else:
            return answer

ms = MemberService()
while True:
    select = select_menu()
    if select == 1:
        print('============')
        print('회원가입')
        print('============')
        num = input_member('회원번호 입력 : ')
        id = input_member('아이디 입력 : ')
        pw = input_member('비밀번호 입력 : ')
        name = input_member('이름 입력 : ')
        phone = input_member('전화번호 입력 : ')
        add = input_member('주소 입력 : ')
        if ms.join_member(num, id, pw, name, phone, add):
            print('결과 : 회원가입이 완료되었습니다.')
    elif select == 2:
        print('============')
        print('회원목록')
        print('============')
        member_list = ms.list_member()
        if not member_list:
            print('현재 회원이 없습니다.')
        else:
            print(f'회원번호\t아이디\t\t비밀번호\t이름\t\t전화번호\t주소')
            for ml in member_list:
                print("-------------------------------------------------------------------------------------")
                print(ml)
            
    elif select == 3:
        print('================')
        print('회원상세정보')
        print('================')
        num = input('회원번호 입력 : ')
        details = ms.list_member_details(num)
        if not details:
            print('존재하지 않는 회원번호입니다.')
        else:
            print(details)
    elif select == 4:
        print('================')
        print('회원정보수정')
        print('================')
        num = input_member('회원번호 입력 : ')
        id = input_member('아이디 입력 : ')
        pw = input_member('비밀번호 입력 : ')
        name = input_member('이름 입력 : ')
        phone = input_member('전화번호 입력 : ')
        add = input_member('주소 입력 : ')
        if ms.modify_member(num, id, pw, name, phone, add):
            print('결과 : 수정이 완료되었습니다.')
    elif select == 5:
        print('============')
        print('회원탈퇴')
        print('============')
        num = input('회원번호 입력 : ')
        if ms.leave_member(num):
            print('결과 : 탈퇴가 완료되었습니다.')
        else:
            print('존재하지 않는 회원번호입니다.')
    elif select == 0:
        break
    else:
        print('메뉴에 있는 번호를 선택해주세요.')