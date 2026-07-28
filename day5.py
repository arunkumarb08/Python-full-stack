# n = [10,20,30,40,50]
# sum = 0
# for i in n:
#     sum += i
# print("sum of elements:",sum)






# list = [10,20,30,40,50]
# emp_list = []
# for i in list:
#     if i not in emp_list:
#         emp_list.append(i)
#     print(emp_list)






# user_input = input("Enter a string: ")
# emp_str = ""

# for i in range(len(user_input) - 1, -1, -1):
#     emp_str += user_input[i]

# print("Reversed string:", emp_str)







num = int(input("Enter a number: "))

if num > 1:
    is_prime = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
else:
    print(f"{num} is not a prime number")