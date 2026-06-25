class Order:
    def __init__(self, order_no, total_price):
        self.__order_no = order_no
        self.__total_price = total_price

    def get_no(self):
        return self.__order_no
    def get_total_price(self):
        return self.__total_price
    
    def set_no(self, new_order_no):
        self.__order_no = new_order_no

    def __str__(self):
        return f'{self.__order_no}\t{self.__total_price}'