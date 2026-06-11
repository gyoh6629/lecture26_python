from user import User
#-----------------------------------------------------------------------
class UserService:
    USER_NUMBER_SEQ = 1000      # 자동 생성 사용자 번호
    ADMIN_ID = 'admin'          # 관리자 아이디
    ADMIN_PASSWORD = 'password' # 관리자 비밀번호
#-----------------------------------------------------------------------
    def __init__(self, user_dao): # 사용자 DB와 연결
        self.__dao = user_dao
        self.current_user = None  # 현재 로그인 유저 아이디
        self.join(User(None, UserService.ADMIN_ID, UserService.ADMIN_PASSWORD, None)) # 실행하면 관리자 계정 자동 생성
#-----------------------------------------------------------------------
    def login(self, id, password): # 로그인 ( 사용자 )
        user = self.__dao.info_user(id)
        if user:
            if user.get_password() == password:
                self.current_user = id
                return True
        return False
    
    def logout(self): # 로그아웃
        self.current_user = None
        self.__dao.save_userDB()
        return True
    
    def join(self, user): # 회원가입
        user.set_user_number(UserService.USER_NUMBER_SEQ)
        if self.__dao.add_user(user):
            UserService.USER_NUMBER_SEQ += 1
            return True
        return False
    
    def view_list_user(self): # 회원 목록 보기 ( 관리자 )
        if self.current_user == UserService.ADMIN_ID:
            return self.__dao.list_user()
        return None
    
    def match_password(self, password): # 비밀번호가 현재 계정과 일치하는지 확인 ( 함수 )
        if self.__dao.info_user(self.current_user).get_password() == password:
            return True
        return False
    
    def view_user_info(self, password): # 회원 정보 보기 ( 사용자 )
        if self.match_password(password):
            id = self.__dao.id_by_password(password)
            return self.__dao.info_user(id)
        return None
    
    def withdrawal_by_user(self, password): # 회원 탈퇴 ( 사용자 )
        if self.match_password(password):
            if self.__dao.delete_user(self.current_user):
                self.current_user = None
                return True
        return False
    
    def withdrawal_by_admin(self, id, password): # 회원 퇴출 ( 관리자 )
        if self.match_password(password):
            self.__dao.del_user(id)
            return True
        return False

    def modify_id(self, new_id, password): # 아이디 수정 ( 사용자 )
        if self.match_password(password):
            if self.__dao.modify_id(new_id, password):
                self.current_user = new_id
                return True
        return False
    
    def modify_password(self, new_password, password): # 비밀번호 수정 ( 사용자 )
        if self.match_password(password):
            if self.__dao.modify_password(new_password, password):
                return True
        return False
    
    def modify_address(self, new_address, password): # 주소 수정 ( 사용자 )
        if self.match_password(password):
            if self.__dao.modify_password(new_address, password):
                return True
        return False

    def view_user_number(self):
        return self.__dao.user_number_by_id(self.current_user)