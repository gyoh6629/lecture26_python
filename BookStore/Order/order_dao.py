import joblib

class OrderDAO:
    ORDER_DB_FILE = './DB/orderDB.joblib' # 사용자 DB 파일
    def __init__(self):
        self.__orderDB = self.__load_orderDB()
#-----------------------------------------------------------------------
    def __load_orderDB(self): # 파일내용 가져오기
        try:
            return joblib.load(OrderDAO.USER_DB_FILE)
        except FileNotFoundError:
            return {}
    def save_orderDB(self): # 파일에 저장하기
        if self.__orderDB:
            joblib.dump(self.__orderDB, OrderDAO.USER_DB_FILE)
#-----------------------------------------------------------------------
    def create_order(self, order): # 주문 생성
        self.__orderDB[order.order_number()] = order
        return True

    def list_order(self): # 주문 목록
        return list(self.__orderDB.values())
    
    def list_order_by_user(self, user_number): # 사용자 별 주문 목록
        result = []
        for order in self.__orderDB.values():
            if order.get_user_number() == user_number:
                result.append(order)
        return result