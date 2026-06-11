class CartService:
    CART_NUMBER_SEQ = 1

    def __init__(self, cart_dao):
        self.__dao = cart_dao

    def add_cart(self, cart):
        cart.set_cart_number(CartService.CART_NUMBER_SEQ)
        if self.__dao.add_cart(cart):
            CartService.CART_NUMBER_SEQ += 1
            return True
        return False
    
    def delete_cart(self, book_number, user_number):
        if self.__dao.delete_cart(book_number, user_number):
            return True
        return False
    
    def empty_cart(self, user_number):
        if self.__dao.empty_cart(user_number):
            return True
        return False
    
    def view_cart(self, user_number):
        return self.__dao.view_cart(user_number)