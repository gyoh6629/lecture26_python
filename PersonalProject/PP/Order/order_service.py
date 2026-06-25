class OrderService:
    order_no_seq = 1

    def __init__(self, dao):
        self.__dao = dao

    def view_order_details(self):
        return self.__dao.list_order()

    def create_order(self, order):
        order.set_no(OrderService.order_no_seq)
        OrderService.order_no_seq += 1
        return self.__dao.create_order(order)