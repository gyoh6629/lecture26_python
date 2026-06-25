class CartService:
    cart_no_seq = 1

    def __init__(self, dao):
        self.__dao = dao

    def view_cart_list(self):
        return self.__dao.list_cart()

    def add_cart(self, cart):
        cart.set_no(CartService.cart_no_seq)
        CartService.cart_no_seq += 1
        self.__dao.add_cart(cart)

    def del_cart(self, cart_no):
        self.__dao.del_cart(cart_no)

    def clear_cart(self):
        self.__dao.clear_cart()