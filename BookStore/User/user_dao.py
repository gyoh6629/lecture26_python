import joblib

class UserDAO:
    USER_DB_FILE = './DB/userDB.joblib' # 사용자 DB 파일
    def __init__(self):
        self.__userDB = self.__load_userDB()
#-----------------------------------------------------------------------
    def __load_userDB(self): # 파일내용 가져오기
        try:
            return joblib.load(UserDAO.USER_DB_FILE)
        except FileNotFoundError:
            return {}
    def save_userDB(self): # 파일에 저장하기
        if self.__userDB:
            joblib.dump(self.__userDB, UserDAO.USER_DB_FILE)
#-----------------------------------------------------------------------
    def is_exist(self, id): # 같은 아이디가 DB에 존재하는지 확인 ( 함수 )
        if len(self.__userDB) > 1:
            for existent_id in self.__userDB.values():
                if existent_id.get_id() == id:
                    return True
        return False
    
    def user_number_by_id(self, id): # 아이디와 일치하는 사용자 번호 반환 ( 함수 )
        if len(self.__userDB) > 1:
            for user in self.__userDB.values():
                if user.get_id() == id:
                    return user.get_user_number()
        return None

    def user_number_by_password(self, password): # 비밀번호와 일치하는 사용자 번호 반환 ( 함수 )
        if len(self.__userDB) > 1:
            for user in self.__userDB.values():
                if user.get_password() == password:
                    return user.get_user_number()
        return None

    def info_user(self, id): # 아이디와 일치하는 사용자 정보 반환 ( 사용자 정보 ) ( 함수 )
            if self.is_exist(id):
                user_number = self.user_number_by_id(id)
                if user_number:
                    return self.__userDB[user_number]
            return None
    
    def add_user(self, user): # DB에 사용자 추가하기 ( 회원 가입 )
        if self.is_exist(user.get_id()):
            return False
        self.__userDB[user.get_user_number()] = user
        return True
        
    def list_user(self): # DB의 모든 사용자 정보 리스트로 반환하기 ( 사용자 목록 ) ( 함수 )
        if len(self.__userDB) > 1:
            return list(self.__userDB.values())
        return None

    def delete_user(self, id): # 아이디와 일치하는 사용자 정보 삭제하기 ( 회원 탈퇴, 강퇴 )
        if self.is_exist(id):
            user_number = self.user_number_by_id(id)
            self.__userDB.pop(user_number)
            return True
        return False
        
    # def modify_user(self, id, user): # 아아디와 일치하는 사용자 정보 수정 ( 사용자 수정 )
    #     if self.is_exist(id):
    #         user_number = self.user_number_by_id(id)
    #         self.__userDB[user_number] = user
    #         return True
    #     return False
    
    def modify_id(self, new_id, password): # 비밀번호에 해당하는 사용자 아이디 변경 ( 아이디 수정 )
        user_number = self.user_number_by_password(password)
        if user_number:
            self.info_user(user_number).set_id(new_id)
            return True
        return False
    
    def modify_password(self, new_password, password): # 비밀번호에 해당하는 사용자 비밀번호 변경 ( 비밀번호 수정 )
        user_number = self.user_number_by_password(password)
        if user_number:
            self.info_user(user_number).set_password(new_password)
            return True
        return False
    
    def modify_address(self, new_address, password): # 비밀번호에 해당하는 사용자 주소 변경 ( 주소 수정 )
        user_number = self.user_number_by_password(password)
        if user_number:
            self.info_user(user_number).set_address(new_address)
            return True
        return False