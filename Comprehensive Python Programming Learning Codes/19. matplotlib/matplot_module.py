# # Matplotlib in Python 
# # Install process: فرایند نصب  
# #           pip install matplotlib

# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.plot(x, y, label='Linear Relationship', color='blue', marker='o')
# plt.title('Line Plot Example')  # عنوان نمودار
# plt.xlabel('X-axis')  # برچسب محور X
# plt.ylabel('Y-axis')  # برچسب محور Y
# plt.legend()  # اضافه کردن راهنما
# plt.grid(True)  # نمایش خطوط شبکه
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 

# import matplotlib.pyplot as plt

# categories = ['A', 'B', 'C', 'D']
# values = [10, 15, 7, 12]

# plt.bar(categories, values, color='green')
# plt.title('Bar Plot Example')
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 
# import matplotlib.pyplot as plt

# labels = ['Category A', 'Category B', 'Category C', 'Category D']
# sizes = [25, 35, 20, 20]
# explode = (0, 0.1, 0, 0)  # برجسته کردن بخش دوم

# plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode, startangle=90)
# plt.title('Pie Chart Example')
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.random.rand(50)
# y = np.random.rand(50)

# plt.scatter(x, y, color='red', alpha=0.7)
# plt.title('Scatter Plot Example')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 

# import matplotlib.pyplot as plt
# data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5]

# plt.hist(data, bins=5, color='purple', edgecolor='black')
# plt.title('Histogram Example')
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y1 = [1, 4, 9, 16, 25]
# y2 = [2, 4, 6, 8, 10]

# plt.subplot(1, 2, 1)  # یک ردیف، دو ستون، نمودار اول
# plt.plot(x, y1, color='blue')
# plt.title('Subplot 1')

# plt.subplot(1, 2, 2)  # یک ردیف، دو ستون، نمودار دوم
# plt.plot(x, y2, color='green')
# plt.title('Subplot 2')

# plt.tight_layout()  # تنظیم فاصله‌ها
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 

# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
# z = [1, 3, 5, 7, 9]

# ax.plot(x, y, z, label='3D Line')
# ax.set_title('3D Plot Example')
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_zlabel('Z-axis')
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 

# import matplotlib.pyplot as plt
# import numpy as np

# # داده‌های نمونه
# x = np.logspace(0.1, 2, 100)  # تولید داده‌های لگاریتمی
# y = x**2  # تابع y = x^2

# # رسم نمودار log-log
# plt.loglog(x, y, label='y = x^2', color='blue')

# # افزودن برچسب‌ها و عنوان
# plt.xlabel('X-axis (log scale)')
# plt.ylabel('Y-axis (log scale)')
# plt.title('Log-Log Plot Example')
# plt.legend()

# # نمایش نمودار
# plt.grid(True, which="both", linestyle="--")
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 

# import matplotlib.pyplot as plt
# import numpy as np

# # داده‌های نمونه
# x = np.logspace(0.1, 2, 100)  # تولید داده‌های لگاریتمی
# y = x**2  # تابع y = x^2

# # تغییر مقیاس محورها به صورت دستی
# plt.plot(x, y, label='y = x^2', color='red')
# plt.xscale('log')
# plt.yscale('log')

# # افزودن جزئیات
# plt.xlabel('X-axis (log scale)')
# plt.ylabel('Y-axis (log scale)')
# plt.title('Log-Log Plot with Manual Scaling')
# plt.legend()

# # نمایش نمودار
# plt.grid(True, which="both", linestyle="--")
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 

# import matplotlib.pyplot as plt
# import numpy as np

# # داده‌های نمونه
# x = np.logspace(0.1, 2, 100)  # تولید داده‌های لگاریتمی

# # داده‌های چند رابطه
# y1 = x**2
# y2 = x**3

# # رسم چند نمودار
# plt.loglog(x, y1, label='y = x^2', color='blue')
# plt.loglog(x, y2, label='y = x^3', color='green')

# # افزودن جزئیات
# plt.xlabel('X-axis (log scale)')
# plt.ylabel('Y-axis (log scale)')
# plt.title('Multiple Log-Log Plots')
# plt.legend()

# # نمایش نمودار
# plt.grid(True, which="both", linestyle="--")
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 

# import matplotlib.pyplot as plt
# import numpy as np

# # داده‌های نمونه
# x = np.logspace(0.1, 2, 100)  # مقادیر لگاریتمی برای محور x
# y = x**2  # تابع y = x^2

# # رسم نمودار Semi-log-x
# plt.semilogx(x, y, label='y = x^2', color='blue')

# # افزودن جزئیات
# plt.xlabel('X-axis (log scale)')
# plt.ylabel('Y-axis (linear scale)')
# plt.title('Semi-log-x Plot')
# plt.legend()
# plt.grid(True, which="both", linestyle="--")
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 

# import matplotlib.pyplot as plt
# import numpy as np

# # داده‌های نمونه
# x = np.linspace(1, 10, 100)  # مقادیر خطی برای محور x

# y = np.exp(x)  # تابع y = e^x

# # رسم نمودار Semi-log-y
# plt.semilogy(x, y, label='y = e^x', color='green')

# # افزودن جزئیات
# plt.xlabel('X-axis (linear scale)')
# plt.ylabel('Y-axis (log scale)')
# plt.title('Semi-log-y Plot')
# plt.legend()
# plt.grid(True, which="both", linestyle="--")
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 

# import matplotlib.pyplot as plt
# import numpy as np

# # داده‌های نمونه
# x = np.logspace(0.1, 2, 100)
# y1 = x**2
# y2 = x**3

