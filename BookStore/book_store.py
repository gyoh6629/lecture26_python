from Book.book import Book
from Book.book_dao import BookDAO
from Book.book_service import BookService
from Cart.cart import Cart
from Cart.cart_dao import CartDAO
from Cart.cart_service import CartService
from Order.order import Order
from Order.order_dao import OrderDAO
from Order.order_service import OrderService
from User.user import User
from User.user_dao import UserDAO
from User.user_service import UserService
#-----------------------------------------------------------------------
class BookStore:
    start_menu = ['종료', '도서목록', '회원가입', '로그인'] # 시작메뉴
    user_menu = ['로그아웃', '도서', '장바구니', '주문내역', '내 정보'] # 사용자메뉴
    user_book_menu = ['돌아가기', '검색', '장바구니'] # 도서
    user_cart_menu = ['돌아가기', '담기', '빼기', '초기화', '주문하기'] # 장바구니
    user_info_menu = ['돌아가기', '내 정보 조회', '내 정보 수정', '탈퇴'] # 사용자 정보
    user_modify_info_menu = ['돌아가기', '아이디 변경', '비밀번호 변경', '주소 변경'] # 사용자 정보 수정
    admin_menu = ['로그아웃', '도서관리', '주문관리', '회원관리'] # 관리자메뉴
    admin_book_menu = ['돌아가기', '재고수정', '도서삭제'] # 도서관리
    admin_order_menu = ['돌아가기', '주문목록', '회원 별 주문내역'] # 주문관리
    admin_user_menu = ['돌아가기', '회원목록', '회원퇴출'] # 회원관리
#-----------------------------------------------------------------------
    def __init__(self):
        self.bs = BookService(BookDAO())
        self.cs = CartService(CartDAO())
        self.os = OrderService(OrderDAO())
        self.us = UserService(UserDAO())
#-----------------------------------------------------------------------실행
    def main(self):
        self.welcome()
        self.show_start_menu()
        self.goodbye()
#-----------------------------------------------------------------------형식
    def welcome(self):
            print('=' * 50)
            title = 'Console Online Book Store'
            print(f'{title:^50}')
            print('=' * 50)
        
    def goodbye(self):
        print('>> Console Online Book Store 를 이용해 주셔서 감사합니다.')

    def select_menu(self, menu_list):
        print('-'*50)
        for index in range(1, len(menu_list)):
            print(f'{index}. {menu_list[index]}')
        print(f'0. {menu_list[0]}')
        print('-'*50)
        try:
            num = int(input('>> 메뉴 : '))
        except ValueError:
            return -1
        else:
            return num
#-----------------------------------------------------------------------시작
    def show_start_menu(self):
        while True:
            menu = self.select_menu(BookStore.start_menu)
            if menu == 0: break # 돌아가기
            elif menu == 1: # 도서목록
                self.start_menu_1()
            elif menu == 2: # 회원가입
                self.start_menu_2()
            elif menu == 3: # 로그인
                self.start_menu_3()
            else:
                print('없는 메뉴입니다.')
    
    def start_menu_1(self): # 도서목록
        book_list = self.bs.view_book_list()
        if len(book_list) == 0:
            print('현재 등록된 도서가 없습니다.')
            return
        for list in book_list:
            print(list)
        

    def start_menu_2(self): # 회원가입
        print('>>>>> 회원가입 <<<<<')
        id = input('아이디 입력 : ')
        password = input('패스워드 입력 : ')
        address = input('주소 입력 : ')
        if self.us.join(User(None, id, password, address)):
            print('회원가입에 성공하였습니다.')
        else:
            print('회원가입에 실패하였습니다.')

    def start_menu_3(self): # 로그인
        print('>>>>> 로그인 <<<<<')
        id = input('아이디 입력 : ')
        password = input('패스워드 입력 : ')
        if self.us.login(id, password):
            print(f'{self.us.current_user}님, 환영합니다.')
            if self.us.current_user == UserService.ADMIN_ID:
                self.show_admin_menu()
            else:
                self.show_user_menu()
        else:
            print('로그인에 실패하였습니다.')
