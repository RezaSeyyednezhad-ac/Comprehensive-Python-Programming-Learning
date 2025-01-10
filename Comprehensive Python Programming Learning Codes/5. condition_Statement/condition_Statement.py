# # Condition Statement in Python (دستورات شرطی در پایتون)

# # First Syntax (Only if) ساختار اول: تعریف دستورات شرطی فقط با
# """
# if condition:
#     statement
# """

# x = 25
# if x%2 == 1:
#     print(f"x:{x} is Odd number")

# name = "Reza"
# if name == "ali":
#     print("Hello Ali")

# # -------------------------------------- # 

# # Condition Statement in Python (دستورات شرطی در پایتون)

# # Second Syntax (if/else) ساختار دوم: تعریف دستورات شرطی با
# """
# if condition:
#     statement
# else:
#     statement
# """

# random_number = 1254
# if random_number%2 == 0:
#     print(f"{random_number} is Even number.")
# else:
#     print(f"{random_number} is Odd number.")
    
# user_score = 5
# # if user score grater than 10, user pass else Reject
# if user_score > 10:
#     print("Pass.")
# else:
#     print("Reject.")

# # -------------------------------------- # 

# # Condition Statement in Python (دستورات شرطی در پایتون)

# # Third Syntax (if/elif/else) ساختار سوم: تعریف دستورات شرطی با
# # Two Condition دستورات شرطی با دو شرط

# user_score = 17

# if user_score >= 17:
#     print("Good Job.")
# elif 10 < user_score < 17:
#     print("Not Bad.")
# else:
#     print("It's Bad.")

# # -------------------------------------- # 

# # Condition Statement in Python (دستورات شرطی در پایتون)

# # Third Syntax (if/elif/else)  ساختار سوم: تعریف دستورات شرطی با
# # Grater than Two Condition دستورات شرطی با بیش از دو شرط

# user_color = "yellow"

# if user_color == "green":
#     print("First try: User color is green.")
# elif user_color == "red":
#     print("Second try: User color is red.")
# elif user_color == "black":
#     print("Third try: User color is black.")
# elif user_color == "white":
#     print("Fourth try: User color is white.")
# elif user_color == "yellow":
#     print("Fifth try: User color is yellow.")
# elif user_color == "blue":
#     print("Last try: User color is blue.")
# else:
#     print("Oh no, I can't guess color! :(")



# # -------------------------------------- # 

# # Condition Statement in Python (دستورات شرطی در پایتون)

# # عملگرهای مقایسه بین دو شرط
# a = 45
# b = 13
# if a == b:
#     print("a and b are equal.")
    
# if a != b:
#     print("a and b are NOT equal.")

# if a > b:
#     print("a is grather than b.")

# if a >= b:
#     print("a is greater than or equal to b.")

# if a < b:
#     print("a is less than b.")

# if a <= b:
#     print("a is less than or equal to b.")

# # -------------------------------------- # 

# # Condition Statement in Python (دستورات شرطی در پایتون)

# # And/Or in Condition Statement کلیدواژه هایی که بین دو شرط استفاده میشود
# name = "Reza"
# age = 23

# if name == "Reza" and age == 24:
#     print("By And")
#     print(f"name = 'Reza':{name == "Reza"}")
#     print("AND")
#     print(f"age = 24: {age == 24}")
#     print(f"Result is {name == "Reza" and age == 24}")
    
# if name == "Reza" or age == 24:
#     print("By Or")
#     print(f"name = 'Reza':{name == "Reza"}")
#     print("OR")
#     print(f"age = 24: {age == 24}")
#     print(f"Result is {name == "Reza" or age == 24}")
    
# # -------------------------------------- # 

# # Condition Statement in Python (دستورات شرطی در پایتون)

# # in keyword in condition statement (بررسی وجود داشتن یا نداشتن با استفاده از کلیدواژه in)
# colors_list = ["red", "green", "blue", "black", "white"]

# if "yellow" in colors_list:
#     print("yellow is exist.")
# else:
#     print("yellow is NOT exist.")


# if 'blue' in colors_list:
#     print("blue is exist.")
# else:
#     print("blue is NOT exist.")

# # -------------------------------------- #

# # Condition Statement in Python (دستورات شرطی در پایتون)
# # not keyword in condition statement (استفاده از کلیدواژه جهت ضد کردن جمله )
# colors_list = ["red", "green", "yellow", "orange", "white"]

# if "yellow" not in colors_list:
#     print("yellow is NOT exist.")
# else:
#     print("yellow is exist.")


# if 'blue' not in colors_list:
#     print("blue is NOT exist.")
# else:
#     print("blue is exist.")

# # -------------------------------------- # 

# # Condition Statement in Python (دستورات شرطی در پایتون)

# # Nested if دستورات شرطی تو در تو
# # Buy Car
# user_age_1 = 24
# user_certificate = True
# if user_age_1 >= 18:
#     if user_certificate == True:
#         print("You Can Buy Car. :)")
#     else:
#         print("You Don't Have Certificate. So You Can't Buy Car. :(")
# else:
#     print("Under legal age! :(")

# # -------------------------------------- # 

# # Condition Statement in Python (دستورات شرطی در پایتون)

# # Nested if دستورات شرطی تو در تو
# # Buy Car
# user_age_2 = 15
# user_certificate = True
# if user_age_2 >= 18:
#     if user_certificate == True:
#         print("You Can Buy Car. :)")
#     else:
#         print("You Don't Have Certificate. So You Can't Buy Car. :(")
# else:
#     print("Under legal age! :(")
    
# # -------------------------------------- # 

# # Condition Statement in Python (دستورات شرطی در پایتون)

# # Nested if دستورات شرطی تو در تو
# # Buy Car
# user_age_3 = 25
# user_certificate = False
# if user_age_3 >= 18:
#     if user_certificate == True:
#         print("You Can Buy Car. :)")
#     else:
#         print("You Don't Have Certificate. So You Can't Buy Car. :(")
# else:
#     print("Under legal age! :(")