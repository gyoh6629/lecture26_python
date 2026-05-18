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