#-----------------------------------------------------------------------시작 > 사용자메뉴
    def show_user_menu(self):
        while True:
            menu = self.select_menu(BookStore.user_menu)
            if menu == 0: # 로그아웃
                self.us.logout()
                break 
            elif menu == 1: # 도서
                self.user_menu_1()
            elif menu == 2: # 장바구니
                self.user_menu_2()
            elif menu == 3: # 주문내역
                self.user_menu_3()
            elif menu == 4: # 내 정보
                if self.user_menu_4():
                    break
            else:
                print('없는 메뉴입니다.')

    def user_menu_1(self): # 도서
        book_list = self.bs.view_book_list()
        if book_list:
            for list in book_list:
                print(list)
            self.show_user_book_menu()
            return
        print('현재 등록된 도서가 없습니다.')       

    def user_menu_2(self): # 장바구니
        self.show_user_cart_menu()
    
    def user_menu_3(self): # 주문내역
        user_number = self.us.view_user_number()
        order_list = self.os.list_order_by_user(user_number)
        if order_list:
            for order in order_list:
                print(order)
                return
        print('주문내역이 없습니다')

    def user_menu_4(self): # 내 정보
        self.show_user_info_menu()
#-----------------------------------------------------------------------사용자메뉴 > 도서
    def show_user_book_menu(self):
        while True:
            menu = self.select_menu(BookStore.user_book_menu)
            if menu == 0: break # 돌아가기
            elif menu == 1: # 검색
                self.user_book_menu_1()
            elif menu == 2: # 장바구니
                self.user_book_menu_2()
            else:
                print('없는 메뉴입니다.')

    def user_book_menu_1(self): # 검색
        book_name = input('제목 : ')
        result_list = self.bs.search_book(book_name)
        if result_list:
            for result in result_list:
                print(result)
                return
        print('검색 결과가 없습니다.')

    def user_book_menu_2(self): # 장바구니
        self.show_user_cart_menu()
#-----------------------------------------------------------------------사용자메뉴 > 장바구니
    def show_user_cart_menu(self): 
        user_number = self.us.view_user_number()
        cart_list = self.cs.view_cart(user_number)
        for list in cart_list:
            print(list)
        while True:
            menu = self.select_menu(BookStore.user_cart_menu)
            if menu == 0: break # 돌아가기
            elif menu == 1: # 담기
                self.user_cart_menu_1()
            elif menu == 2: # 빼기
                self.user_cart_menu_2()
            elif menu == 3: # 초기화
                self.user_cart_menu_3()
            elif menu == 4: # 주문하기
                self.user_cart_menu_4()
            else:
                print('없는 메뉴입니다.')
        
    def user_cart_menu_1(self): # 담기
        book_number = input('도서번호 : ')
        book = self.bs.view_book_info(book_number)
        if self.cs.add_cart(book):
            print('장바구니에 추가되었습니다.')
        else:
            print('없는 도서입니다.')

    def user_cart_menu_2(self): # 빼기
        book_number = input('도서번호 : ')
        user_number = self.us.view_user_number()
        if self.cs.add_cart(book_number, user_number):
            print('장바구니에서 제거되었습니다.')
        else:
            print('없는 도서입니다.')

    def user_cart_menu_3(self): # 초기화
        user_number = self.us.view_user_number()
        if self.cs.empty_cart(user_number):
            print('장바구니를 비웠습니다.')
        else:
            print('장바구니를 비우는데 실패했습니다.')

    def user_cart_menu_4(self): # 주문하기
        user_number = self.us.view_user_number()
        cart_list = self.cs.view_cart(user_number)
        if cart_list:
            for cart in cart_list:
                book_number = cart.get_book_number()
                book_name = cart.get_book_name()
                author = cart.get_author()
                price = cart.get_price()
                self.os.create_order(None, book_number, book_name, author, price, user_number)
            return
        print('장바구니가 비었습니다.')
    #-----------------------------------------------------------------------사용자메뉴 > 내 정보
    def show_user_info_menu(self):
        while True:
            menu = self.select_menu(BookStore.user_info_menu)
            if menu == 0: break # 돌아가기
            elif menu == 1: # 내 정보 조회
                self.user_info_menu_1()
            elif menu == 2: # 내 정보 수정
                self.user_info_menu_2()
            elif menu == 3: # 탈퇴
                if self.user_info_menu_3():
                    return True
            else:
                print('없는 메뉴입니다.')

    def user_info_menu_1(self): # 내 정보 조회
        password = input('비밀번호 입력 : ')
        info = self.us.view_user_info(password)
        if info:
            print(info)
            return
        print('비밀번호가 일치하지 않습니다.')

    def user_info_menu_2(self): # 내 정보 수정
        self.show_user_modify_info_menu()

    def user_info_menu_3(self): # 탈퇴
        password = input('비밀번호 입력 : ')
        if self.us.withdrawal_by_user(password):
            return True
        return   
