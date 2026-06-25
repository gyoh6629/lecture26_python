class BeverageService:
    bev_no_seq = 1

    def __init__(self, dao):
        self.__dao = dao

    def view_bev_list(self):
        return self.__dao.list_bev()

    def bev_by_no(self, no):
        for bev in self.view_bev_list():
            if bev.get_no() == no:
                return bev

    def add_bev(self, bev):
        bev.set_no(BeverageService.bev_no_seq)
        BeverageService.bev_no_seq += 1
        self.__dao.add_bev(bev)

    def mod_bev(self, bev):
        self.__dao.mod_bev(bev)

    def del_bev(self, bev_no):
        self.__dao.del_bev(bev_no)