print("Pham Tuan Dat")
print("235752021610105")
class ATM:
    def __init__(self, balance=0):
        
        self.balance = balance
        self.is_logged_in = False
        self.pin = "1234"  

    def login(self, entered_pin):
       
        if entered_pin == self.pin:
            self.is_logged_in = True
            print("Đăng nhập thành công!")
        else:
            print("Mã PIN không chính xác! Vui lòng thử lại.")

    def check_balance(self):
       
        if self.is_logged_in:
            print(f"Số dư tài khoản của bạn là: {self.balance} VND")
        else:
            print("Vui lòng đăng nhập trước.")

    def withdraw(self, amount):
        
        if self.is_logged_in:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Rút thành công {amount} VND. Số dư còn lại: {self.balance} VND")
            else:
                print("Số tiền rút vượt quá số dư tài khoản.")
        else:
            print("Vui lòng đăng nhập trước.")

    def deposit(self, amount):
        
        if self.is_logged_in:
            self.balance += amount
            print(f"Gửi thành công {amount} VND. Số dư hiện tại: {self.balance} VND")
        else:
            print("Vui lòng đăng nhập trước.")

    def logout(self):
        
        self.is_logged_in = False
        print("Đã đăng xuất thành công.")


def main():
    atm = ATM()

    while True:
        print("\n------ MENU ATM ------")
        print("1. Đăng nhập")
        print("2. Kiểm tra số dư")
        print("3. Rút tiền")
        print("4. Gửi tiền")
        print("5. Đăng xuất")
        print("6. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            pin = input("Nhập mã PIN: ")
            atm.login(pin)
        elif choice == '2':
            atm.check_balance()
        elif choice == '3':
            amount = float(input("Nhập số tiền cần rút: "))
            atm.withdraw(amount)
        elif choice == '4':
            amount = float(input("Nhập số tiền cần gửi: "))
            atm.deposit(amount)
        elif choice == '5':
            atm.logout()
        elif choice == '6':
            print("Thoát chương trình...")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


if __name__ == "__main__":
    main()
