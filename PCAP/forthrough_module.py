# import pkgutil

# def list_package_modules(package):
#     package = __import__(package, fromlist=["dummy"])
#     for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
#         print(f"Module: {modname}, Is Package: {ispkg}")

# list_package_modules("platform")

# -----------------------------------
# import inspect
# import math

# for name, obj in inspect.getmembers(math.sqrt):
#     if inspect.ismodule(obj):
#         print(f"Module: {name}")
#     elif inspect.isclass(obj):
#         print(f"Class: {name}")
#     elif inspect.isfunction(obj):
#         print(f"Function: {name}")

# for i in range(10):
#     pass
#     print(i)
# print(i)



# -------------
# i = 5
# while i > 0:
#     i=i//2
#     if i %2 = 0:
#         break
# else
#     i+=1

# print(i)



# -------------
# for i in range(1,3):
#     print("*", end="")
# else:
#     print("*")



# -------------
# a = [1]
# b = a
# a[0] = 0

# print(b)



# --------------
# a = [0]
# print(a)
# b = a[:]
# c = a
# print(b)
# print("c: ", c)
# a[0] = 1
# print(a, b, c)
# # len(a) == len(b)

# # b[0]-1 == a[0]

# a[0] == b[0]
# print(a[0], b[0], c[0])


# --------------------
# text = "Hello, World!"

# # Extract the last 6 characters
# slice7 = text[-6:]
# print(slice7)  # Output: World!

# # Extract all but the last character
# slice8 = text[1:-2]
# print(slice8)  # Output: Hello, World

# for i in len(text):
#     text[i] = text[i].upper()

# print(text)


# ------------------------
# def fu(a):
#     for i in range(1,a):
#         yield i

# fu(2)


# ----------
# result = 'mike' > 'Mike'
# print(result)


# --------------
# import sys
# import math
# b1 = type(dir(math)) is list
# b2 = type(sys.path) is list
# print(type(sys.path))
# print(b1 and b2)

# import random 
# v1 = random.random()
# print(v1)


# ----------------
# assert angel % 180 != 90

# The code shows an extravagant way
# of leaving the loop.

# the_list = [1, 2, 3, 4, 5]
# ix = 0
# do_it = True

# while do_it:
#     try:
#         print("index",ix)
#         print(the_list[ix])
#         ix += 1
#     except IndexError:
#         print("exception occurred")
#         do_it = False

# print('Done')

# print(chr(ord('z') - 2))

# print('Mike' > "Mikey")
# print('mike' > "Mikey")

# class A:
#     def __str__(self):
#         return 'a'
    
# class B:
#     def __str__(self):
#         return 'b'
    
# class C(B, A):
#     pass

# o = C()
# print(o)


# --------------
# class Person:
#     def __init__(self, name, age):
#         self.namee = name
#         self.age = age

# person = Person("Alice", 30)

# # Check if the person object has the attribute 'name'
# if hasattr(person, 'name'):
#     print(f"Name: {person.name}")

# # Check if the person object has the attribute 'address'
# if hasattr(person, 'address'):
#     print(f"Address: {person.address}")
# else:
#     print("Address attribute does not exist.")


# print(2**10)

# def my_fun():
#     for num in range(3):
#         yield num

# for i in my_fun():
#     print(i)

# print(yield 3)

# None * None

# 16//3

# def func(a, b):
#     return b ** a


# print(func(b=2, 2))

# my_list = [1, 2]

# for v in range(2):
#     my_list.insert(-1, my_list[v])

# print(my_list)

# def func(a, b):
#     return b ** a


# print(func(b=2,a=1))

# print("a", "b", "c", end="sep")

# lst = [[x for x in range(3)] for y in range(3)]
# print(lst)

# lst = [[x for x in range(3)] for y in range(3)]

# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 != 0:
#             print("#")

# foo = (1, 2, 3)
# foo.index(0)

# x = int(input())
# y = int(input())
# x = x % y
# x = x % y
# y = y % x
# print(y)

# dct = {}
# dct['1'] = (1, 2)
# dct['2'] = (2, 1)

# for x in dct.keys():
#     print(dct[x][1], end="")

# dct = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dct['three']

# for k in range(len(dct)):
#     print("k",k)
#     v = dct[v]
#     print(v)

# print(v)

# --------------------
# from datetime import date

# date_1 = date(1992,1,16)
# date_2 = date(1991,2,5)
# print(date_1)

# print(date_1 - date_2)


# # ---------------------------
# from datetime import datetime

# datetime = datetime(2019,11,27,11,27,22)
# print(datetime.strftime("%y/%B/%d %H:%M:%S"))



# ------------------------
# import os
# os.mkdir('pictures')
# os.chdir('pictures')
# os.mkdir('images')
# os.chdir('images')
# os.mkdir('photos')
# os.chdir('../')


