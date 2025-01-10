# # Object-Oriented Programming (OOP) in Python برنامه نویسی شئ گرایی در پایتون

# # __init__ Synatx:

# """
# class ClassName:
#     def __init__(self, arg1, arg2, ...):
#         self.attribute1 = arg1
#         self.attribute2 = arg2
# """

# # -------------------------------------- # 

# # Object-Oriented Programming (OOP) in Python برنامه نویسی شئ گرایی در پایتون

# # __init__ Example:

# class Person:
#     def __init__(self, name, age):
#         self.name = name  # ویژگی name
#         self.age = age    # ویژگی age

# # ایجاد اشیاء از کلاس Person
# person1 = Person("Ali", 25)
# person2 = Person("Sara", 30)

# # نمایش ویژگی‌های اشیاء
# print(person1.name, person1.age) 
# print(person2.name, person2.age)  

# # -------------------------------------- # 

# # Object-Oriented Programming (OOP) in Python برنامه نویسی شئ گرایی در پایتون

# # __init__ Example:
# class Person:
#     def __init__(self, name, age):
#         self.name = name  # ویژگی نمونه
#         self.age = age    # ویژگی نمونه

#     def greet(self):
#         return f"Hello, my name is {self.name} and I am {self.age} years old."

# # ساخت یک شئ از کلاس (ایجاد یه نمونه از کلاس)
# Reza = Person("REZA", 24)
# Mahdi = Person("MAHDI", 30)


# # فراخوانی رفتار برای نمونه ایجاد شده
# print(Reza.greet()) 
# print(Mahdi.greet()) 

# # -------------------------------------- # 

# # Object-Oriented Programming (OOP) in Python برنامه نویسی شئ گرایی در پایتون

# # __init__ Example:
# class Person:
#     def __init__(name, age):  # Missing 'self'
#         self.name = name      # Error: 'self' is not defined
#         self.age = age
#     def greet():
#         return f"Hello, my name is {self.name} and I am {self.age} years old."

# Reza = Person("Reza", 24)
# print(Reza.greet())

# # -------------------------------------- # 

# # Object-Oriented Programming (OOP) in Python برنامه نویسی شئ گرایی در پایتون

# # __str__  Example:

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}"

# # ساخت یک شیء
# person = Person("Ali", 25)

# # استفاده از print یا str
# print(person)      
# print(str(person))   

# # -------------------------------------- # 

# # Object-Oriented Programming (OOP) in Python برنامه نویسی شئ گرایی در پایتون

# # __repr __  Example:
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return f"Person(name={self.name!r}, age={self.age!r})"
    

# # ساخت یک شیء
# person = Person("Ali", 25)

# # استفاده از repr
# print(repr(person))  

# # -------------------------------------- # 

# Object-Oriented Programming (OOP) in Python برنامه نویسی شئ گرایی در پایتون

# # class without __str__ , __repr__ ساخت کلاس بدون
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# person = Person("Ali", 25)

# print(person)

# # -------------------------------------- # 

# # Object-Oriented Programming (OOP) in Python برنامه نویسی شئ گرایی در پایتون

# # The difference between __str__ vs __repr__ تفاوت بین  
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}"
#     def __repr__(self):
#         return f"Person(name={self.name!r}, age={self.age!r})"
    

# person = Person("Ali", 25)
# print(person)       
# print(str(person))
# print(repr(person))  

# # -------------------------------------- # 

# # Object-Oriented Programming (OOP) in Python برنامه نویسی شئ گرایی در پایتون

# # Instance Methods Example:  مثال توابع وابسته نمونه

# class Person:
#     def __init__(self, name, age):
#         self.name = name  # ویژگی نمونه
#         self.age = age
#     def greet(self):
#         return f"Hello, my name is {self.name} and I am {self.age} years old."
    
# # استفاده از تابع وابسته نمونه
# person1 = Person("Ali", 25)
# print(person1.greet())  

# # -------------------------------------- # 

# # Object-Oriented Programming (OOP) in Python برنامه نویسی شئ گرایی در پایتون

# # Class Methods Example:  مثال توابع وابسته کلاس
# class Person:
#     population = 0  # ویژگی کلاس
#     def __init__(self, name):
#         self.name = name
#         Person.population += 1
#     @classmethod
#     def get_population(cls):
#         return f"There are {cls.population} people."
    
# # استفاده از تابع وابسته کلاس
# print(Person.get_population()) 

# person1 = Person("Ali")
# print(Person.get_population())  

# person2 = Person("Reza")
# print(Person.get_population())

# # -------------------------------------- # 

# # Object-Oriented Programming (OOP) in Python برنامه نویسی شئ گرایی در پایتون

# # Static Methods Example:  مثال توابع وابسته ایستا
# class MathUtils:
#     @staticmethod
#     def add(a, b):
#         return a + b
    
# # استفاده از تابع وابسته ایستا
# print(MathUtils.add(5, 3)) 

