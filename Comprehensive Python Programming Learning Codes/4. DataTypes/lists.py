# # Lists in Python (فهرست‌ها در پایتون )
# # Examples:

# List_Example_1 = [20, 65, 2000, 1, 56, 9, 896, 0, -632, -96345, -1, -1000000]

# List_Example_2 = ["Chevrolet", "Ford", "Dodge", "BMW", "Mercedes"]

# List_Example_3 = [20, "Red", 1364, 98536, 1, "Yellow", "2416", "21g"]

# List_Example_4 = ["Sky", "Green Earth", "This is a text.", "Is This Text?"]

# List_Example_5 = [[1, 2], ['red', 'blue', 'green'], [100], ["Samsung"]]

# List_Example_5 = [[200, 'red', 'blue'], ["Samsung", 23, 5, 634, 42]]

# # -------------------------------------- #

# # Lists in Python (فهرست‌ها در پایتون )
# # Len(list) 

# List_Example_1 = [20, 65, 2000, 1, 56, 9, 896, 0, -632, -96345, -1, -1000000]
# print(f"Length of List_Example_1 is {len(List_Example_1)}")

# List_Example_2 = [20, "Red", 1364, 98536, 1, "Yellow", "2416", "21g"]
# print(f"Length of List_Example_2 is {len(List_Example_2)}")

# List_Example_3 = [[1, 2], ['red', 'blue', 'green'], [100], ["Samsung"]]
# print(f"Length of List_Example_3 is {len(List_Example_3)}")

# List_Example_4 = [[200, 'red', 'blue'], ["Samsung", 23, 5, 634, 42]]
# print(f"Length of List_Example_4 is {len(List_Example_4)}")

# # -------------------------------------- #

# # Lists in Python (فهرست‌ها در پایتون )
# # دسترسی به یک عنصر خاص
# # Variable_Name = List_Name[index]

# List_Example_1 = [20, "Red", 1364, 98536, 1, "Yellow", "2416", "21g"]

# select_item_1364 = List_Example_1[2]
# print(select_item_1364)

# select_item_yellow = List_Example_1[5]
# print(select_item_yellow)

# # -------------------------------------- #

# # Lists in Python (فهرست‌ها در پایتون )
# # دسترسی به یک محدوده خاص از یک لیست
# # New_List_Name = List_Name[Start_Index:End_index:Step]

# List_Example_1 = [20, "Red", 1364, 98536, 1, "Yellow", "2416", "21g"]

# select_red_to_yellow = List_Example_1[1:6:2]
# print(f'select_red_to_yellow: {select_red_to_yellow}')

# # Select 20, 1364, 1, "2416"
# select_custom = List_Example_1[::2]
# print(f'select_custom: {select_custom}')

# # -------------------------------------- #

# # Lists in Python (فهرست‌ها در پایتون )
# # Change List Item/Items
# #       Change One Item of List
# #       Syntax:  List_Example[index] = new_Value

# Car_List = ["Chevrolet", "Ford", "Dodge", "BMW", "Mercedes"]

# # Before Changing
# print(f"Before: {Car_List}")

# Car_List[1] = "Mclaren"

# # After Changing
# print(f"After: {Car_List}")

# # -------------------------------------- #

# # Lists in Python (فهرست‌ها در پایتون )
# # Change List Item/Items
# #       Change many Items of List
# #       Syntax: List_Example[StartIndex:EndIndex:Step] = [new_Values]

# Car_List =  ["Chevrolet", "Ford", "Dodge", "BMW", "Mercedes"]
# print(f"Before: {Car_List}")
# Car_List[1:3] = ["McLaren", "Lamborghini"]
# print(f"After: {Car_List}")

# # -------------------------------------- #

# # Lists in Python (فهرست‌ها در پایتون )
# # Adding new Item/Items to List
# Car_List =  ["Chevrolet", "Ford", "Dodge", "BMW", "Mercedes"]

# # Add a new item to list by append() method
# Car_List.append("McLaren")
# print(f"Adding 'McLaren' in Car List by append():\n\t{Car_List}")

# # Add a new item to list by insert() method
# Car_List.insert(1, "Ferrari")
# print(f"Adding 'Ferrari' in Car List by insert():\n\t{Car_List}")

# # -------------------------------------- #

# # Lists in Python (فهرست‌ها در پایتون )
# # Adding new Items to List

# Car_List =  ["Chevrolet", "Ford", "Dodge", "BMW", "Mercedes"]

# # Add new items to list by extend() method
# New_Car_List = ["McLaren", "Ferrari"]
# Car_List.extend(New_Car_List) 
# #You can write like this: 
# #               Car_List.extend(["McLaren", "Ferrari"])

# print(f"Adding ['McLaren', 'Ferrari'] in Car List by extend(): \n\t{Car_List}")

