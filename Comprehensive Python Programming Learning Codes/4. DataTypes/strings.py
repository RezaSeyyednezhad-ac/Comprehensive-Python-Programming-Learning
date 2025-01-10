# # String in Python (رشته‌ها در پایتون)

# # String with single-quotation
# single_quotation_string = 'In the name of GOD'
# print(f"type of single_quotation_string is {type(single_quotation_string)}")

# # String with double-quotation
# double_quotation_string = "Hello, World!"
# print(f"type of double_quotation_string is {type(double_quotation_string)}")

# # String with triple-quotation
# triple_quotation_string = """
# In the name of GOD
# Hello, World!
# How are you?
# """
# print(f"type of triple_quotation_string is {type(triple_quotation_string)}")

# -------------------------------------- #

# # String in Python (رشته‌ها در پایتون)

# # Concentration in Python
# #     Syntax: string_1 + string_2 + ....
    
# string_1 = "Hello World!"
# string_2 = "Nice to meet you."
# string_3 = "Good Luck:)"

# string_sums = string_1 + " " + string_2 + " " + string_3
# print(f"Concentration Method: {string_sums}") 

# # Use F-string for concentration
# print(f"f-string Method: {string_1} {string_2} {string_3}")

# -------------------------------------- #

# # String in Python (رشته‌ها در پایتون)
# # Indexing in Python

# string_sample = "Hello, World!"
# myChar_1 = string_sample[0]
# myChar_2 = string_sample[1]
# myChar_3 = string_sample[2]
# myChar_4 = string_sample[-1] # => in "World!" extract "!"
# myChar_5 = string_sample[-2] # => in "World!" extract "d"
# myChar_6 = string_sample[-13] # => in "World!" extract "H"

# print(f"string_sample[0] of 'Hello, World!' is: {myChar_1}")
# print(f"string_sample[1] of 'Hello, World!' is: {myChar_2}")
# print(f"string_sample[2] of 'Hello, World!' is: {myChar_3}")
# print(f"string_sample[-1] of 'Hello, World!' is: {myChar_4}")
# print(f"string_sample[-2] of 'Hello, World!' is: {myChar_5}")
# print(f"string_sample[-13] of 'Hello, World!' is: {myChar_6}")

# -------------------------------------- #

# # String in Python (رشته‌ها در پایتون)
# # Slicing in Python

# string_sample_2 = "Hello, World! Nice to meet you."

# Hello_extract = string_sample_2[0:6]
# print(f"Extract 'Hello' from string_sample_2: {Hello_extract}")

# reverse_string_sample_2 = string_sample_2[::-1]
# print(f"Reverse string sample_2: {reverse_string_sample_2}")

# Meet_extract_and_reverse = string_sample_2[-6:-10:-1]
# print(f"Extract 'Meet' from string_sample_2 and reverse: {Meet_extract_and_reverse}")

# -------------------------------------- #

# # String in Python (رشته‌ها در پایتون)

# myString = "hello, and welcome to my world."

# # Capitalize()
# cap_string = myString.capitalize()
# print(f"Capitalize of myString is: {cap_string}")

# # Upper()
# upper_string = myString.upper()
# print(f"Upper of myString is: {upper_string}")

# # Lower()
# lower_string = myString.lower()
# print(f"Lower of myString is: {lower_string}")

# -------------------------------------- #

# # String in Python (رشته‌ها در پایتون)

# myString = "Hello, and welcome To python Tutorial."

# # Title()
# title_string = myString.title()
# print(f"Title method for myString: {title_string}")

# # Casefold()
# casefold_string = myString.casefold()
# print(f"Casefold method for myString: {casefold_string}")

# # Swapcase()
# swapcase_string = myString.swapcase()
# print(f"Swapcase method for myString: {swapcase_string}")

# -------------------------------------- #

# # String in Python (رشته‌ها در پایتون)
# # Strip()

# # Example 1
# String_example_1 = "   apples are delicious fruits that come in many different colors.  "
# new_String_example_1 = String_example_1.strip()
# print(f"Example 2: Before: {String_example_1}\nAfter: {new_String_example_1}")

# # Example 2 
# String_example_2 = "***apples are delicious fruits that come in many different colors.**"
# new_String_example_2 = String_example_2.strip("*") #Set Custom Character
# print(f"Example 2: Before: {String_example_2}\nAfter: {new_String_example_2}")

# -------------------------------------- #

