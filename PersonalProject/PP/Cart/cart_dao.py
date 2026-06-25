class CartDAO:
    def __init__(self):
        self.__cartDB = {}

    def list_cart(self):
        return list(self.__cartDB.values())
    
    def add_cart(self, cart):
        self.__cartDB[cart.get_no()] = cart

    def del_cart(self, cart_no):
        self.__cartDB.pop(cart_no)

    def clear_cart(self):
        self.__cartDB.clear()