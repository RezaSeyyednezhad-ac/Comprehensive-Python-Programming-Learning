# Numpy in Python نامپای در پایتون
# Install numpy: نصب نامپای 
#           pip install numpy

# import numpy as np

# # ایجاد ماتریس صفر 3*3
# print(np.zeros((3,3)))

# # -------------------------------------- # 

# # Numpy in Python نامپای در پایتون
# # Install numpy: نصب نامپای 
# #           pip install numpy

# import numpy as np

# # # ایجاد ماتریس یک 3*3
# print(np.ones((3,3)))

# # -------------------------------------- # 

# # Numpy in Python نامپای در پایتون
# # Install numpy: نصب نامپای 
# #           pip install numpy

# import numpy as np

# # ایجاد ماتریس قطری 3*3
# print(np.eye(3))

# # -------------------------------------- # 

# # Numpy in Python نامپای در پایتون
# # Install numpy: نصب نامپای 
# #           pip install numpy

# import numpy as np

# # ایجاد ماتریس 3*3
# print(np.array([[1, 2, 3], [4, 5, 6]]))

# # -------------------------------------- # 

# # Numpy in Python نامپای در پایتون

# import numpy as np
# A = np.array([[1, 2, 3], [4, 5, 6]])
# B = np.array([[10, 20, 30], [40, 50, 60]])

# # عملیات جمع در ماتریس ها
# print(f"A + B = \n{A+B}")

# # عملیات تفریق در ماتریس ها
# print(f"A - B = \n{A-B}")

# # -------------------------------------- # 

# # Numpy in Python نامپای در پایتون

# import numpy as np

# a = np.array([[1, 0], [0, 1]])
# b = np.array([[4, 1], [2, 2]])

# # np.dot()
# print(np.dot(a, b))

# # -------------------------------------- # 

# # Numpy in Python نامپای در پایتون

# import numpy as np

# a = np.array([[4, 1], [2, 2]])
# print(f"Before: \n{a}")

# # transpose()
# print(f"After (transpose()): \n{np.transpose(a)}")

# # a.T
# print(f"After (a.T): \n{a.T}")

# # # -------------------------------------- # 

# # Numpy in Python نامپای در پایتون

# import numpy as np
# a = np.array([[4, 1], [2, 2]])
# print(f"Default Matrix: \n{a}")

# # معکوس ماتریس
# print(f"Invertible matrix: \n{np.linalg.inv(a)}")

# # -------------------------------------- # 

# # Numpy in Python نامپای در پایتون

# import numpy as np
# a = np.array([[4, 1], [2, 2]])
# print(f"Default Matrix: \n{a}")

# # دترمینال ماتریس
# print(f"Matrix Determinant: \n{np.linalg.det(a)}")

# # -------------------------------------- # 

# # Numpy in Python نامپای در پایتون

# import numpy as np
# a = np.array([[4, 1], [2, 5]])
# print(f"Default Matrix: \n{a}")

# # دسترسی به عناصر ماتریس
# # دسترسی به عنصر خاص از ماتریس
# print(f"a[0, 0]: {a[0,0]}")
# print(f"a[1, 1]: {a[1,1]}")
# print(f"a[1, 0]: {a[1,0]}")
# print(f"a[0, 1]: {a[0,1]}")

# # -------------------------------------- # 

# # Numpy in Python نامپای در پایتون

# import numpy as np
# a = np.array([[4, 1], [2, 5]])
# print(f"Default Matrix: \n{a}")

# # دسترسی به عناصر ماتریس
# # دسترسی به سطر یا ستون یک ماتریس
# # سطر اول
# print(f"a[0, :]: {a[0, :]}")
# # سطر دوم
# print(f"a[1, :]: {a[1, :]}")
# # ستون اول
# print(f"a[:, 0]: {a[:, 0]}")
# # ستون دوم
# print(f"a[:, 1]: {a[:, 1]}")

# # -------------------------------------- # 

# # Numpy in Python نامپای در پایتون

# import numpy as np
# a = np.array([[4, 1, 9], [2, 5, 2]])
# print(f"Default Matrix: \n{a}")

# # تغییر شکل ماتریس

# print(f"Reshape a: \n{a.reshape((3, 2))}")  # تغییر شکل ماتریس به ۳ سطر و ۲ ستون

# # -------------------------------------- # 

# # Numpy in Python نامپای در پایتون

# # Example 1. Create 1d and 2d array
# import numpy as np

# # آرایه یک‌بعدی
# array_1d = np.array([1, 2, 3, 4])
# print(f"1D array: \n{array_1d}") 
# # آرایه دوبعدی
# array_2d = np.array([[1, 2], [3, 4]])
# print(f"2D array: \n{array_2d}")

# # -------------------------------------- # 

# # Numpy in Python نامپای در پایتون

# # Example 2. Create Specia arrayl 
# import numpy as np

# # آرایه‌ای از صفرها
# zeros = np.zeros((2, 3))
# print(f"Zeros Array: \n{zeros}")

# # آرایه‌ای از یک‌ها
# ones = np.ones((3, 3))
# print(f"Ones Array: \n{ones}")

# # آرایه‌ای از اعداد متوالی
# sequence = np.arange(1, 10, 2)
# print(f"Sequence 2D array: \n{sequence}")

# # آرایه‌ای از اعداد بین دو مقدار
# linspace = np.linspace(0, 1, 5)
# print(f"Numbric Array between two number:\n{linspace}")  

# # -------------------------------------- # 

# # Numpy in Python نامپای در پایتون

# # Example 3. Get array shape, size and dimension
# import numpy as np

# array = np.array([[1, 2, 3], [4, 5, 6]])
# print(f"Shape: {array.shape}") 
# print(f"Size: {array.size}") 
# print(f"Dimension: {array.ndim}") 

# # -------------------------------------- # 

# # Numpy in Python نامپای در پایتون

# # Example 4.  obtain the addition, subtraction, multiplication, division, 
# #                     and square root operations of any array.

# import numpy as np
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# # آرایه ها
# print(f"a = {a}")
# print(f"b = {b}")

# # جمع و تفریق
# print(f"a + b = {a + b}")
# print(f"a - b = {a - b}")

# # ضرب و تقسیم
# print(f"a * b = {a * b}")
# print(f"a / b = {a / b}")

# # توان
# print(f"a**2 = {a**2}")
# print(f"b**2 = {b**2}")

# # -------------------------------------- # 

# Numpy in Python نامپای در پایتون

# # Example 5.  obtain the addition, avrage, maximum, minimum, 
# #                     and Standard deviation of 1D array.

# import numpy as np

# array = np.array([1, 2, 3, 4])
# print(f"array: {array}")
# print(f"Sum of array: {np.sum(array)}")       
# print(f"Average of array: {np.mean(array)}")       
# print(f"Max of array: {np.max(array)}")       
# print(f"Min of array: {np.min(array)}")   
# print(f"Standard deviation of array: {np.std(array)}")   
