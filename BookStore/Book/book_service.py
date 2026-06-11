class BookService:
    BOOK_NUMBER_SEQ = 1001 # 자동 도서번호

    def __init__(self, book_dao): # 도서 DB와 연결
        self.__dao = book_dao

    def add_book(self, book): # 도서번호 만들어서 전달하기 ( 도서 추가 )
        book.set_book_number(BookService.BOOK_NUMBER_SEQ)
        if self.__dao.add_book(book):
            BookService.BOOK_NUMBER_SEQ += 1
            return True
        return False

    def delete_book(self, book_number): # 삭제할 도서번호 전달하기( 도서 삭제 )
        if self.__dao.delete_book(book_number):
            return True
        return False
    
    def view_book_list(self): # 도서목록 전달하기 ( 도서 목록 )
        return self.__dao.list_book()
    
    def view_book_info(self, book_number): # 도서정보 전달하기 ( 도서 상세정보 조회 )
        return self.__dao.info_book(book_number)
    
    def search_book(self, book_name): # 검색한 도서 결과 전달하기 ( 도서 검색 )
        return self.__dao.search_book(book_name)
    
    def modify_stock(self, book_number, new_stock): # 도서번호와 새 재고 전달하기 ( 재고 수정 )
        return self.__dao.mod_book(book_number, new_stock)