#############oops concept--------------
# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f'Name:{self.name},Age: {self.age}')

# s = student('name',22)
# s.display()





# class student:
#     def __init__(self,name,age,course):
#         self.name = name
#         self.age = age
#         self.course= course
#     def display(self):
#         print(f'Name:{self.name},Age: { self.age}')
#     def study(self,subject):
#         print(f'{self.name} is studying {subject}')

# s = student('name',22,"pfsd")
# s.display()
# s.study('python')



# class Employee:
#     def __init__(self, name, emp_id, salary, dept):
#         self.name = name
#         self.emp_id = emp_id
#         self.salary = salary
#         self.dept = dept

#     def display(self):
#         print(f"Name      : {self.name}")
#         print(f"Employee ID: {self.emp_id}")
#         print(f"Salary    : {self.salary}")
#         print(f"Department: {self.dept}")

#     def work(self):
#         print(f"{self.name} is working in the {self.dept} department.")


# # Create an object
# s = Employee("Arun", 101, 50000, "IT")

# # Call methods
# s.display()
# s.work()



#area of the circle-----------------

# class  circle:
#     pi = 3.14
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return circle.pi * self.radius ** 2

# c = circle(5)
# print(c.area())



#area of the triangle----------------------


# class triangle:
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height
#     def area(self):
#         return 0.5 * self.base * self.height

# t = triangle(10,20)
# print(t.area())



#---------------------
# class circle:
#     def __init__(self,radius):
#         self.radius = radius
#     @classmethod
#     def change_pi(cls,value):
#         cls.pi = value

#     @staticmethod
#     def info():
#         print('this area of the circle')
#     def area(self):
#         return self.pi * self.radius ** 2
   

# c = circle(5)
# d = change_pi(6)
# print(c.area())
# circle.info()


# # single inheritances-----------------
# class parent:
#     def dispaly(self):
#         print("this is a parent class")
#     def child(parent):
#         def show(self):
#             print("this is a child class")


# obj = child()
# obj.display()
# obj.show()


######multiple inheritances---------------
# class father:
#     def display(self):
#         print("this  is a parent class")
# class mother(father):
#     def show(self):
#         print("this is a child class")
# class child(mother):
#     def show1(self):
#         print("this is a multiple inheritance")

# obj = child()
# obj.display()
# obj.show()
# obj.show1()


# product details-------------

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def display(self):
#         print(f"Product : {self.name}")
#         print(f"Price   : {self.price}")


# class Clothing(Product):
#     def __init__(self, name, price, warranty):
#         super().__init__(name, price)
#         self.warranty = warranty

#     def display1(self):
#         self.display()
#         print(f"Warranty: {self.warranty} year(s)")


# c1 = Clothing("Shirt", 2000, 1)
# c1.display1()



# #-----------------
# class Employee:
#     def __init__(self, name, emp_id, language, team_no):
#         self.name = name
#         self.emp_id = emp_id
#         self.language = language
#         self.team_no = team_no

#     def display(self):
#         print(f"Employee Name       : {self.name}")
#         print(f"Employee ID         : {self.emp_id}")
#         print(f"Programming Language: {self.language}")
#         print(f"Team Number         : {self.team_no}")


# # Create object
# e1 = Employee("Arun", 101, "Python", 5)

# # Call methods
# e1.display()






# #capturing a brand name ------------------------
# class Call:
#     def calling(self):
#         print("Calling...")


# class Capture:
#     def capturing(self):
#         print("Capturing image...")


# class Brand(Call, Capture):
#     def __init__(self, smartphone):
#         self.smartphone = smartphone

#     def display(self):
#         print(f"Smartphone Brand: {self.smartphone}")


# # Create object
# b1 = Brand("iphone")

# # Call methods
# b1.display()
# b1.calling()
# b1.capturing()








class Person:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_name(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)


# Create an object
student = Person("Rahul", 101)

# Call the method
student.display_name()
