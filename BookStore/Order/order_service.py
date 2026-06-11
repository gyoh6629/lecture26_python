class OrderService:
    ORDER_NUMBER_SEQ = 1001
#-----------------------------------------------------------------------
    def __init__(self, order_dao):
        self.__dao = order_dao
#-----------------------------------------------------------------------
    def create_order(self, order): # 주문 생성
        order.set_order_number(OrderService.ORDER_NUMBER_SEQ)
        if self.__dao.create_order(order):
            OrderService.ORDER_NUMBER_SEQ += 1

    def list_order(self): # 주문 목록
        return self.__dao.list_order()
    
    def list_order_by_user(self, user_number): # 사용자 별 주문 목록
        return self.__dao.list_order_by_user(user_number)