# # رسم دو نمودار Semi-log
# plt.semilogx(x, y1, label='y = x^2', color='blue')
# plt.semilogx(x, y2, label='y = x^3', color='red')

# # افزودن جزئیات
# plt.xlabel('X-axis (log scale)')
# plt.ylabel('Y-axis (linear scale)')
# plt.title('Multiple Semi-log-x Plots')
# plt.legend()
# plt.grid(True, which="both", linestyle="--")
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 

# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.plot(x, y)
# plt.xlabel('Time (s)', fontsize=12, color='blue')  # برچسب محور افقی
# plt.ylabel('Distance (m)', fontsize=12, color='green')  # برچسب محور عمودی
# plt.title('Motion Analysis')  # عنوان نمودار
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.plot(x, y)
# plt.xlabel('Time (s)', fontsize=12, color='blue')  # برچسب محور افقی
# plt.ylabel('Distance (m)', fontsize=12, color='green')  # برچسب محور عمودی
# plt.title('Motion Analysis')  # عنوان نمودار
# plt.xlim(0, 6)  # محدوده محور X
# plt.ylim(0, 12)  # محدوده محور Y
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.plot(x, y)
# plt.grid(True, linestyle='--', color='gray', alpha=0.7)
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# ticks_x = [1, 2, 3, 4, 5]
# labels_x = ['One', 'Two', 'Three', 'Four', 'Five']

# ticks_y = [2, 4, 6, 8, 10]
# labels_y = ['Low', 'Medium', 'High', 'Higher', 'Highest']

# plt.plot(x, y)
# plt.xticks(ticks_x, labels_x)  # تغییر مقادیر محور X
# plt.yticks(ticks_y, labels_y)  # تغییر مقادیر محور Y
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.plot(x, y)
# plt.xticks(rotation=45)  # چرخش برچسب‌های محور X
# plt.yticks(rotation=90)  # چرخش برچسب‌های محور Y
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.plot(x, y)
# plt.axhline(y=6, color='red', linestyle='--')  # خط افقی
# plt.axvline(x=3, color='blue', linestyle='--')  # خط عمودی
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.set_xlabel('Time (s)')
# ax.set_ylabel('Distance (m)')
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y1 = [1, 4, 9, 16, 25]
# y2 = [2, 4, 6, 8, 10]

# plt.subplot(1, 2, 1)  # یک ردیف، دو ستون، نمودار اول
# plt.plot(x, y1, color='blue')
# plt.title('Plot 1')

# plt.subplot(1, 2, 2)  # یک ردیف، دو ستون، نمودار دوم
# plt.plot(x, y2, color='green')
# plt.title('Plot 2')

# plt.tight_layout()  # تنظیم فاصله‌ها بین نمودارها
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y1 = [1, 4, 9, 16, 25]
# y2 = [2, 4, 6, 8, 10]

# plt.subplot(2, 2, 1)  # دو ردیف، دو ستون، نمودار اول
# plt.plot(x, y1, color='red')
# plt.title('Plot 1')

# plt.subplot(2, 2, 2)  # دو ردیف، دو ستون، نمودار دوم
# plt.plot(x, y2, color='blue')
# plt.title('Plot 2')

# plt.subplot(2, 2, 3)  # دو ردیف، دو ستون، نمودار سوم
# plt.bar(x, y1, color='purple')
# plt.title('Plot 3')

# plt.subplot(2, 2, 4)  # دو ردیف، دو ستون، نمودار چهارم
# plt.scatter(x, y2, color='green')
# plt.title('Plot 4')

# plt.tight_layout()  # تنظیم خودکار فاصله‌ها
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y1 = [1, 4, 9, 16, 25]
# y2 = [2, 4, 6, 8, 10]

# fig, axes = plt.subplots(2, 2, figsize=(8, 6))  # دو ردیف، دو ستون

# axes[0, 0].plot(x, y1, color='red')
# axes[0, 0].set_title('Plot 1')

# axes[0, 1].bar(x, y2, color='blue')
# axes[0, 1].set_title('Plot 2')

# axes[1, 0].scatter(x, y1, color='green')
# axes[1, 0].set_title('Plot 3')

# axes[1, 1].plot(x, y2, linestyle='--', color='purple')
# axes[1, 1].set_title('Plot 4')

# plt.tight_layout()
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 
# import matplotlib.pyplot as plt
# import numpy as np

# data = np.random.randn(1000)  # تولید داده‌های تصادفی
# plt.hist(data, bins=20, color='blue', alpha=0.7, edgecolor='black')
# plt.title('Histogram Example')
# plt.xlabel('Bins')
# plt.ylabel('Frequency')
# plt.show()

# # -------------------------------------- # 

# # Matplotlib in Python 
# import matplotlib.pyplot as plt

# categories = ['A', 'B', 'C', 'D']
# values = [10, 15, 7, 12]

# plt.bar(categories, values, color='orange', alpha=0.8, edgecolor='black')
# plt.title('Bar Chart Example')
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.show()

# # -------------------------------------- # 

# Matplotlib in Python 
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 12]

plt.subplot(1, 2, 1)  # رسم هیستوگرام
plt.hist(data, bins=20, color='blue', alpha=0.7, edgecolor='black')
plt.title('Histogram')

plt.subplot(1, 2, 2)  # رسم نمودار میله‌ای
plt.bar(categories, values, color='orange', alpha=0.8, edgecolor='black')
plt.title('Bar Chart')

plt.tight_layout()
plt.show()
