class Book:
    def __init__(self, book_number, book_name, author, publisher, price, stock):
        self.__book_number = book_number # 도서번호
        self.__book_name = book_name     # 제목
        self.__author = author           # 저자
        self.__publisher = publisher     # 출판사
        self.__price = price             # 가격
        self.__stock = stock             # 재고
#-----------------------------------------------------------------------
    def get_book_number(self): 
        return self.__book_number
    def get_book_name(self):
        return self.__book_name
    def get_author(self):
        return self.__author
    def get_publisher(self):
        return self.__publisher
    def get_price(self):
        return self.__price
    def get_stock(self):
        return self.__stock
#-----------------------------------------------------------------------
    def set_book_number(self, seq_number):
        self.__book_number = seq_number
    def set_stock(self, stock):
        self.__stock = stock
#-----------------------------------------------------------------------
    def __str__(self):
        return f'{self.__book_number}\t{self.__book_name}\t{self.__author}\t{self.__price}'