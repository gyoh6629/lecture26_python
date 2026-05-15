class Member:
    def __init__(self, num, id, pw, name, phone, add):
        self.__num = num
        self.__id = id
        self.__pw = pw
        self.__name = name
        self.__phone = phone
        self.__add = add
    def __str__(self):
        return f'{self.__num}\t\t{self.__id}\t\t{self.__pw}\t\t{self.__name}\t\t{self.__phone}\t\t{self.__add}'
    
    def modify(self, num, id, pw, name, phone, add):
        if num != None:
            self.__num = num
        if id != None:
            self.__id = id
        if pw != None:
            self.__pw = pw
        if name != None:
            self.__name = name
        if phone != None:
            self.__phone = phone
        if add != None:
            self.__add = add
    def get_num(self):
        return self.__num
    def get_id(self):
        return self.__id
    def get_pw(self):
        return self.__pw
    def get_name(self):
        return self.__name
    def get_phone(self):
        return self.__phone
    def get_add(self):
        return self.__add
    
class MemberService:
    def __init__(self):
        self.__member_list = []
        self.__basic_list = []

    def join_member(self, num, id, pw, name, phone, add):
        new_member = Member(num, id, pw, name, phone, add)
        basic_information = Member(num, id, None, None, None, None)
        self.__member_list.append(new_member)
        self.__basic_list.append(basic_information)
        return True
    def list_member(self):
        return self.__basic_list
    def list_member_details(self, num):
        for find_member in self.__member_list:
            if find_member.get_num() == num:
                return find_member
        else:
            return False
    def modify_member(self, num, id, pw, name, phone, add):
        for find_member in self.__member_list:
            if find_member.get_num() == num:
                find_member.modify(num, id, pw, name, phone, add)
        for find_member in self.__basic_list:
            if find_member.get_num() == num:
                find_member.modify(num, id, None, None, None, None)
        return True
    def leave_member(self, num):
        if not any(remain_member.get_num() == num for remain_member in self.__member_list):
            return False
        self.__member_list = [remain_member for remain_member in self.__member_list if remain_member.get_num() != num]
        self.__basic_list = [remain_member for remain_member in self.__basic_list if remain_member.get_num() != num]
        return True
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