# class student:
#     def __init__(self):
#         self.name = "name"
#         self.__age = 12
#     def display(self):
#         print('age' ,self.__age )
# s = student()
# print(s.name)
# s.display()


# class bank:
#     def __init__(self,name,balance):
#         self.__balance = balance


#     def deposit(self,amount):
#         if amount > 0 :
#             self.__balance += amount
#     def withdraw(self,amount):
#         if amount > self.__balance:
#             print("insufficient balance")
#         else:
#             self.__balance -= amount
#     def get_balance(self):
#         return self.__balance
# acc = bank("name",1000)
# acc.deposit(5000)
# print(acc.get_balance())
# print(acc._balance)



# class Bank:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def withdraw(self, amount):
#         if amount > self.__balance:
#             print("Insufficient balance")
#         else:
#             self.__balance -= amount

#     def get_balance(self):
#         return self.__balance


# acc = Bank("Arun", 1000)

# acc.deposit(5000)
# print(acc.get_balance())   


##absraction------------------
# from abc import ABC, abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class rectangle(shape):
#     def __init__(self,l,b):
#         self.l = l
#         self.b = b
#     def area(self):
#         print(self.l*self.b)

# r = rectangle(10,5)
# r.area()


#area of circle

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         print("Area of Circle:", 3.14 * self.radius * self.radius)

# c = Circle(5)
# c.area()



# #area of triangle--------

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         print("Area of Triangle:", 0.5 * self.base * self.height)

# t = Triangle(10, 8)
# t.area()
