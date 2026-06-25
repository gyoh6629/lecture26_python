class Cart:
    def __init__(self, cart_no, name, price):
        self.__cart_no = cart_no
        self.__name = name
        self.__price = price

    def get_no(self):
        return self.__cart_no
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    
    def set_no(self, new_cart_no):
        self.__cart_no = new_cart_no

    def __str__(self):
        return f'{self.__cart_no}\t{self.__name}\t{self.__price}'