# # Tuples in Python (تاپل در پایتون)
# # روش‌های ایجاد تاپل

# # first method: using ()
# create_tuple_1 = ("Reza", "Mahdi", "Mohammad", "Ali")
# print(f"Create tuple using (): \n\t{create_tuple_1}")
# print(f"Type of create_tuple_1 is: \n\t{type(create_tuple_1)}")


# # Second Method: use tuple build-in function
# create_tuple_2 = tuple(("Reza", "Ali", "Mohammad", "Mahdi"))
# print(f"Create tuple using tuple() build-in function : \n\t{create_tuple_2}")
# print(f"Type of create_tuple_2 is: \n\t{type(create_tuple_2)}")

# -------------------------------------- #

# Tuples in Python (تاپل در پایتون)
# داده‌هایی که می‌توان در تاپل قرار داد

# tuple_example_1 = (
#     "Reza", 
#     23, 188.65, 10+5j, 
#     ["Yellow", "Green", "Red", "Orange", [1, 2, 3, 4, 5]], 
#     ('chevrolet', 'Dodge', 'Ford'),
#     True, False,
#     {"Abolfazl", "Amir", "Ehsan"},
#     {
#         "book": "Python",
#         "level": "Intermediate",
#         "rating": [5, 4.5, 4, 5, 4]
#     }
# )
# print(tuple_example_1)

# -------------------------------------- #

# # Tuples in Python (تاپل در پایتون)
# # Length of Tuple

# tuple_example_1 = (
#     "Yellow", 
#     "Green", 
#     "Red", 
#     "Orange", 
#     True, 
#     1253, 
#     52.364958, 
#     ('chevrolet', 'Dodge', 'Ford')
# )
# print(f"Elements of tuple_example_1 is: \n\t{tuple_example_1}")
# print(f"Length of tuple_example_1 is: {len(tuple_example_1)}")

# -------------------------------------- #

# # Tuples in Python (تاپل در پایتون)
# # Tuple With ONE Element

# # This is Tuple
# tuple_example_2 = ("Yellow",)
# print(f"tuple_example_2: {tuple_example_2}")
# print(f"Type of tuple_example_2 is {type(tuple_example_2)}") # tuple

# # This is NOT Tuple
# tuple_example_3 = ("Yellow")
# print(f"tuple_example_3: {tuple_example_3}")
# print(f"Type of tuple_example_3 is {type(tuple_example_3)}") # string

# -------------------------------------- #

# # Tuples in Python (تاپل در پایتون)
# # Access The Tuple Elements => variable = tuple_name[index]

# tuple_example_4 = (
#     "Reza", 
#     23, 
#     188.65, 
#     ["Yellow", "Green", "Red", "Orange"], 
#     ('chevrolet', 'Dodge', 'Ford'),
#     True
# )
# print(f"Main Tuple: \n\t{tuple_example_4}")

# # Extract list from tuple_example_4
# print(f"List extract from tuple_example_4: \n\t{tuple_example_4[3]}")

# # Extract float number from tuple_example_4
# print(f"Float number extract from tuple_example_4: \n\t{tuple_example_4[2]}")

# -------------------------------------- #

# # Tuples in Python (تاپل در پایتون)
# # Negative Index in Tuples
# tuple_example_5 = (
#     "Yellow", 
#     ("Green",), 
#     True, 
#     1253, 
#     52.364958, 
#     ('chevrolet', 'Dodge', 'Ford')
# )
# print(f"Main Tuple: \n\t{tuple_example_5}")

# # Extract last tuple from tuple_example_5
# last_item_of_tuple_example_5 = tuple_example_5[-1]
# print(f"Last item of tuple_example_5 (tuple_example_5[-1]) is: \n\t{last_item_of_tuple_example_5}")

# # Extract Int Number from tuple_example_5
# myIntNumber = tuple_example_5[-3]
# print(f"Int Number of tuple_example_5 (tuple_example_5[-3]) is: \n\t{myIntNumber}")

# -------------------------------------- #

# # Tuples in Python (تاپل در پایتون)
# # Access Range of Tuple Elements
# tuple_example_6 = (
#     "Red", 
#     "Green", 
#     True, 
#     5639, 
#     52.3649, 
#     False
# )
# print(f"Main Tuple: \n\t{tuple_example_6}")

# # Extract from "Green" to 52.3649 
# extract_range_of_tuple = tuple_example_6[1:5]
# print(f"Extract data is: \n\t{extract_range_of_tuple}") 
# print(f"Type of extract data is: {type(extract_range_of_tuple)}")

# -------------------------------------- #

# # Tuples in Python (تاپل در پایتون)
# # Is Exist Or NOT ??? (بررسی وجود داشتن یک عنصر داخل تاپل)

# tuple_example_7 = tuple(("Reza", "Ali", "Mohammad", "Mahdi", "Amir"))

# print(f"tuple_example_7: \n\t{tuple_example_7}")

# print(f"Is 'Reza' on the tuple_example_7: {"Reza" in tuple_example_7}") # True

# print(f"Is 'Zahra' on the tuple_example_7: {"Zahra" in tuple_example_7}") # False

# print(f"Is 'ali' on the tuple_example_7: {"ali" in tuple_example_7}") # False

# print(f"Is 'Ehsan' on the tuple_example_7: {"Ehsan" in tuple_example_7}") # False

# print(f"Is 'Mohammad' on the tuple_example_7: {"Mohammad" in tuple_example_7}") # True

# -------------------------------------- #

# # Tuples in Python (تاپل در پایتون)
# # Change Element of Tuples (تغییر عناصر تاپل)

# # First Method: Convert Tuple to List
# tuple_example_8 = ("Yellow", "Green", "Red", "Orange")
# print(f"1. tuple_example_8: \n\t{tuple_example_8}")

# # Convert tuple to list 
# tuple_to_list = list(tuple_example_8)
# print(f"2. Convert Tuple To List: \n\t{tuple_to_list}")

# # Now You Can Change  
# tuple_to_list[1] = "Blue"
# print(f"3. Change Time (Blue instead of Green): \n\t{tuple_to_list}")

# # After Change, Convert list to tuple
# list_to_tuple = tuple(tuple_to_list)
# print(f"4. Convert list to tuple: \n\t{list_to_tuple}")

# -------------------------------------- #

# # Tuples in Python (تاپل در پایتون)
# # Change Element of Tuples (تغییر عناصر تاپل)

# # Second Method: use addition assignment(+=)
# tuple_example_9 = ("Yellow", "Green", "Red", "Orange")
# print(f'Before Adding: {tuple_example_9}')

# another_tuple = ("Blue",)
# tuple_example_9 += another_tuple
# print(f'After Adding: {tuple_example_9}')
