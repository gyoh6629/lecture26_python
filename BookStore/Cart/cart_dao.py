import joblib

class CartDAO:
    CART_DB_FILE = './DB/cartDB.joblib'

    def __init__(self):
        self.__cartDB = self.__load_cartDB()
#-----------------------------------------------------------------------
    def __load_cartDB(self):
        try:
            return joblib.load(CartDAO.CART_DB_FILE)
        except FileNotFoundError:
            return {}
    def save_cartDB(self):
        if self.__cartDB:
            return joblib.dump(self.__cartDB, CartDAO.CART_DB_FILE)
#-----------------------------------------------------------------------
    def view_cart(self, user_number):
        result = []
        for cart in self.__cartDB.values():
            if cart.get_user_number() == user_number:
                result.append(cart)
        return result

    def add_cart(self, cart):
        self.__cartDB[cart.get_cart_number()] = cart
        return True
    
    def delete_cart(self, book_number, user_number):
        for cart in self.__cartDB.values():
            if cart.get_book_number() == book_number and cart.get_user_number() == user_number:
                self.__cartDB.pop(cart.get_cart_number())
        return True

    def empty_cart(self, user_number):
        for cart in self.__cartDB.values():
            if cart.get_user_number() == user_number:
                self.__cartDB.pop(cart.get_cart_number())
        return True