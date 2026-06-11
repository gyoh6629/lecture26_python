import joblib

class BookDAO:
    BOOK_DB_FILE = './DB/bookDB.joblib' # 도서 DB 파일
    def __init__(self):
        self.__bookDB = self.__load_bookDB()
#-----------------------------------------------------------------------
    def __load_bookDB(self): # 파일내용 가져오기
        try:
            return joblib.load(BookDAO.BOOK_DB_FILE)
        except FileNotFoundError:
            return {}
    def save_bookDB(self): # 파일에 저장하기
        if self.__bookDB:
            joblib.dump(self.__bookDB, BookDAO.BOOK_DB_FILE)
#-----------------------------------------------------------------------
    def is_exist(self, book): # 같은 도서가 DB에 존재하는지 확인 ( 함수 )
        for existent_book in self.__bookDB.keys():
            if existent_book.get_book_name() == book.get_book_name() and existent_book.get_author() == book.get_author():
                return True
        return False
    
    def add_book(self, book): # DB에 도서 추가하기 ( 도서 추가 )
        if self.is_exist(book):
            return False
        self.__bookDB[book.get_book_number()] = book
        return True
        
    def delete_book(self, book_number): # DB에서 도서 삭제하기 ( 도서 삭제 )
        book = self.info_book(book_number)
        if self.is_exist(book):
            self.__bookDB.pop(book.get_book_number())
            return True
        return False
        
    def list_book(self): # DB의 모든 도서 정보 리스트로 반환하기 ( 도서 목록 ) ( 함수 )
        if self.__bookDB:
            return list(self.__bookDB.values())
        return None
        
    def info_book(self, book_number): # DB에서 도서번호와 일치하는 도서 정보 반환 ( 도서 별 상세 정보 ) ( 함수 )
        book = self.__bookDB[book_number]
        if book:
            return book
        return None
    
    def search_book(self, book_name): # DB에서 제목에 일치하는 도서 정보 반환 ( 도서 검색 )
        if self.__bookDB:
            result = []
            book_list = self.list_book()
            if book_list:
                for book in book_list:
                    if book.get_book_name() == book_name:
                        result.append(book)
                return result
        return None
    
    def modify_book_stock(self, book_number, new_stock): # DB에서 도서번호와 일치하는 도서의 재고 수정 ( 재고 수정 )
        book = self.info_book(book_number)
        if self.is_exist(book):
            book.set_stock(new_stock)
            return True
        return False