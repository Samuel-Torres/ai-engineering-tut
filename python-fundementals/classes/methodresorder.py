"""
Mothod Resolution Order (MRO) in Python determines the order in which base classes are searched when executing a method.
    It is especially important in the context of multiple inheritance, where a class can inherit from more than one base class.
    Python uses the C3 linearization algorithm to establish the MRO, ensuring a consistent and predictable order of method resolution.
"""


class A:
    label = "A: Bass Class"


class B(A):
    label = "B: Masala Blend"


class C(A):
    label = "C: Herbal Blend"


class D(C, B):
    # prints B first because of method resolution order (MRO)... in other words, the first class listed in the parentheses takes precedence.
    pass


cup = D()
print(cup.label)  # Output: B: Masala Blend
print(D.__mro__)
