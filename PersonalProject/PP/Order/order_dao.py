class OrderDAO:
    def __init__(self):
        self.__orderDB = {}

    def list_order(self):
        return list(self.__orderDB.values())
    
    def create_order(self, order):
        self.__orderDB[order.get_no()] = order