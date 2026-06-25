class Beverage:
    def __init__(self, bev_no, name, price):
        self.__bev_no = bev_no
        self.__name = name
        self.__price = price

    def get_no(self):
        return self.__bev_no
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    
    def set_no(self, new_bev_no):
        self.__bev_no = new_bev_no
    def set_price(self, new_price):
        self.__price = new_price

    def __str__(self):
        return f'{self.__bev_no}\t{self.__name}\t{self.__price}'