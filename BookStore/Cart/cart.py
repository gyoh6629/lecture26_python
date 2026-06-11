class Cart:
    def __init__(self, cart_number, book_number, book_name, author, price, user_number):
        self.__cart_number = cart_number
        self.__book_number = book_number
        self.__book_name = book_name
        self.__author = author
        self.__price = price
        self.__user_number = user_number
    
    def get_book_number(self):
        return self.__book_number
    def get_book_name(self):
        return self.__book_name
    def get_author(self):
        return self.__author
    def get_price(self):
        return self.__price
    def get_user_number(self):
        return self.__user_number
    
    def set_cart_number(self, seq_number):
        self.__cart_number = seq_number
    def set_user_number(self, user_number):
        self.__user_number = user_number

    def __str__(self):
        return f'{self.__book_number}\t{self.__book_name}\t{self.__author}\t{self.__price}'