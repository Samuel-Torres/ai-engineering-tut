"""
5 Types of Errors:

IndexError: This error occurs when you try to access an index that is out of the range of a list or a string.
KeyError: This error occurs when you try to access a key that does not exist in a dictionary.
ZeroDivisionError: This error occurs when you try to divide a number by zero.
TypeError: This error occurs when you perform an operation on a value of an inappropriate type.
NameError: This error occurs when you try to use a variable that has not been defined.

"""

# Examples:

# IndexError
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError as e:
    print("IndexError caught:", e)

# KeyError
my_dict = {"a": 1, "b": 2}
try:
    print(my_dict["c"])
except KeyError as e:
    print("KeyError caught:", e)

# ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError caught:", e)

# TypeError
try:
    result = "10" + 5
except TypeError as e:
    print("TypeError caught:", e)

# NameError
try:
    print(undefined_variable)
except NameError as e:
    print("NameError caught:", e)
