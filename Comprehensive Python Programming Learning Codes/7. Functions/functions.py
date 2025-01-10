# # Functions in Python (توابع در پایتون)

# # Example: 
# def greet():
#     print("Hello, World!")

# greet()

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)
# # Example: 
# def Sum(Score_List):
#     total = 0
#     for i in Score_List:
#         total += i
#     return total


# myScores = [18, 17, 20, 11, 16]
# print(f"Sum of myScores is {Sum(myScores)}")

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)
# # Example: 

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# number = int(input("please Enter integer number: "))
# if number < 0:
#     print("Sorry, factorial does not exist for negative numbers")
# else:
#     result = factorial(number)
#     print("The factorial of {} is: {}".format(number, result))

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # Function with () and without ()
# # With ()

# def greet():
#     print("Hello, World!")

# greet()

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # Function with () and without ()
# # Without ()

# def greet():
#     return "Hello, World!"

# greeting = greet

# print(greeting())

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # Argument and Parameter
# # Parameter

# def greet(name):
#     return f"Hello, {name}!"

# print(greet("Alice"))  
# print(greet("Bob"))  

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)
# # Types of Parameters
# # Positional Parameters پارامترهای موقعیتی

# def add(x, y):
#        return x + y
   
# print(add(10, 20))  

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # Types of Parameters
# # Keyword Parameters پارامترهای کلیدواژه‌ای

# def introduce(name, age):
#     return f"My name is {name} and I am {age} years old."

# print(introduce(age=25, name="Alice"))

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # Types of Parameters
# # Default Parameters پارامترهای پیش فرض

# def greet(name="Guest"):
#     return f"Hello, {name}!"

# print(greet())
# print(greet("Alice"))

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # Types of Parameters
# # Arbitrary Parameters پارامترهای دلخواه

# def summarize(*args):
#     return sum(args)

# print(f"Answer is: {summarize(1, 2, 3, 4)}")  

# # -------------------------------------- # 

# Functions in Python (توابع در پایتون)

# Types of Arguments
# Positional Arguments آرگومان های موقعیتی

# def calculate_area(length, width): 
#     return length * width # محاسبه مساحت یک مستطیل

# area = calculate_area(5, 3)  # طول = 5، عرض = 3
# print(area)  


# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # Types of Arguments
# # Keyword Arguments آرگومان کلیدواژه

# def calculate_area(length, width): 
#     return length * width # محاسبه مساحت یک مستطیل

# area = calculate_area(length=5, width=3)  # نام آرگومان‌ها مشخص شده
# print(area) 


# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # Types of Arguments
# # Arbitrary Arguments آرگومان دلخواه

# def print_info(*args, **kwargs):
#        print("Positional Arguments:", args)
#        print("Keyword Arguments:", kwargs)

# print_info("Alice", 30, city="New York", profession="Engineer")

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # difference between argument and parameter in python

# def introduce(name, age): 
#     # name and age are Parameter
#     return f"My name is {name} and I am {age} years old."

# print(introduce("Alice", 30)) 
# # "Alice" and 30 are Argument

# print(introduce("Reza", 24))
# # "Reza" and 24 are Argument

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # Types of Arguments
# # Arbitrary Arguments (*args explain) آرگومان های دلخواه
# def sum_numbers(*args):
#     total = sum(args)
#     return total

# print(sum_numbers(1, 2, 3, 4))  
# print(sum_numbers(5, 10, 15))    

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # Types of Arguments
# # Arbitrary Arguments (**kwargs explain)

# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_info(name="Alice", age=30, city="New York")

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # Types of Arguments
# # Arbitrary Arguments (*args and **kwargs)

# def display_info(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)
    
# display_info(1, 2, 3, name="Alice", age=30)

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # *args Examples
# # Example 1: Sum many numbers using *args

# def sum_all(*args):
#     total = 0
#     for number in args:
#         total += number
#     return total

# print(f"Sum of the (1, 2, 3): {sum_all(1, 2, 3)}")
# print(f"Sum of the (10, 20, 30, 40): {sum_all(10, 20, 30, 40)}") 

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # *args Examples
# # Example 2: Display a message and then several names using *args

# def greet(message, *names):
#     for name in names:
#         print(f"{message}, {name}!")

# greet("Hello", "Ali", "Sara", "Reza")

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # **kwargs Examples
# # Example 1: Display a user's information using **kwargs

# def display_user_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# display_user_info(name="Ali", age=25, job="Engineer")

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # **kwargs Examples
# # Example 2: Create a personalized message using

# def custom_message(template, **kwargs):
#     return template.format(**kwargs)

# message = custom_message("Hello {name}, you have {notifications} new notifications.", 
#                         name="Sara", notifications=5)
# print(message)


# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # ** Lambda Function ** توابع لامدا

# # Example 1: توان دوم اعداد فهرست
# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, numbers))

# print(squared)

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # ** Lambda Function **
# # Example 2: جمع کردن مقادیر دو فهرست متناظر

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# summed = list(map(lambda x, y: x + y, list1, list2))

# print(f"Sum of the Lists: {summed}")

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # ** Lambda Function **
# # Example 3: مرتب‌سازی لیستی از رشته‌ها بر اساس طول آن‌ها

# words = ['apple', 'banana', 'kiwi', 'grape']
# sorted_words = sorted(words, key=lambda x: len(x))

# print(f"Sorted List: {sorted_words}")

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # zip(), map(), filter()
# # Zip Function ( zip() )

# names = ['Ali', 'Sara', 'Reza']
# ages = [30, 27, 24]
# combined = zip(names, ages)

# print(list(combined))

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # zip(), map(), filter()
# # Map Function ( map() )

# numbers = [1, 2, 3, 4]
# squared_numbers = map(lambda x: x**2, numbers)

# print(list(squared_numbers))

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # zip(), map(), filter()
# # Map Function ( map() )

# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]
# added_numbers = map(lambda x, y: x + y, numbers1, numbers2)

# print(list(added_numbers))

# # -------------------------------------- # 

# # Functions in Python (توابع در پایتون)

# # zip(), map(), filter()
# # Filter Function ( filter() )

# numbers  = [1, 2, 3, 4, 5, 6]
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# odd_numbers = filter(lambda x: x%2 != 0, numbers)

# print(f"Even numbers: {list(even_numbers)}")
# print(f"Odd numbers: {list(odd_numbers)}")
