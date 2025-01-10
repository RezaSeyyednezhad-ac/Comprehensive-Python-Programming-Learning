# # datetime module in Python ماژول تاریخ و زمان در پایتون
# from datetime import datetime # وارد کردن ماژول و کلاس

# # datetime.now()
# now = datetime.now()
# print(now)  

# # -------------------------------------- # 

# # datetime module in Python ماژول تاریخ و زمان در پایتون
# from datetime import datetime # وارد کردن ماژول و کلاس

# # datetime.today()
# today = datetime.today()
# print(today)  

# # -------------------------------------- # 

# # datetime module in Python ماژول تاریخ و زمان در پایتون
# from datetime import datetime # وارد کردن ماژول و کلاس

# # تبدیل یک رشته تاریخ/زمان به یک شئ
# date_str = "2024-12-29 15:45"
# date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M")

# print(date_obj)  
# print(f"Type of date_str is {type(date_str)}")
# print(f"Type of date_obj is {type(date_obj)}")


# # -------------------------------------- # 

# # datetime module in Python ماژول تاریخ و زمان در پایتون
# from datetime import datetime # وارد کردن ماژول و کلاس

# now = datetime.now()
# formatted = now.strftime("%Y/%m/%d %H:%M:%S")
# # Y: year, m: month, d: day, H: hour, M: minute, S: second

# print(formatted)  
# print(f"type of now is: {type(now)}")
# print(f"type of formatted is: {type(formatted)}")

# # -------------------------------------- # 

# # datetime module in Python ماژول تاریخ و زمان در پایتون
# from datetime import datetime # وارد کردن ماژول و کلاس

# timestamp = 1937210700
# date_from_timestamp = datetime.fromtimestamp(timestamp)
# print(date_from_timestamp)  

# # -------------------------------------- # 

# # datetime module in Python ماژول تاریخ و زمان در پایتون
# from datetime import datetime, date, time # وارد کردن ماژول و کلاس

# d = date(2025, 1, 8)
# t = time(11, 35, 40)
# combined = datetime.combine(d, t)
# print(combined) 

# # -------------------------------------- # 

# # datetime module in Python ماژول تاریخ و زمان در پایتون
# from datetime import datetime # وارد کردن ماژول و کلاس

# now = datetime.now()
# print(f"Before Changing: {now}")
# new_time = now.replace(hour=20, minute=30) # تغییر دادن ساعت و دقیقه
# print(f"After Changing: {new_time}")  

# # -------------------------------------- # 

# # datetime module in Python ماژول تاریخ و زمان در پایتون
# from datetime import datetime # وارد کردن ماژول و کلاس

# now = datetime.now()
# print(f"Date Time: {now}")
# timestamp = now.timestamp()
# print(f"Unix Time: {timestamp}")  