#-----------------------------------------------------------------------내 정보 > 내 정보 수정
    def show_user_modify_info_menu(self):
        while True:
            menu = self.select_menu(BookStore.user_modify_info_menu)
            if menu == 0: break # 돌아가기
            elif menu == 1: # 아이디 변경
                self.user_modify_info_menu_1()
            elif menu == 2: # 비밀번호 변경
                self.user_modify_info_menu_2()
            elif menu == 3: # 주소 변경
                self.user_modify_info_menu_3()
            else:
                print('없는 메뉴입니다.')

    def user_modify_info_menu_1(self): # 아이디 변경
        new_id = input('새 아이디 입력 : ')
        password = input('비밀번호 입력 : ')
        if self.us.modify_id(new_id, password):
            print('아이디가 변경되었습니다.')
            return
        print('비밀번호가 일치하지 않습니다.')

    def user_modify_info_menu_2(self): # 비밀번호 변경
        new_password = input('새 비밀번호 입력 : ')
        password = input('비밀번호 입력 ; ')
        if self.us.modify_id(new_password, password):
            print('비밀번호가 변경되었습니다.')
            return
        print('비밀번호가 일치하지 않습니다.')

    def user_modify_info_menu_3(self): # 주소 변경
        new_address = input('새 주소 입력 : ')
        password = input('비밀번호 입력 : ')
        if self.us.modify_id(new_address, password):
            print('주소가 변경되었습니다.')
            return
        print('비밀번호가 일치하지 않습니다.')
#-----------------------------------------------------------------------시작 > 관리자메뉴
    def show_admin_menu(self):
        while True:
            menu = self.select_menu(BookStore.admin_menu)
            if menu == 0: # 돌아가기
                self.us.logout()
                break 
            elif menu == 1: # 도서관리
                self.admin_menu_1()
            elif menu == 2: # 주문관리
                self.admin_menu_2()
            elif menu == 3: # 회원관리
                self.admin_menu_3()
            else:
                print('없는 메뉴입니다.')

    def admin_menu_1(self): # 도서관리
        self.show_admin_book_menu()

    def admin_menu_2(self): # 주문관리
        self.show_admin_order_menu()

    def admin_menu_3(self): # 회원관리
        self.show_user_book_menu()
#-----------------------------------------------------------------------관리자메뉴 > 도서관리
    def show_admin_book_menu(self):
        while True:
            menu = self.select_menu(BookStore.admin_book_menu)
            if menu == 0: # 돌아가기
                break 
            elif menu == 1: # 도서추가
                self.admin_book_menu_1()
            elif menu == 2: # 재고수정
                self.admin_book_menu_2()
            elif menu == 3: # 도서삭제
                self.admin_book_menu_3()
            else:
                print('없는 메뉴입니다.')

    def admin_book_menu_1(self):
        book_list = self.bs.view_book_list()
        if book_list:
            for list in book_list:
                print(list)
        book_name = input('제목 입력 : ')
        author = input('저자 입력 : ')
        publisher = input('출판사 입력 : ')
        price = input('가격 입력 : ')
        stock = input('재고 입력 : ')
        if self.bs.add_book(None, book_name, author, publisher, price, stock):
            print('도서가 추가되었습니다.')
            return
        print('도서를 추가하는데 실패하였습니다.')
#-----------------------------------------------------------------------관리자메뉴 > 주문관리
    def show_admin_order_menu(self):
        while True:
            menu = self.select_menu(BookStore.admin_order_menu)
            if menu == 0: # 돌아가기
                break 
            elif menu == 1: # 도서관리
                self.admin_menu_1()
            elif menu == 2: # 주문관리
                self.admin_menu_2()
            elif menu == 3: # 회원관리
                self.admin_menu_3()
            else:
                print('없는 메뉴입니다.')
#-----------------------------------------------------------------------관리자메뉴 > 회원관리
    def show_admin_user_menu(self):
        while True:
            menu = self.select_menu(BookStore.admin_user_menu)
            if menu == 0: # 돌아가기

                break 
            elif menu == 1: # 도서관리
                self.admin_menu_1()
            elif menu == 2: # 주문관리
                self.admin_menu_2()
            elif menu == 3: # 회원관리
                self.admin_menu_3()
            else:
                print('없는 메뉴입니다.')

admin_book_menu = ['돌아가기', ,'도서추가', '재고수정', '도서삭제'] # 도서관리
    admin_order_menu = ['돌아가기', '주문목록', '회원 별 주문내역'] # 주문관리
    admin_user_menu = ['돌아가기', '회원목록', '회원퇴출'] # 회원관리