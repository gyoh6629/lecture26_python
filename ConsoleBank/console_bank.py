from Member.member import Member
from Member.member_service import MemberService
from Member.member_dao import MemberDAO
from Account.account import Account
from Account.account_service import AccountService
from Account.account_dao import AccountDAO

class ConsoleBank:
    start_menu = ['종료', '로그인', '회원가입']
    banking_menu = ['로그아웃', '계좌목록', '입금', '출금']
    member_myinfo_menu = []
    admin_menu = []
    admin_account_menu = []
    admin_member_menu = []

    def __init__(self):
        self.msv = MemberService(MemberDAO())
        self.asv = AccountService(AccountDAO())
        # for test
        self.msv.join(Member(0, 'A', '1111', 'aaaa'))
        self.asv.create_account(Account(0, 'Q', 10000, '0000'))

    def main(self):
        self.show_welcome()
        self.run_start_menu()
        self.say_goodbye()
#-----------------------------------------------------------------------
    def show_welcome(self):
        print('======== Console Bank ========')
        
    def say_goodbye(self):
        print('>> Console Bank 를 이용해 주셔서 감사합니다.')

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
#-----------------------------------------------------------------------    
    def run_start_menu(self):
        while True:
            menu = self.select_menu(ConsoleBank.start_menu)
            if menu == 0: break
            elif menu == 1:
                self.menu_login()
            elif menu == 2:
                self.menu_join()

    def menu_join(self):
        print('>>>> 회원가입 <<<<')
        if self.msv.join(Member(0, 'A', '1111', 'aaaa')):
            print('회원가입에 성공하였습니다.')
        else:
            print('회원가입을 할 수 없습니다.')

    def menu_login(self):
        print('>>>> 로그인 <<<<')
        if self.msv.login('A', '1111'):
            print(f'{self.msv.current_user.get_name()}님, 환영합니다.')
            if self.msv.current_user == MemberService.ADMIN_ID:
                self.run_admin_menu()
            else:
                self.run_banking_menu()
        else:
            print('로그인을 할 수 없습니다.')
    def menu_logout(self):
        pass
#-----------------------------------------------------------------------
    def run_banking_menu(self):
        print('>>>> 은행 업무 메뉴 <<<<')
        while True:
            menu = self.select_menu(self.banking_menu)
            if menu == 0: 
                self.msv.logout()
                break
            elif menu == 1:
                self.menu_list_my_accounts()
            elif menu == 2:
                self.menu_deposit()
            elif menu == 3:
                self.menu_withdraw()

    def menu_list_my_accounts(self):
        print('>>>> 내 계좌 목록 <<<<')
        self.list_members_accounts(self.msv.current_user)

    def list_members_accounts(self, id):
        account_list = self.asv.get_members_accounts(id)
        print('-'*50)
        if account_list:
            for account in account_list:
                print(account)
        else:
            print('등록된 계좌가 없습니다.')
        print('-'*50)

    def menu_deposit(self):
        print('>>>> 입금 <<<<')
        self.list_members_accounts(self.msv.current_user)
        account_no = input('>> 계좌번호 : ')
        amount = int(input('입금액 : '))
        if self.asv.deposit(account_no, amount):
            print(f'계좌번호 {account_no}에 {amount}원을 입금했습니다.')
            balance = self.asv.get_account_balance(account_no)
            if balance >= 0:
                print(f'잔액 : {balance:,}')
        else:
            print('입금을 할 수 없습니다.')

    def menu_withdraw(self):
        pass

    def menu_create_account(self):
        pass

    def menu_delete_account(self):
        pass

    def menu_myinfo(self):
        pass
#-----------------------------------------------------------------------
    def run_my_info_menu(self):
        pass

    def menu_view_myinfo(self):
        pass

    def menu_update_password(self):
        pass

    def menu_delete_membership(self):
        pass
#-----------------------------------------------------------------------
    def run_admin_menu(self):
        pass

    def menu_manage_members(self):
        pass

    def menu_manage_accounts(self):
        pass
#-----------------------------------------------------------------------
    def run_admin_account_menu(self):
        pass    

    def menu_list_all_accounts(self):
        pass

    def menu_list_member_accounts(self):
        pass
#-----------------------------------------------------------------------
    def run_admin_member_menu(self):
        pass

    def menu_list_members(self):
        pass

    def menu_view_member_info(self):
        pass

    def menu_delete_member(self):
        pass


if __name__ == '__main__':
    app = ConsoleBank()
    app.main()