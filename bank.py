from abc import ABC, abstractmethod


# -------------------- Abstract Class --------------------
class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display(self):
        pass


# -------------------- Bank Account --------------------
class BankAccount(Person):
    total_account = 0

    def __init__(self, name, account_no, balance):
        super().__init__(name)
        self.account_no = account_no
        self.__balance = balance
        BankAccount.total_account += 1

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Amount cannot be negative.")

    # Deposit
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount Deposited Successfully.")
        else:
            print("Invalid deposit amount.")

    # Withdraw
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient Balance.")
        else:
            self.__balance -= amount
            print("Amount Withdrawn Successfully.")

    # Check Balance
    def check_balance(self):
        print("Current Balance:", self.__balance)

    # Display Details
    def display_details(self):
        print("\n----- Account Details -----")
        print("Account Number :", self.account_no)
        print("Account Holder :", self.name)
        print("Balance        :", self.__balance)

    # Abstract Method Implementation
    def display(self):
        self.display_details()

    # Class Method
    @classmethod
    def show_total(cls):
        print("Total Accounts:", cls.total_account)

    # Static Method
    @staticmethod
    def bank_rules():
        print("\n------ Bank Rules ------")
        print("Minimum Balance : 1000")
        print("Working Days    : Monday - Friday")
        print("Bank Hours      : 9:00 AM - 5:00 PM")
        print("Interest Rate   : 5%")
    
    def add_interest(self):

        interest = self.__balance * 0.05
        self.__balance += interest
        print(f"Interest Added: {interest:.2f}")
        print(f"Updated Balance: {self.__balance:.2f}")

# -------------------- Savings Account --------------------
class SavingsAccount(BankAccount):
    def __init__(self, name, account_no, balance):
        super().__init__(name, account_no, balance)

    def display(self):
        self.display_details()


# -------------------- Bank --------------------
class Bank:
    def __init__(self):
        self.accounts = {}

    # Create Account
    def create_account(self):
        account_no = int(input("Enter Account Number: "))

        if account_no in self.accounts:
            print("Account already exists!")
            return

        name = input("Enter Account Holder Name: ")
        balance = float(input("Enter Initial Balance: "))

        account = SavingsAccount(name, account_no, balance)
        self.accounts[account_no] = account

        print("Account Created Successfully.")

    # Search Account
    def search(self):
        account_no = int(input("Enter Account Number: "))

        if account_no in self.accounts:
            return self.accounts[account_no]
        else:
            print("Account Not Found.")
            return None

    # Deposit
    def deposit(self):
        account = self.search()

        if account:
            amount = float(input("Enter Deposit Amount: "))
            account.deposit(amount)

    # Withdraw
    def withdraw(self):
        account = self.search()

        if account:
            amount = float(input("Enter Withdrawal Amount: "))
            account.withdraw(amount)

    # Display
    def display(self):
        account = self.search()

        if account:
            account.display()

    # Check Balance
    def check_balance(self):
        account = self.search()

        if account:
            account.check_balance()


    @staticmethod
    def bank_rules():
        print("\n------ Bank Rules ------")
        print("Minimum Balance : 1000")
        print("Working Days    : Monday - Friday")
        print("Bank Hours      : 9:00 AM - 5:00 PM")
        print("Interest Rate   : 5%")


# -------------------- Main Program --------------------
bank = Bank()

while True:
    print("\n========== BANK MANAGEMENT SYSTEM ==========")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Account")
    print("5. Check Balance")
    print("6. Bank Rules")
    print("7. Total Accounts")
   

    print("8. Exit")
    

    try:
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            bank.create_account()

        elif choice == 2:
            bank.deposit()

        elif choice == 3:
            bank.withdraw()

        elif choice == 4:
            bank.display()

        elif choice == 5:
            bank.check_balance()

        elif choice == 6:
            print("Option 6 selected")
            BankAccount.bank_rules()

        elif choice == 7:
            print("Option 7 selected")
            BankAccount.show_total()

        

        elif choice == 8:
            print("Thank You for Using Bank Management System.")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please enter a valid number.")

        