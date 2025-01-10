# # SymPy in Python ماژول سیمپای در پایتون
# # Install sympy: نصب سیمپای 
# #           pip install sympy

# from sympy import symbols, simplify

# x = symbols('x')
# expr = (x**2 + 2*x + 1)/(x + 1)
# print(f"Before = {expr}")

# # ساده سازی عبارت جبری
# print(f"After = {simplify(expr) }")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون
# # Install sympy: نصب سیمپای 
# #           pip install sympy

# from sympy import symbols, expand

# x = symbols('x')
# expr = (x + 1)**2
# print(f"Before = {expr}")

# # گسترش عبارت جبری
# print(f"After = {expand(expr) }")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون

# from sympy import symbols, limit
# x = symbols('x')
# expr = (x**2 - 1) / (x - 1)
# print(f"Equation: {expr}")

# # محاسبه حد تابع
# result = limit(expr, x, 1)
# print(f"limit of equation of  x as x approaches 1 equals: {result}")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون

# from sympy import symbols, limit
# x = symbols('x')
# expr = 1 / x
# print(f"Equation: {expr}")

# # محاسبه حد تابع
# result = limit(expr, x, float('inf'))
# print(f"limit of equation of  x as x approaches infinity equals: {result}")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون

# from sympy import symbols, limit
# x = symbols('x')
# expr = 1 / x
# print(f"Equation: {expr}")

# # One-sided limit
# # محاسبه حد یک طرفه تابع
# result = limit(expr, x, 0, dir='+')
# print(f"limit of equation of  x as x approaches a 'from the right': {result}")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون

# from sympy import symbols, limit
# x = symbols('x')
# expr = 1 / x
# print(f"Equation: {expr}")

# # One-sided limit
# # محاسبه حد یک طرفه تابع
# result = limit(expr, x, 0, dir='-')
# print(f"limit of equation of  x as x approaches a 'from the left': {result}")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون

# from sympy import symbols, limit, sin
# x = symbols('x')
# expr = sin(x)/x
# print(f"Equation: {expr}")

# # محاسبه حد توابع مثلثاتی
# result = limit(expr, x, 0)
# print(f"limit of equation of  x as x approaches 0 equals: {result}")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون

# from sympy import symbols, limit, sin
# x = symbols('x')
# expr = 1/(x-1)
# print(f"Equation: {expr}")

# # حد در نقاط ناپیوسته
# left_limit = limit(expr, x, 1, dir='-')  # حد از چپ
# right_limit = limit(expr, x, 1, dir='+')  # حد از راست

# print(f"limit of equation of x as x approaches 1 'from the right': {left_limit}")
# print(f"limit of equation of x as x approaches 1 'from the left': {right_limit}")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون

# from sympy import symbols, diff
# x = symbols('x')
# expr = x**2
# print(f"Equation: {expr}")

# # محاسبه مشتق اول
# print(f"Differntial of {expr} is: \n\t{diff(expr, x)}")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون

# from sympy import symbols, diff
# x = symbols('x')
# expr = x**3
# print(f"Equation: {expr}")

# # محاسبه مشتق دوم
# print(f"Differntial of {expr} is: \n\t{diff(expr, x, 2)}")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون

# from sympy import symbols, diff
# x = symbols('x')
# y = symbols('y')
# expr = x**2 + y**2
# print(f"Equation: {expr}")

# partial_x = diff(expr, x)  # نسبت به x
# partial_y = diff(expr, y)  # نسبت به y

# # محاسبه مشتق توابع چند متغیره
# print(f"Differntial of partial_x is: \t{partial_x}")
# print(f"Differntial of partial_y is: \t{partial_y}")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون

# from sympy import symbols, diff, sin

# x = symbols('x')
# expr = sin(x)
# print(f"Equation: {expr}")

# # محاسبه مشتق توابع مثلثاتی
# result = diff(expr, x)
# print(result) 

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون

# from sympy import symbols, diff, sin

# x = symbols('x')
# expr = sin(x**2)
# print(f"Equation: {expr}")

# # محاسبه مشتق توابع مرکب 
# result = diff(expr, x)
# print(result)  

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون
# # Integral in SymPy انتگرال در سیمپای

# from sympy import symbols, integrate
# x = symbols('x')
# expr = x**2
# print(f"Equation: {expr}")

# # محاسبه انتگرال نامعین
# result = integrate(expr, x)
# print(f"Result of Integral: {result}")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون
# # Integral in SymPy انتگرال در سیمپای

# from sympy import symbols, integrate
# x = symbols('x')
# expr = x**2
# print(f"Equation: {expr}")

# # محاسبه انتگرال معین
# result = integrate(expr, (x, 0, 2))
# print(f"Result of Integral: {result}")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون
# # Integral in SymPy انتگرال در سیمپای

# from sympy import symbols, integrate
# from sympy import sin, pi
# x = symbols('x')
# expr = sin(x)
# print(f"Equation: {expr}")

# # محاسبه انتگرال معین توابع مثلثاتی
# result = integrate(expr, (x, 0, pi))
# print(f"Result of Integral: {result}")



# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون
# # Integral in SymPy انتگرال در سیمپای

# from sympy import symbols, integrate
# x = symbols('x')
# y = symbols('y')
# expr = x * y
# print(f"Equation: {expr}")

# # محاسبه انتگرال توابع چند متغیره
# result = integrate(expr, (x, 0, 1), (y, 0, 1))
# print(f"Result of Integral: {result}")


# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون
# # Integral in SymPy انتگرال در سیمپای