# # -------------------------------------- #

# # Lists in Python (فهرست‌ها در پایتون )
# #  Remove Item/Items from List

# Car_List =  ["Chevrolet", "Ford", "Dodge", "BMW", "Mercedes"]
# print(f"Car List: \n\t{Car_List}")

# # remove() method
# Car_List.remove("Ford")
# print(f"Remove 'Ford' from Car List by remove(): \n\t{Car_List}")

# # pop() method
# Car_List.pop(2) # remove 'BMW'
# print(f"Remove 'BMW' from Car List by pop(): \n\t{Car_List}")

# # del keyword
# del Car_List[-1] # remove 'Mercedes'
# print(f"Remove 'Mercedes' from Car List by del keyword: \n\t{Car_List}")

# # -------------------------------------- #

# # Lists in Python (فهرست‌ها در پایتون )
# #  Remove all items from List

# Car_List = ['Chevrolet', 'Ford', 'Dodge', 'BMW', 'Mercedes']
# print(f"Car List: \n\t{Car_List}")

# # Remove all items by clear() method
# Car_List.clear()
# print(f"Remove all items from Car List by clear(): \n\t{Car_List}")

# # -------------------------------------- #

# # Lists in Python (فهرست‌ها در پایتون )
# # list Copy

# Car_List = ['Chevrolet', 'Ford', 'Dodge', 'BMW', 'Mercedes']
# print(f"Car List: \n\t{Car_List}")

# # by copy() method
# new_car_list_by_copy_method = Car_List.copy()
# print(f"new_car_list_by_copy_method: \n\t{new_car_list_by_copy_method}")

# # by build-in function
# new_car_list_by_build_in_function = list(Car_List)
# print(f"new_car_list_by_build_in_function: \n\t{new_car_list_by_build_in_function}")

# # -------------------------------------- #

# # Lists in Python (فهرست‌ها در پایتون )
# # Nested List

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 20], ['red', 'blue', 'green'], [100], ["Samsung"]]
# print(nested_list)

# # -------------------------------------- #

# # Lists in Python (فهرست‌ها در پایتون )
# # Access to nested list items

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(nested_list[0])      # دسترسی به اولین زیرلیست

# print(nested_list[1][2])   # دسترسی به عنصر سوم از زیرلیست دوم

# # -------------------------------------- #

# # Lists in Python (فهرست‌ها در پایتون )
# # Adding item/items to nested list

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(f"nested_list: \n\t{nested_list}")

# nested_list.append(1024) # اضافه کردن یک عنصر
# print(f"Adding One item to nested_list: \n\t{nested_list}")

# nested_list.append([10, 11, 12])  # اضافه کردن یک لیست 
# print(f"Adding One list to nested_list: \n\t{nested_list}")

# nested_list.extend([2048, 4096, 8192]) # اضافه کردن چند عنصر
# print(f"Adding many items to nested_list: \n\t{nested_list}")

# nested_list.extend([['red', 'yellow', 'green'], ['blue', 'gray', 'green']]) # اضافه کردن چند لیست
# print(f"Adding many lists to nested_list: \n\t{nested_list}")

# # -------------------------------------- #

# # Lists in Python (فهرست‌ها در پایتون )
# # remove item/items to nested list

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], 1024, [10, 11, 12], 2048, 4096, 8192]
# print(f"nested_list: \n\t{nested_list}")

# nested_list.remove(1024)
# print(f"Remove one item from nested_list using remove() method: \n\t{nested_list}")

# del nested_list[4]
# print(f"Remove one item from nested_list using index of item: \n\t{nested_list}")

# del nested_list[1][2]
# print(f"Remove one item from sub lists of nested_list using index of item: \n\t{nested_list}")

# # -------------------------------------- #

# Lists in Python (فهرست‌ها در پایتون )
# Merge Two List by for loop

first_list = ['Chevrolet', 'Ford', 'Dodge', 'BMW', 'Mercedes']
second_list = ["McLaren", "Ferrari"]
third_list = ["Nissan", "Porsche"]

print(f"first_list: {first_list}\nsecond_list: {second_list}")

# Using for loop to add second_list to first_list
for i in second_list:
    first_list.append(i)
print(f"merge two list by for loop: \n\t{first_list}\n")

# using extend() method to add third_list to first_list
first_list.extend(third_list)
print(f"merge two list by extend(): \n\t{first_list}")


# # -------------------------------------- #

# # Lists in Python (فهرست‌ها در پایتون )
# # Array VS List

# List = [100, 200, "Hello", "Bye", 536] # List

# Array = [20, 65, 2000, 1, 56, 9, 896, 0, -632, -96345, -1, -1000000] # Array

# Array_2 = ["Chevrolet", "Ford", "Dodge", "BMW", "Mercedes"] # Array