# # String in Python (رشته‌ها در پایتون)
# # Replace(old value, new value, count)

# newString = """Apple is a sweet and delicious fruit that is very healthy. 
# Apple is also a good disease-fighter and we can eat it every day."""

# newString_1 = newString.replace('Apple', 'Orange')
# print(f"replace all 'Apple' to 'Orange':\n{newString_1}", end='\n\n')

# newString_2 = newString.replace('Apple', 'Orange', 1)
# print(f"replace first 'Apple' to 'Orange':\n{newString_2}")

# -------------------------------------- #

# # String in Python (رشته‌ها در پایتون)
# # Split()

# # Example 1: split the fruits
# fruits = "Apple,Orange,Banana,Pineapple,Cherry,Lemon"
# fruits_list = fruits.split(',')
# print(f"Before Splitting: {fruits}\nAfter Splitting: {fruits_list}", end='\n\n')

# # Example 2: split the Cars
# Cars = "Chevrolet*Dodge*Ford*BMW*Mercedes"
# Cars_list = Cars.split("*")
# print(f"Before Splitting: {Cars}\nAfter Splitting: {Cars_list}")

# -------------------------------------- #

# # String in Python (رشته‌ها در پایتون)
# # Find(value, start, end)

# newString = "Apples are delicious fruits."
# # Words: A p p l e s   a r e    d  e  l  i  c  i  o  u  s     f  r  u  i  t  s  .
# # Index: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 

# print(f"location of 'fruits' is: {newString.find("fruits")}" )
# print(f"location of 'Apples' is: {newString.find("Apples")}") 
# print(f"location of 'orange' is: {newString.find("orange")}") 


# -------------------------------------- #

# # String in Python (رشته‌ها در پایتون)
# # Index(value, start, end)

# newString = "Apples are delicious fruits."

# # Words: A p p l e s   a r e    d  e  l  i  c  i  o  u  s     f  r  u  i  t  s  .
# # Index: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 

# print(f"location of 'fruits' is: {newString.index("fruits")}")
# print(f"location of 'Apples' is: {newString.index("Apples")}") 
# print(f"location of 'orange' is: {newString.index("orange")}") 

# -------------------------------------- #

# # String in Python (رشته‌ها در پایتون)
# # find() vs index()

# new_string = "In the name of GOD. In GOD we trust."

# # Words: I n   t h e   n a m e     o  f     G  O  D  .  ...
# # Index: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ...

# print(f"location of 'GOD' is: {new_string.find("GOD", 0, 19)}")
# print(f"location of 'GOD' is: {new_string.find("Apple", 0, 19)}", end='\n\n')
# print(f"location of 'GOD' is: {new_string.index("GOD", 0, 19)}")
# print(f"location of 'GOD' is: {new_string.index("Apple", 0, 19)}")


# -------------------------------------- #

# Count(Value, Start Index, End Index)
# newString = """
# Apples are delicious fruits that come in many different colors and flavors.
# You can eat apples on their own as a snack, or use them in cooking.
# Eating apples regularly can help keep you healthy.
# """
# برای حالتی که از همه متن کلمه مورد نظر را پیدا میکند
# print(f"for 'apples' words: {newString.count('apples')}")
# print(f"for 'Apples' word: {newString.count('Apples')}")

# Count(Value, Start Index, End Index)
# newString = """Apples are delicious fruits that come in many different colors and flavors.
# You can eat apples on their own as a snack, or use them in cooking.
# Eating apples regularly can help keep you healthy.
# """
# برای حالت دوم که از یک ایندکسی تا یک ایندکس دیگر جستجو میکند
# Custom_Sentences = newString[0:75] # جمله اول از پاراگراف بالا
# print(Custom_Sentences)
# print(f"for 'Apples' words:{newString.count("Apples", 0, 75)}")
# print(f"for 'apples' words:{newString.count("apples", 0, 75)}")



# StartWith(value, start index, end index) & EndsWith(value, start index, end index)
# new_string = "In the name of GOD. In GOD we trust."

# StartWith(value, start index, end index)
# print(f"Is new_string Starts with 'In': {new_string.startswith('In')}") # True
# print(f"Is new_string Starts with 'GOD': {new_string.startswith('GOD')}") # False

# EndsWith(value, start index, end index)
# print(f"Is new_string Ends with 'trust': {new_string.endswith('trust.')}") # True
# print(f"Is new_string Ends with 'GOD': {new_string.endswith('GOD')}") # False




