# # Sets in Python (مجموعه‌ها در پایتون)
# # Create Set (روش ایجاد مجموعه)

# # First Meyhod:  {} استفاده از 
# set_example_1 = {"1", "2", 1, 2, 3, 4}

# print(f"First Way is {set_example_1}")
# print(f"type of set_example_1: {type(set_example_1)}\n\n")

# # Second Method: استفاده از تابع داخلی
# set_example_2 = set(("1", "2", 1, 2, 3, 4))

# print(f"Second Way is {set_example_2}")
# print(f"type of set_example_2: {type(set_example_2)}")

# -------------------------------------- #

# # Sets in Python (مجموعه‌ها در پایتون)
# # داده‌هایی که می‌توان در داخل مجموعه‌ها استفاده کرد

# set_example_3 = {"Reza", "Red", "Corvette", "1", "-0.4"} # Strings in Set
# print(f"set_example_3: {set_example_3} and Type of set_example_3 is {type(set_example_3)}")

# set_example_4 = {1, 2, 6, 8, 0.5, -523, 510.249, -7.8} # Numbers in Set
# print(f"set_example_4: {set_example_4} and Type of set_example_4 is {type(set_example_4)}")

# set_example_5 = {True, False} # Boolean in Set
# print(f"set_example_5: {set_example_5} and Type of set_example_5 is {type(set_example_5)}")

# set_example_6 = {"Reza", False, 23, 188.8, "Yellow", "1"} # 
# print(f"set_example_6: {set_example_6} and Type of set_example_6 is {type(set_example_6)}")

# # -------------------------------------- #

# # Sets in Python (مجموعه‌ها در پایتون)
# # Length of Sets بدست آوردن اعداد عناصر مجموعه

# set_example_7 = {1, 2, 6, 8, 0.5, -523, 510.249, -7.8}
# print(f"length of {set_example_7} is {len(set_example_7)}")

# set_example_8 = {}
# print(f"length of {set_example_8} is {len(set_example_8)}")

# set_example_9 = {"Reza", False, 23, 188.8, "Yellow", "1"}
# print(f"length of {set_example_9} is {len(set_example_9)}")

# set_example_10 = {True}
# print(f"length of {set_example_10} is {len(set_example_10)}")


# # -------------------------------------- #

# # Sets in Python (مجموعه‌ها در پایتون)
# # Is Exist or NOT ??? عنصر در مجموعه وجود دارد یا نه؟؟؟

# set_example_11 = {"Reza", False, 23, 188.8, "Yellow", "1"}

# print(f"Is 'Blue' in set_example_11: {'Blue' in set_example_11}")

# print(f"Is '1' in set_example_11: {'1' in set_example_11}")

# print(f"Is 'True' in set_example_11: {True in set_example_11}")

# print(f"Is 'Reza' in set_example_11: {'Reza' in set_example_11}")

# print(f"Is 23 in set_example_11: {23 in set_example_11}")

# # -------------------------------------- #

# Sets in Python (مجموعه‌ها در پایتون)
# Add element/elements into Set افزودن یک یا چند عنصر به مجموعه

# set_example_12 = {"Reza"}
# print(f"Before Add: {set_example_12}")

# # Add one element
# set_example_12.add("Mohammad")
# print(f"After add one Element: {set_example_12}")

# # Add many elements
# set_example_12.update(['Abolfazl', 'Mahdi', 'Ali'])
# print(f"After add many elements: {set_example_12}")

# # -------------------------------------- #

# # Sets in Python (مجموعه‌ها در پایتون)
# # Remove one element from Set حذف یک عنصر از مجموعه

# set_example_13 = {'Abolfazl', 'Reza', 'Ali', 'Mahdi', 'Mohammad', 'Hossein', 'Amir'}
# # print(f"Before Removing: {set_example_13}")

# # Remove by discard method
# set_example_13.discard('Ali')
# print(f"Remove 'Ali' by discard method: {set_example_13}")

# # Remove by remove method
# set_example_13.remove('Hossein')
# print(f"Remove 'Hossein' by remove method: {set_example_13}")

