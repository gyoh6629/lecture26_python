import datetime

class Order:
    def __init__(self, order_number, book_name, author, price, user_number):
        self.__order_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 주문 날짜
        self.__order_number = order_number # 주문 번호
        self.__book_name = book_name       # 도서 제목                                         
        self.__author = author             # 저자
        self.__price = price               # 가격
        self.__user_number = user_number   # 사용자 번호
#-----------------------------------------------------------------------
    def get_user_number(self):
        return self.__user_number
#-----------------------------------------------------------------------
    def set_order_number(self, seq_number):
        self.__order_number = seq_number
#-----------------------------------------------------------------------
    def __str__(self):
        return f'{self.__order_date}\t{self.__order_number}\t{self.__book_name}\t{self.__author}\t{self.__price}'