# # Errors in Python (خطاها در پایتون)

# # Types of Errors
#     # Syntax Errors
#     # Runtime Errors
#     # Logical Errors


# # Types of Errors
#     # Syntax Errors
    
# print("Hello World"

# # -------------------------------------- # 

# Errors in Python (خطاها در پایتون)

# Types of Errors
#     Syntax Errors
#     Runtime Errors
#     Logical Errors

# Runtime Errors

# print(100/0)

# # -------------------------------------- # 

# # Errors in Python (خطاها در پایتون)

# # Types of Errors
# #     Syntax Errors
# #     Runtime Errors
# #     Logical Errors

# # Runtime Errors

# my_list = [1, 2, 3]
# print(my_list[5])

# # -------------------------------------- # 

# # Errors in Python (خطاها در پایتون)

# # Types of Errors
# #     Syntax Errors
# #     Runtime Errors
# #     Logical Errors

# # Logical Errors خطای منطقی
# def average(a, b):
#     return a + b / 2
#     # به صورت زیر محاسبه خواهد کرد
#     # a + (b/2)
# print(f"First Ans: {average(a=14,b=12)}")

# # Solve Problem حل خطای منطقی
# def average(a, b):
#     return (a + b) / 2
#     # به صورت زیر محاسبه خواهد کرد
#     # (a + b) / 2
# print(f"Second Ans: {average(a=14,b=12)}")

# # -------------------------------------- # 

# # Errors in Python (خطاها در پایتون)
# # Other Errors
# #     TypeErrors 

# def Sum_Operation(a, b):
#     return f"Sum of a , b: {a + b}"

# print(Sum_Operation("12", 4))

# # -------------------------------------- # 

# # Errors in Python (خطاها در پایتون)
# # Other Errors
# #     ValueErrors

# def Value_Error_Example(a):
#     return f"{int(a)}"

# print(Value_Error_Example("Hello World!"))

# # -------------------------------------- # 

# # Errors in Python (خطاها در پایتون)
# # Other Errors
# #     NameErrors

# # هیچ متغیری یا تابعی تعریف نکردیم
# print(f"value of x is {x}")

# # -------------------------------------- # 

# # Errors in Python (خطاها در پایتون)
# # Other Errors
# #     KeyErrors

# mydict = {
#     "firstName": "Reza",
#     "age": 23
# }
# # Available Key
# print(f"First Name:{mydict["firstName"]}")

# # Not Available Key
# print(f"Last Name:{mydict["lastName"]}")

# # -------------------------------------- # 

# Errors in Python (خطاها در پایتون)
# Other Errors
#     ImportErrors

# import no_exist_module

# print(help(no_exist_module))

# # -------------------------------------- # 

# Errors in Python (خطاها در پایتون)
# Errors Handling مدیریت خطاها
    # Try/Except
    # Try/Except/Else/Finally

# Try/Except
"""
try:
    # کدی که ممکن است خطا تولید کند
except ErrorType:
    # کدی که در صورت رخ دادن خطا اجرا می‌شود

"""
# # -------------------------------------- # 

# # Errors in Python (خطاها در پایتون)
# # Errors Handling مدیریت خطاها
#     # Try/Except

# try:
#     result = 265 / 0
# except ZeroDivisionError:
#     print("Division by zero is not possible.")

# # -------------------------------------- # 

# # Errors in Python (خطاها در پایتون)
# # Errors Handling مدیریت خطاها
#     # Try/Except

# # Many Except Section
# try:
#     num = int(input("Enter a number:"))
#     result = 10 / num
# except ValueError:
#     print("Please Enter Number Not Integer!")
# except ZeroDivisionError:
#     print("Division by zero is not possible!")

# # -------------------------------------- # 

# # Errors in Python (خطاها در پایتون)
# # Errors Handling مدیریت خطاها
#     # Try/Except

# # If Error is not clear: اگر نوع خطا مشخص نباشد
# try:
#     num = int("hello")
# except:
#     print("An unspecified error has occurred.")

# # -------------------------------------- # 

# # Errors in Python (خطاها در پایتون)
# # Errors Handling مدیریت خطاها
# #     Try/Except/Else/Finally

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("Division by zero is not possible!")
# except ValueError:
#     print("The Input is invalid!")
# else:
#     print("Result:", result)
# finally:
#     print("End of the process.")



