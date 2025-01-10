# # Dictionary in python (دیکشنری در پایتون)
# """
# Syntax:
#        my_dictionary = {
#            key:value
#        }
# """ 
# # Examples
# dictionary_example_1 = {
#     "name": "Reza",
#     "age": 23,
#     "favorite color": "yellow"
# }
# dictionary_example_2 = {
#     "car_1": {
#         "Brand": "Chevrolet",
#         "Model": "Corvette"
#     },
#     "car_1": {
#         "Brand": "Dodge",
#         "Model": "Viper"
#     }
# }

# -------------------------------------- #

# # Dictionary in python (دیکشنری در پایتون)
# # Function => تابع
# def Sum_Two_Number(a,b):
#     return a + b

# dictionary_example_3 = {
#     1: "Hello",
#     2: "Good_bye",
#     "3": "This is String",
#     ("a", "b", "c"): 1,
#     ("d", "e", "f"): ["Chevrolet", "Dodge"],
#     "Car": {
#         "Brand": "Dodge",
#         "Model": "Viper"
#     },
#     "Sum_Function": Sum_Two_Number
# }
# x = dictionary_example_3["Sum_Function"](2,1)
# print(x) 

# -------------------------------------- #

# # Dictionary in python (دیکشنری در پایتون)
# # define key:value for dictionary
#         # First method: insert to dictionary
# Car_1 = {
#     "Brand": "Chevrolet",
#     "Model": "Corvette C8",
#     "Year": 2023,
#     "Colors": ["Red", "Green", "Blue", "Yellow"]
# }
# print(f"Information of Car_1 is:\n\t{Car_1}")

# # define key:value for dictionary
#         # Second method: Car_Info[key] = value
# Car_2 = {}
# Car_2["Brand"] = "Ford"
# Car_2["Model"] = "Mustang"
# Car_2["Year"] = 2020
# Car_2["Colors"] = ["Gray", "White", "Orange", "Black"]

# print(f"Information of Car_2 is:\n\t{Car_2}")

# -------------------------------------- #

# # Dictionary in python (دیکشنری در پایتون)
# # Change value of a special key
# car_info = {
#     'Brand': 'Chevrolet',
#     'Model': 'Corvette C8',
#     'Year': 2023
# }
# print(f"Unchanged Dictionary: \n\t{car_info}")

# # If key is Exist:
# car_info["Year"] = 2024
# print(f"Change value of 'year' key:  \n\t{car_info}")

# # If key is NOT Exist:
# car_info["color"] = 'red'
# print(f"Define New Key and Value:  \n\t{car_info}")

# -------------------------------------- #

# # Dictionary in python (دیکشنری در پایتون)
# # Removing key:value from Dictionary
# my_car_info = {
#     'Brand': 'Chevrolet',
#     'Model': 'Corvette C8',
#     'Year': 2024,
#     'color': 'red'
# }
# # pop() method
# my_car_info.pop('color')
# print(f"Remove key:value with pop method: \n\t{my_car_info}")

# # popitem() method
# my_car_info.popitem()
# print(f"Remove key:value with popitem method: \n\t{my_car_info}")

# # del keyword
# del my_car_info["Model"]
# print(f"Remove key:value with del keyword: \n\t{my_car_info}")

# -------------------------------------- #

# # Dictionary in python (دیکشنری در پایتون)
# # Remove All key:value from Dictionary

# my_car_info = {
#     'Brand': 'Chevrolet',
#     'Model': 'Corvette C8',
#     'Year': 2024,
# }
# print(f"Before using clear method: \n\t{my_car_info}")

# # clear method for remove every key and value of Dictionary
# my_car_info.clear()

# print(f"After using clear method: \n\t{my_car_info}")

# -------------------------------------- #

# # Dictionary in python (دیکشنری در پایتون)
# # Copy of Dictionary

# my_car_info = {
#     'Brand': 'Chevrolet',
#     'Model': 'Corvette C8',
#     'Year': 2024,
# }
# print(f"Main Dictionary: \n\t{my_car_info}")

# # Using copy method
# car_info_copy_1 = my_car_info.copy()
# print(f"Copy of my_car_info by copy method: \n\t{car_info_copy_1}")

# # Using dict build-in function
# car_info_copy_2 = dict(my_car_info)
# print(f"Copy of my_car_info by dict build-in: \n\t{car_info_copy_2}")

# -------------------------------------- #

# # Dictionary in python (دیکشنری در پایتون)
# # Nested Dictionary Example
# nested_dict = {
#     "person1": {"name": "Reza", "age": 23},
#     "person2": {"name": "Ali", "age": 22},
#     "person3": {"name": "Mohammad", "age": 24}
# }
# print(nested_dict)

# -------------------------------------- #

# # Dictionary in python (دیکشنری در پایتون)
# # Access to Nested Dictionary items 
# nested_dict = {
#     "person1": {"name": "Reza", "age": 23},
#     "person2": {"name": "Ali", "age": 22},
#     "person3": {"name": "Mohammad", "age": 24}
# }

# # دسترسی به دیکشنری مربوط به شخص اول
# print(f"Person1 info is: \n\t{nested_dict["person1"]}")      

# # دسترسی به نام شخص دوم
# print(f"Name of person2 is: \n\t{nested_dict["person2"]["name"]}") 

# # دسترسی به سن شخص سوم
# print(f"Age of person3 is: \n\t{nested_dict["person3"]["age"]}")   

# -------------------------------------- #

# # Dictionary in python (دیکشنری در پایتون)
# # Add item/items to nested dictionary

# nested_dict = {
#     "person1": {"name": "Reza", "age": 23},
#     "person2": {"name": "Ali", "age": 22},
#     "person3": {"name": "Mohammad", "age": 24}
# }
# print(f"Main Dictionary: \n\t{nested_dict}")

# # افزودن شهر به اطلاعات شخص اول
# nested_dict["person1"]["city"] = "Tabriz"  
# print(f"Update 1: \n\t{nested_dict}")

# # افزودن شخص جدید
# nested_dict["person4"] = {"name": "Diana", "age": 28}  
# print(f"Update 2: \n\t{nested_dict}")

# -------------------------------------- #

# # Dictionary in python (دیکشنری در پایتون)
# # remove item/items from nested dictionary

# nested_dict = {
#     "person1": {"name": "Reza", "age": 23, "city": "Tabriz"},
#     "person2": {"name": "Ali", "age": 22},
#     "person3": {"name": "Mohammad", "age": 24},
#     "person4": {"name": "Diana", "age": 28}
# }
# print(f"Main Dictionary: \n\t{nested_dict}")

# # حذف شهر از اطلاعات شخص اول
# del nested_dict["person1"]["city"]  
# print(f"Update 1: \n\t{nested_dict}")


# # حذف اطلاعات شخص چهارم
# del nested_dict["person4"]          
# print(f"Update 2: \n\t{nested_dict}")