# # Remove by pop method
# set_example_13.pop()
# print(f"Remove Random element by pop method: {set_example_13}")

# # -------------------------------------- #

# # Sets in Python (مجموعه‌ها در پایتون)
# # Remove all elements from Set حذف تمامی عناصر یک مجموعه

# # remove by clear method
# set_example_14 = {'Abolfazl', 'Reza', 'Ali', 'Mahdi', 'Mohammad', 'Hossein', 'Amir'}
# print(f"Before Removing: {set_example_14}")

# set_example_14.clear()
# print(f"After Removing: {set_example_14}")

# # -------------------------------------- #

# # Sets in Python (مجموعه‌ها در پایتون)

# #  union and update methods
# set_example_15 = {'Abolfazl', 'Reza'}
# adding_set_1 = set(('Ali', 'Mahdi', 'Mohammad'))
# adding_set_2 = {'Hossein', 'Amir'}
# print(f"Before adding: {set_example_15}\n")

# # union Method 
# myNewSet = set_example_15.union(adding_set_1)
# print(f"adding by union method: {myNewSet}\n")

# # update method
# set_example_15.update(adding_set_2)
# print(f"adding by update method: {set_example_15}")

# # -------------------------------------- #

# # Sets in Python (مجموعه‌ها در پایتون)

# # intersection and difference and symmetric_difference methods
# set_example_16 = {'Abolfazl', 'Reza', 'Ali', 'Mahdi', 'Mohammad'}
# set_example_17 = {'Hossein', 'Amir', 'Mahdi', 'Reza', 'Ali'}
# print(f"Default Sets:\n\t set Example 16: {set_example_16}\n\t set Example 17: {set_example_17}\n\n")
# # intersection method
# intersection_result = set_example_16.intersection(set_example_17)
# print(f"intersection of set_example_16 and set_example_17 is {intersection_result}\n")

# # difference method
# difference_result = set_example_16.difference(set_example_17)
# print(f"difference of set_example_16 and set_example_17 is {difference_result}\n")

# # symmetric_difference methods
# symmetric_difference_result = set_example_16.symmetric_difference(set_example_17)
# print(f"symmetric_difference of set_example_16 and set_example_17 is {symmetric_difference_result}")

# # -------------------------------------- #

# # Sets in Python (مجموعه‌ها در پایتون)

# set_example_18 = {'Abolfazl', 'Reza'}
# set_example_19 = {'Mahdi', 'Reza', 'Ali'}
# set_example_20 = {'Reza', 'Hossein', 'Amir'}
# set_example_21 = {'Hossein', 'Reza', 'Ali'}

# # union = |
# union_result = set_example_18 | set_example_19 | set_example_20 | set_example_21
# print(f"Result of union is {union_result}")

# # intersection = &
# intersection_result = set_example_18 & set_example_19 & set_example_20 & set_example_21
# print(f"Result of intersection is {intersection_result}")

# # -------------------------------------- #

# # Sets in Python (مجموعه‌ها در پایتون)

# set_example_18 = {'Abolfazl', 'Reza'}
# set_example_19 = {'Mahdi', 'Reza', 'Ali'}
# set_example_20 = {'Reza', 'Hossein', 'Amir'}
# set_example_21 = {'Hossein', 'Reza', 'Ali'}

# # difference = -
# difference_result = set_example_18 - set_example_19 - set_example_20 - set_example_21
# print(f"Result of difference is {difference_result}")

# # symmetric_difference = ^
# symmetric_difference_result = set_example_18 ^ set_example_19 ^ set_example_20 ^ set_example_21
# print(f"Result of symmetric_difference is {symmetric_difference_result}")

# # -------------------------------------- #

# Sets in Python (مجموعه‌ها در پایتون)

# True = 1
set_example_22 = {True, 1}
print(f"Result: {set_example_22}")

# False = 0
set_example_23 = {False, 0}
print(f"Result: {set_example_23}")

# Combination
set_example_24 = {1, False, 0, True}
print(f"Result: {set_example_24}")