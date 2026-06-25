from Beverage.beverage import Beverage
from Beverage.beverage_dao import BeverageDAO
from Beverage.beverage_service import BeverageService
from Cart.cart import Cart
from Cart.cart_dao import CartDAO
from Cart.cart_service import CartService
from Order.order import Order
from Order.order_dao import OrderDAO
from Order.order_service import OrderService

class Cafe:
    start_menu = ['종료', '주문하기', '관리자 인증']
    order_menu = ['돌아가기', '장바구니 담기', '장바구니 확인', '결제하기']
    admin_menu = ['돌아가기', '메뉴 추가', '메뉴 수정', '메뉴 삭제', '주문 내역']

    def __init__(self):
        self.bsv = BeverageService(BeverageDAO())
        self.csv = CartService(CartDAO())
        self.osv = OrderService(OrderDAO())
    
        self.bsv.add_bev(Beverage(None, '아메리카노', 4000))
        self.bsv.add_bev(Beverage(None, '카페라떼', 5000))
        self.bsv.add_bev(Beverage(None, '아이스티', 3000))

    def main(self):
        self.welcome()
        self.run_start_menu()
        self.goodbye()
#--------------------------------------------------------------------------------------
    def welcome(self):
            print('=' * 50)
            title = 'Cafe'
            print(f'{title:^50}')
            print('=' * 50)
        
    def goodbye(self):
        print('>> Cafe 를 이용해 주셔서 감사합니다.')

    def select_menu(self, menu_list):
        print('-'*50)
        for index in range(1, len(menu_list)):
            print(f'{index}. {menu_list[index]}')
        print(f'0. {menu_list[0]}')
        print('-'*50)
        try:
            num = int(input('메뉴 : '))
        except ValueError:
            return -1
        else:
            return num
#--------------------------------------------------------------------------------------
    def run_start_menu(self):
        while True:
            menu = self.select_menu(Cafe.start_menu)
            if menu == 0: break
            elif menu == 1:
                self.start_order()
            elif menu == 2:
                self.start_admin()
            else:
                print('없는 메뉴입니다.')

    def start_order(self):
        self.run_order_menu()

    def start_admin(self):
        self.run_admin_menu()
#--------------------------------------------------------------------------------------
    def run_order_menu(self):
        print('-'*50)
        for bev in self.bsv.view_bev_list():
            print(bev)
        while True:
            menu = self.select_menu(Cafe.order_menu)
            if menu == 0: break
            elif menu == 1:
                self.order_put_cart()
            elif menu == 2:
                self.order_view_cart()
            elif menu == 3:
                self.order_pay_cart()
            else:
                print('없는 메뉴입니다.')

    def order_put_cart(self):
        no = int(input('번호 : '))
        bev = self.bsv.bev_by_no(no)
        self.csv.add_cart(Cart(None, bev.get_name(), bev.get_price()))

    def order_view_cart(self):
        print('-'*50)
        for cart in self.csv.view_cart_list():
            print(cart)
    
    def order_pay_cart(self):
        print('-'*50)
        self.order_view_cart()
        print('총 결제금액 : ', end="")
        sum = 0
        for cart in self.csv.view_cart_list():
            sum += cart.get_price()
        print(sum)
        self.csv.clear_cart()
        self.osv.create_order(Order(None, sum))
#--------------------------------------------------------------------------------------
    def run_admin_menu(self):
        admin =input('인증번호 : ')
        if admin == '1234':
            while True:
                menu = self.select_menu(Cafe.admin_menu)
                if menu == 0: break
                elif menu == 1:
                    self.admin_add_bev()
                elif menu == 2:
                    self.admin_mod_bev()
                elif menu == 3:
                    self.admin_del_bev()
                elif menu == 4:
                    self.admin_order_details()
                else:
                    print('없는 메뉴입니다.')
        return False

    def admin_add_bev(self):
        name = input('이름 : ')
        price = int(input('가격 : '))
        self.bsv.add_bev(Beverage(None, name, price))

    def admin_mod_bev(self):
        print('-'*50)
        for bev in self.bsv.view_bev_list():
            print(bev)
        no = int(input('번호 : '))
        bev = self.bsv.bev_by_no(no)
        new_price = int(input('새 가격 : '))
        self.bsv.mod_bev(Beverage(bev.get_no(), bev.get_name(), new_price))

    def admin_del_bev(self):
        print('-'*50)
        for bev in self.bsv.view_bev_list():
            print(bev)
        no = int(input('번호 : '))
        self.bsv.del_bev(no)

    def admin_order_details(self):
        for order in self.osv.view_order_details():
            print(order)
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
if __name__ == '__main__':
    app = Cafe()
    app.main()