# print(MathUtils.add(9, 1)) 

# print(MathUtils.add(20, 4)) 

# # -------------------------------------- # 

# # Object-Oriented Programming (OOP) in Python برنامه نویسی شئ گرایی در پایتون

# # Methods Example:  مثال استفاده از توابع وابسته مختلف در یک مسئله
# class Calculator:
#     def __init__(self, name):
#         self.name = name

#     def instance_method(self, x, y):
#         return f"{self.name} adds: {x + y}"

#     @classmethod
#     def class_method(cls, x, y):
#         return f"Class adds: {x + y}"

#     @staticmethod
#     def static_method(x, y):
#         return f"Static adds: {x + y}"

# # استفاده از توابع وابسته
# calc = Calculator("MyCalculator")
# print(calc.instance_method(3, 4)) # تابع وابسته نمونه
# print(Calculator.class_method(3, 4))  # تابع وابسته کلاس
# print(Calculator.static_method(3, 4))  # تابع وابسته ایستا

# # -------------------------------------- # 

# # Object-Oriented Programming (OOP) in Python برنامه نویسی شئ گرایی در پایتون

# # Inheritance in Python وراثت در پایتون
# class ParentClass:
#     # Parent class definition
#     pass

# class ChildClass(ParentClass):
#     # Child class definition
#     pass

# # -------------------------------------- # 

# # Object-Oriented Programming (OOP) in Python برنامه نویسی شئ گرایی در پایتون

# # Inheritance in Python وراثت در پایتون
# # وراثت تک گانه
# class Animal:
#     def speak(self):
#         return "I make a sound."

# class Dog(Animal):
#     def speak(self):
#         return "Woof! Woof!"

# # Create objects
# animal = Animal()
# dog = Dog()

# print(animal.speak()) 
# print(dog.speak())   

# # -------------------------------------- # 

# # Object-Oriented Programming (OOP) in Python برنامه نویسی شئ گرایی در پایتون

# # Inheritance in Python وراثت در پایتون

# # overriding بازنویسی کلاس والد توسط کلاس های فرزند
# class Parent:
#     def greet(self):
#         return "Hello from the parent class!"

# class Child(Parent):
#     def greet(self):
#         return "Hello from the child class!"

# # Test overriding
# obj = Child()
# print(obj.greet())

# # -------------------------------------- # 

# # Object-Oriented Programming (OOP) in Python برنامه نویسی شئ گرایی در پایتون

# # Inheritance in Python وراثت در پایتون
# # Super() Example مثالی از تابع 

# class Parent:
#     def greet(self):
#         return "Hello from Parent!"

# class Child(Parent):
#     def greet(self):
#         return super().greet() + " And hello from Child!"

# # Test super()
# obj = Child()
# print(obj.greet()) 

# # -------------------------------------- # 

# # Object-Oriented Programming (OOP) in Python برنامه نویسی شئ گرایی در پایتون

# # Inheritance in Python وراثت در پایتون
# #  وراثت چندگانه در پایتون
# class A:
#     def method_a(self):
#         return "Method from class A"

# class B:
#     def method_b(self):
#         return "Method from class B"

# class C(A, B):
#     pass

# # Test multiple inheritance
# obj = C()
# print(obj.method_a()) 
# print(obj.method_b()) 

# # -------------------------------------- # 

# # Object-Oriented Programming (OOP) in Python برنامه نویسی شئ گرایی در پایتون

# # Inheritance in Python وراثت در پایتون
# # multi-level inheritance وراثت چندسطحی

# class Animal:
#     def breathe(self):
#         return "I am breathing"

# class Mammal(Animal):
#     def walk(self):
#         return "I am walking"

# class Dog(Mammal):
#     def bark(self):
#         return "Woof! Woof!"

# # Test multi-level inheritance
# dog = Dog()
# print(dog.breathe()) 
# print(dog.walk())     
# print(dog.bark())     

# # -------------------------------------- # 

# # Object-Oriented Programming (OOP) in Python برنامه نویسی شئ گرایی در پایتون

# # Polymorphism in Python چندریختی در پایتون

# # ترکیب چندریختی با ارث بری
# class Animal:
#     def sound(self):
#         return "Some generic sound"
# class Dog(Animal):
#     def sound(self):
#         return "Woof! Woof!"
# class Cat(Animal):
#     def sound(self):
#         return "Meow!"

# animals = [Dog(), Cat(), Animal()]
# for animal in animals:
#     print(animal.sound())

# # -------------------------------------- # 

# # Object-Oriented Programming (OOP) in Python برنامه نویسی شئ گرایی در پایتون

# # Polymorphism in Python چندریختی در پایتون

# # Duck Typing ترکیب چند ریختی با 
# class Bird:
#     def fly(self):
#         return "Flying high"
# class Airplane:
#     def fly(self):
#         return "Taking off"
# def lift_off(entity):
#     print(entity.fly())
    
# lift_off(Bird())     
# lift_off(Airplane())  
