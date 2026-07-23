#####add
# def add(a,b):
#     return a+b
# print(add(a+b))




##lambda function......................
# a = lambda x: x**2
# print(a(5))


# filter with lambda------------------------
# a=[1,10,28,3,19,49,30]
# b=list(filter(lambda x: x%2 ==0,a))
# print(b)



# a=[1,10,28,3,19,49,30]
# b=list(filter(lambda x: x%2 !=0,a))
# c=list(map(lambda x: x**2,a))
# print(b)
# print(c)



#factorial----------------
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n *fact(n-1)
# print(fact(7))



#fibonocci series-----------------------
# def fib(n):
#     if n<=1:
#         return n
#     return fib(n-1)+fib(n-2)
# print(fib(1))


#sets-----------

# s = {1,2,3,4,4,5,3}
# print(s)
# s.add(7)

# s = {1,2,3,4,4,3}
# s.add(5)
# s.remove(5)
# s.pop()
# print(s)

##union sets---------------
# a = {1,2,3,4}
# b = {3,4,5,6}

# print(a | b) # union
# print(a & b) # both common
# print(a - b)
# print(a ^ b)


#dictionary--------------------
# d= {}
# print(type(d))


# student = {
#     "name": "Arun",
#     "age": 22,
#     "course": "MCA"
# }

# print(student['name'])
# print(student.get('age',0))



# student = {
#     "name": "Arun",
#     "age": 22,
#     "course": "MCA"
# }

# for key in student:
#     print(key, ":", student[key])

# student = {
#     "name": "Arun",
#     "age": 22,
#     "course": "MCA"
# }

# for key, value in student.items():
#     print(key, ":", value)


# numbers = [1, 2, 2, 3, 1, 4]

# numbers = list(set(numbers))

# print(numbers)

# student ={
#     'arun':90,
#     'chandra':57,
#     'bharath':49,
#     'arjun':77
# }
# for i,j in student.items():
#     if j>88:
#         print(i)


####to print sinle letters in word

# s = 'helloworld'
# print(s[::2])


# s = 'helloworld'
# print(s.title())
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())
# print(s.replace('hello','python'))
# print(s.find('hello'))
# print(s.count('1'))
# print(s.startswith("11"))
# print(s.endswith('1d'))
# print(len(s))






#vowel----------------

# word = input("Enter a word: ")

# count = 0

# for letter in word:
#     if letter in "aeiouAEIOU":
#         count += 1

# print("Number of vowels:", count)


# word = input("Enter a word: "
# count = 0
# for i in word:
#     if i in "aeiou":
#         print(i)
#         count += 1
# print("Total vowels:", count)




#exception handling----------
# try:
#     a = 10
#     b = 2
#     print(a / b)
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# else:
#     print("Division successful.")

#######
def validate_phone(phone):
    if len(phone):
        raise ValueError(f'phone must have 10 digits')
    return True
try:
    validate_phone('1234567890')
except ValueError as e:
    print('Error,e')