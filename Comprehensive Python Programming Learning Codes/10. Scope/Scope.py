# # Scope in Python (مبحث دامنه در پایتون) 

# # Local Scope دامنه محلی
# def my_function():
#     x = 45  # Local Scope
#     # در داخل تابع می‌توان ایکس را فراخوانی کرد
#     print(f"function Result is {x}")

# my_function()
# # اگر ایکس را در خارج از تابع فراخوانی کنیم، خطا خواهد داد
# print(x)  

# # -------------------------------------- # 

# # Scope in Python (مبحث دامنه در پایتون) 

# # Enclosing دامنه بسته
# def outer():
#     y = 20  # Enclosing Scope
#     def inner():
#         print(y)  # دسترسی به متغیر Enclosing
#     inner()
# outer()

# # -------------------------------------- # 

# # Scope in Python (مبحث دامنه در پایتون)

# # Global Scope دامنه سراسری
# x = 30  # Global Scope

# def my_function():
#     print(f"function Result: {x}")  # در داخل تابع  می‌توان به ایکس دسترسی داشت
# my_function()

# print(f"Global Scope: {x}") # در خارج از تابع می‌توان به ایکس دسترسی داشت

# # -------------------------------------- # 

# # Scope in Python (مبحث دامنه در پایتون)

# # Global Scope and global keyword دامنه سراسری و استفاده از کلیدواژه
# # Convert local Scope to global scope تبدیل دامنه محلی به دامنه سراسری

# x = 10  # متغیر سراسری
# def my_function():
#     global x
#     x = 20  # تغییر متغیر سراسری
#     print(f"In the Function: {x}")
# my_function()
# print(f"Out the Function: {x}")  # مقدار تغییر کرده است

# # -------------------------------------- # 

# Scope in Python (مبحث دامنه در پایتون)

# Local Scope and nonlocal keyword  دامنه محلی و استفاده از کلیدواژه
# Convert local Scope to global scope تبدیل دامنه محلی به دامنه سراسری

def outer():
    x = 10  # متغیر Enclosing

    def inner():
        nonlocal x
        x = 20  # تغییر مقدار متغیر Enclosing
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()

