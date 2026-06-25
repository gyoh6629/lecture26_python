class BeverageDAO:
    def __init__(self):
        self.__bevDB = {}
    
    def list_bev(self):
        return list(self.__bevDB.values())
    
    def add_bev(self, bev):
        self.__bevDB[bev.get_no()] = bev

    def mod_bev(self, bev):
        self.__bevDB[bev.get_no()] = bev

    def del_bev(self, bev_no):
        self.__bevDB.pop(bev_no)