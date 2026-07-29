##multilevel heritances

# class Animal:
#     def eat(self):
#         print("Animal eats food")

# class Bird(Animal):
#     def fly(self):
#         print("Bird can fly")

# class Parrot(Bird):
#     def speak(self):
#         print("Parrot can speak")

# # Create object
# p = Parrot()


# p.eat()
# p.fly()
# p.speak()




######public encapsulation

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display(self):
#         print("Name:", self.name)
#         print("Marks:", self.marks)

# # Create object
# s = Student("Ravi", 92)

# # Display details
# s.display()

###bankaccount...

# class BankAccount:
#     def __init__(self):
#         self.__balance = 5000

#     def show_balance(self):
#         print("Balance:", self.__balance)

# account = BankAccount()

# account.show_balance()

# print(account.__balance)




##class wallet

# class BankAccount:
#     def __init__(self):
#         self.__balance = 1000

#     def deposit(self, amount):
#         self.__balance += amount

#     def show_money(self):
#         print("money available:", self.__balance)

# account = BankAccount()

# account.deposit(500)
# account.show_money()




class BankAccount:
    def __init__(self):
        self.__balance = 10000

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.__balance)

account = BankAccount()

account.withdraw(3000)
account.show_balance()

account.withdraw(9000)
account.show_balance()