# print(os.getcwd())



# -----------------------------
# import calendar

# c = calendar.Calendar()
# print(c)
# print(c.iterweekdays())

# for weekday in c.iterweekdays():
#     print(weekday, end=" ")



# -----------------------
# b = bytearray(3)
# print(b)

# -----------------
# import os
# os.mkdir('pictures')
# os.chdir('pictures')
# sizes = ['small', 'medium', 'large']

# for size in sizes:
#     os.mkdir(size)

# print(os.listdir())

# ---------------------
# import calendar

# print(calendar.weekheader(5))



# -------------------
# x = "\\\\"
# print(len(x))

# --------------------
# from datetime import timedelta

# delta = timedelta(weeks=1, days=7, hours=11)
# print(delta*2)


# import random

# a = random.randint(0,100)
# b = random.randrange(10,100,3)
# c = random.choice((0,100,3))

# print(a)
# print(b)
# print(c)


# -----------------
# try:
#     raise Exception
# except:
#     print("c")
# except BaseException:
#     print("a")
# except Exception:
#     print("b")


# # -----------------
# try:
#     raise Exception(1,2,3)
# except Exception as e:
#     print(len(e.args))


# class A:
#     A = 1
#     B = 10
#     c = None
#     def __init__(self):
#         self.a = 0

# print(hasattr(A, 'c'))


# ------------------
# import os

# os.mkdir('pictures')
# os.chdir('pictures')

# print(os.getcwd())


# ----------------
# numbers = [i*i for i in range(5)]
# foo = list(filter(lambda x: x%2, numbers))

# print(foo)

# ------------------------
# class A:
#     def __init__(self):
#         pass

# a = A(1)
# print(hasattr(a, 'A'))


# # ------------------
# from datetime import datetime

# datetime1 = datetime(2019,11,28,11,27,22)
# datetime2 = datetime(2019,11,27,0,0,0)

# print(datetime1 - datetime2)



# -------------------
# print(11*60)


# --------------------
# import math
# print(math.e)
# print(math.pow(2,4))

# result = math.e != math.pow(2,4)
# print(result)
# print(int(result))



# -------------------
# for i in range(10):
#     pass

# print(i)


# -----------------
# for i in range(1,3):
#     print("*", end="")
#     print(i)
# else:
#     print("*")
#     print(i)


# --------------
# a = 2
# if a>0:
#     a+=1
#     else:
#         a-=1
# print(a)

# ------------------
# class A:
#     VarA = 1
#     def __init__(self):
#         self.prop_a = 1

# class B(A):
#     VarA = 2
#     def __init__(self):
#         self.prop_a = 2
#         self.prop__aa = 2

# class C(B):
#     def __init__(self):
#         super.__init__()

# obj_a = A()
# obj_b = B()
# obj_c = C()

# # print (i for i in obj_a)
# # print (i for i in obj_b)
# # print (i for i in obj_c)
# hasattr(obj_b, 'prop_aa')
# 'VarA' in obj_b.__dict__



# ---------------------
# import os
# os.mkdir('picturess')
# os.chdir('picturess')

# print(os.getcwd())
# print(os.uname())

# what are the two ansers from below options?
# 1. operating system Name
# 2. current path
# 3. last login date
# 4. hardware identifier


# --------------------
# import math as u

# dir(math)


# ---------------
# from math import e, exp, log

# print(pow(e, 1) == exp(log(e)))
# print(pow(2, 2) == exp(2 * log(2)))
# print(log(e, e) == exp(0))

# print(pow(e, 1))
# print(exp(log(e)))
# print(pow(2, 2))
# print(exp(2 * log(2)))
# print(log(e, e))
# print(exp(0))

# print("log 2: ", log(2))
# print("log 1: ", log(1))
# # print("log 0: ", log(0))
# print("e to 0:", exp(0))
# print("e to 1:", exp(1))



# # ----------------
# from platform import platform

# print(platform())
# print(platform(1))
# print(platform(0, 1))



# ----------------------
import os
# from platform import platform, system, release, version, machine, processor, python_version

# # Platform module examples
# print("Platform:", platform())
# print("System:", system())
# print("Release:", release())
# print("Version:", version())
# print("Machine:", machine())
# print("Processor:", processor())
# print("Python Version:", python_version())

# # OS module examples
# print("OS Name:", os.name)
# print("Current Working Directory:", os.getcwd())
# os.mkdir('example_dir')
# os.chdir('example_dir')
# print("New Working Directory:", os.getcwd())
# os.chdir('..')
# os.rmdir('example_dir')


# def foo(x,y,z):
#     return x(y) -x(z)

# print(foo(lambda x:x % 2, 2, 1))



lis = [i for i in range(5, 0, -1)]
m = [lis[i] for i in range(5) if lis{i} % 2 == 0]

print(m)