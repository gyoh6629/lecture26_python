class User:
    def __init__(self, user_number, id, password, address):
        self.__user_number = user_number # 사용자 번호
        self.__id = id                   # 아이디
        self.__password = password       # 비밀번호
        self.__address = address         # 주소
#-----------------------------------------------------------------------
    def get_user_number(self):
        return self.__user_number
    def get_id(self):
        return self.__id
    def get_password(self):
        return self.__password
    def get_address(self):
        return self.__address
#-----------------------------------------------------------------------
    def set_user_number(self, seq_number):
        self.__user_number = seq_number
    def set_id(self, new_id):
        self.__id = new_id
    def set_password(self, new_password):
        self.__password = new_password
    def set_address(self, new_address):
        self.__address = new_address
#-----------------------------------------------------------------------
    def __str__(self):
        return f'{self.__user_number}\t{self.__id}\t{self.__address}'