# from sympy import N
# from sympy import symbols, integrate, sin
# x = symbols('x')
# expr = integrate(sin(x) / x, (x, 1, 10))
# print(f"Equation: {expr}")

# # محاسبه انتگرال عددی
# result = N(expr)  # تبدیل به عدد تقریبی
# print(f"Result of Integral: {result}")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون
# # Integral in SymPy انتگرال در سیمپای

# from sympy import symbols, integrate
# from sympy import exp
# x = symbols('x')
# expr = exp(-x**2)
# print(f"Equation: {expr}")

# # انتگرال گیری از توالع پیچیده
# result = integrate(expr, x)
# print(f"Result of Integral: {result}")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون
# # Algebraic equation in SymPy معادلات جبری در سیمپای

# from sympy import symbols, Eq, solve
# x = symbols('x')
# expr = Eq(expression1, expression2)  # معادله‌ای به فرم expression1 = expression2
# solution = solve(expr, x)

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون
# # Algebraic equation in SymPy معادلات جبری در سیمپای

# from sympy import symbols, Eq, solve
# x = symbols('x')
# expr = x + 2
# print(f"Equation: {expr}")

# # حل معادله خطی
# solution = solve(expr, x)  # معادله به‌صورت x + 2 = 0
# print(f"Result: {solution}")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون
# # Algebraic equation in SymPy معادلات جبری در سیمپای

# from sympy import symbols, Eq, solve
# x = symbols('x')
# expr = x**2 - 4*x + 3
# print(f"Equation: {expr}")

# # حل معادله درجه دوم
# solution = solve(expr, x)
# print(f"Result: {solution}")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون
# # Algebraic equation in SymPy معادلات جبری در سیمپای

# from sympy import symbols, Eq, solve
# x, y = symbols('x y')

# eq1 = Eq(x + y, 3)
# print(f"Equation 1: {eq1}")

# eq2 = Eq(x - y, 1)
# print(f"Equation 2: {eq2}")

# # حل سیستم معادلات
# solution = solve([eq1, eq2], (x, y))
# print(f"Result: {solution}")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون
# # Algebraic equation in SymPy معادلات جبری در سیمپای

# from sympy import symbols, Eq, solve
# x = symbols('x')
# expr = x**3 - x + 1
# print(f"Equation: {expr}")

# # حل معادلات غیرخطی
# solution = solve(expr, x)
# print(f"Result: {solution}")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون
# # Algebraic equation in SymPy معادلات جبری در سیمپای

# from sympy import solveset, S
# from sympy import symbols, Eq, solve
# x = symbols('x')
# expr = x**2 - 4
# print(f"Equation: {expr}")

# # solveset  حل معادلات با روش 
# solution = solveset(expr, x, domain=S.Reals)
# print(f"Result: {solution}")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون
# # Differential equation in SymPy معادلات دیفرانسیلی در سیمپای
# from sympy import symbols, Function, Eq, dsolve

# x = symbols('x')
# y = Function('y')(x)
# expr = y.diff(x)
# print(f"Equation: {expr}")

# # حل معادله دیفرانسیلی ساده
# eq = Eq(expr, x)
# solution = dsolve(eq, y)
# print(f"Result: {solution}")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون
# # Differential equation in SymPy معادلات دیفرانسیلی در سیمپای
# from sympy import symbols, Function, Eq, dsolve

# x = symbols('x')
# y = Function('y')(x)
# expr = y.diff(x, 2) - 3*y.diff(x) + 2*y
# print(f"Equation: {expr}")

# # حل معادله دیفرانسیلی مرتبه دوم
# eq = Eq(expr, 0)
# solution = dsolve(eq, y)
# print(f"Result: {solution}")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون
# # Differential equation in SymPy معادلات دیفرانسیلی در سیمپای

# from sympy import symbols, Function, Eq, dsolve
# x = symbols('x')
# y = Function('y')(x)

# # حل معادلات دیفرانسیلی غیر خطی
# eq = Eq(y.diff(x), y**2)
# solution = dsolve(eq, y)
# print(f"Result: {solution}")

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون
# # SymPy Examples مثال های مربوط به ماژول سیمپای

# from sympy import symbols, simplify
# x = symbols('x')
# expr = (x**2 + 2*x + 1) / (x + 1)
# result = simplify(expr)
# print(result) 


# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون
# # SymPy Examples مثال های مربوط به ماژول سیمپای

# from sympy import symbols, solve
# x = symbols('x')
# eq = x**2 - 4
# roots = solve(eq, x)
# print(roots)  

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون
# # SymPy Examples مثال های مربوط به ماژول سیمپای

# from sympy import symbols, diff
# x = symbols('x')
# expr = x**3 + 2*x**2 + x
# derivative = diff(expr, x)
# print(derivative) 

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون
# # SymPy Examples مثال های مربوط به ماژول سیمپای

# from sympy import symbols, integrate
# x = symbols('x')
# expr = x**2
# integral = integrate(expr, x)
# print(integral) 

# # -------------------------------------- # 

# # SymPy in Python ماژول سیمپای در پایتون
# # SymPy Examples مثال های مربوط به ماژول سیمپای

# # پیاده سازی سری تیلور
# from sympy import symbols, sin, series
# x = symbols('x')
# expr = sin(x)
# taylor = series(expr, x, 0, 6)
# print(taylor) 

# # -------------------------------------- # 

# SymPy in Python ماژول سیمپای در پایتون
# SymPy Examples مثال های مربوط به ماژول سیمپای

# پیاده سازی مساحت دایره به صورت تحلیلی
from sympy import symbols, pi
r = symbols('r')
area = pi * r**2
print(area) 

