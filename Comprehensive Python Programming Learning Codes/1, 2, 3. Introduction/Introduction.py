# # Comment in Python

# # ** Single Line Comment **
# # print("Hello World")  کامنت تک خطی

# # ** Multiple Line Comment **
# """
# کامنت چند خطی
# Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
# sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
# Ut enim ad minim veniam, 
# quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
# Duis aute irure dolor in reprehenderit in voluptate velit esse. 
# Excepteur sint occaecat cupidatat non proident, 
# sunt in culpa qui officia deserunt mollit anim id est laborum.
# سلام
# به امید دیدار
# """

# -------------------------------------- #

# # تابع درونی print()
# # print(Object, sep="separator", end="end")
# # sep: 
# print("Hello", "World", 4 , 25, sep="-") # جداکننده با علامت(-)
# print("Hello", "World", 4 , 25, sep="*") # جداکننده با علامت(*)
# print("Hello", "World", 4 , 25, sep="#") # جداکننده با علامت(#)
# print("Hello", "World", 4 , 25, sep=" ") # جداکننده با علامت( )

# """
# 'Result in Terminal:' 

#     Hello-World-4-25
#     Hello*World*4*25
#     Hello#World#4#25
#     Hello World 4 25
# """
# -------------------------------------- #

# # تابع درونی print()
# # print(Object, sep="separator", end="end")
# # end: Default value of end is: \n (New Line)

# print("First Example ", end="***")  #  =>  New value of end is: "***"
# print("Second Example ", 4 , 25, end="#") # =>  New value of end is: "#"

# """
# New value of end is: "***"
# 'Result in Terminal:' 
#     First Example ***Second Example  4 25#
# """

# -------------------------------------- #

# #  ** F-Strings in Python **

# name = "Reza"
# age = 23
# score = 18.23

# print(f"My name is {name} and I am {age} years old.")
# print(f"I got a grade of {score} in math.")
# """
# 'Result in Terminal:'
#     My name is Reza and I am 23 years old.
#     I got a grade of 18.23 in math.
# """


# -------------------------------------- #

# # Logical Operator (and)

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# """
# 'Result in Terminal:'
#     True
#     False
#     False
#     False
# """

# Logical Operator (or)

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)
# """
# 'Result in Terminal:'
#     True
#     True
#     True
#     False
# """

import os

os.system('cls')
print("Hello World!")

